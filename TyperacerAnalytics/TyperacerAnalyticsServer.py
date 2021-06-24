
"""
    TyperacerAnalytics/TyperacerAnalyticsServer.py

    this server receives data from brave extension
    and
    saves the data locally on windows and linux
"""

# python
import os
import json
import socket
import requests
import argparse
import subprocess
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

# project

import platform
operating_system = platform.system().lower()

linux = operating_system == "linux"


from TyperacerAnalytics.imports import *
from core.everything import *
from core.linuxapi import linux_notification

logger_TyperacerAnalyticsWebServer = Loggerr(
    "TyperacerAnalyticsWebServer",
    foldername="logs"
)

remote_default_server = "192.168.1.234"
remote_default_port = "8500"

def POSTRequest(ip_address, port, data):
    url = f"http://{ip_address}:{port}/"
    try:
        response = requests.post(url, json=data)

    except requests.RequestException as exception:
        print("there is a request error:")
        print(exception)

    else:
        if response.status_code != 200:
            print(f"server: {ip_address} is OFFLINE.")
            print(f"status code: {response.status_code}")
        else:
            print(f"server: {ip_address} is ONLINE.")
            print(f"status code: {response.status_code}")
            print("data:")
            print(data)
            print("sent successsfully!")


def CheckRemoteServerONLINE(ip_address, port):
    url = f"http://{ip_address}:{port}/"
    try:
        print("checking for remote server...\n")
        response = requests.get(url)

    except requests.RequestException as exception:
        print(f"TyperacerAnalyticsRemoteServer: {orange_underlined(url)} [ {red_bold('OFFLINE')} ]")
        print(f"warning: data saved from typeracer will be saved only on this machine ({get_this_machine_IP()})")
        for _ in range(6):
            print("|||")

    else:
        if response.status_code == 200:
            print(f"TyperacerAnalyticsRemoteServer: {orange_underlined(url)} [ {green_bold('ONLINE')} ]")
            print(f"info: data saved from typeracer will ALSO be saved on this linux server")
            for _ in range(6):
                print("|||")
        else:
            print(f"code: {response.status_code}")



class TyperacerAnalyticsServer(BaseHTTPRequestHandler):
    total_requests = 0
    post_requests = 0
    get_requests = 0
    head_requests = 0

    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()


    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.

        """
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!


    def format_response(self, request_type, **kwargs):
        response_json = {
            "request_type": request_type,
            "status_code": 200,
            "request_date": datetime.now().strftime("%d.%m.%Y-%H:%M:%S"),
            "user_ip": self.client_address[0],
            "server_ip": default_ip_address,
            "server_port": default_port,
        }
        if kwargs:
            for key, value in kwargs.items():
                response_json.update({key: value})

        return json.dumps(response_json, indent=4)


    def print_details(self, response, request_type):
        print(f"Request number [ __ {self.total_requests} __ ]")

        if request_type == "GET":
            print(f"{request_type} request number [ __ {self.get_requests} __ ]")
        elif request_type == "POST":
            print(f"{request_type} request number [ __ {self.post_requests} __ ]")
        elif request_type == "HEAD":
            print(f"{request_type} request number [ __ {self.head_requests} __ ]")

        print(f"\n{request_type} Response sent with this data:")
        print(response)
        print()


    def send_response_back(self, request_type, **kwargs):
        json_response = self.format_response(request_type, **kwargs)
        self.wfile.write(json_response.encode("utf-8"))
        self.print_details(json_response, request_type)
        return json_response


    def do_GET(self):
        """ GET REQUEST """
        self.total_requests += 1
        self.get_requests += 1

        self._set_headers()
        request_type = "GET"
        resp = self.send_response_back(request_type)


        logger_TyperacerAnalyticsWebServer.info(
            f"{request_type} REQUEST received; what was sent back as RESPONSE\n{resp}",
            print__=False
        )


    def do_HEAD(self):
        """ HEAD REQUEST """
        self.total_requests += 1
        self.get_requests += 1

        self._set_headers()
        request_type = "HEAD"
        self.send_response_back(request_type)


    def do_POST(self):
        self.total_requests += 1
        self.post_requests += 1

        # if linux:
        #     if self.client_address[0] != friend_ip:
        #         self._set_headers(403)
        #         print(self.client_address[0])
        #         print("blocked.")
        #         return

        self._set_headers()
        request_type = "POST"

        # size of data
        content_length = int(self.headers['Content-Length'])
        # data
        post_data = self.rfile.read(content_length)
        decoded_data = post_data.decode('utf-8')

        try:

            request_data_json = json.loads(decoded_data)
            self.send_response_back(request_type, received_data=request_data_json)

            # immediately after receiving POST request
            # another POST request is sent to home server
            # POSTRequest(remote_default_server, remote_default_port, request_data_json)

        except json.JSONDecodeError as error:
            print_red_bold(error)
            print("~" * 50)
            print("Data:")
            print(post_data)

        pretty_data = json.dumps(request_data_json, indent=4)
        colored_data = lime_green(pretty_data)
        logger_TyperacerAnalyticsWebServer.info(f"POST request received with data:\n{colored_data}")

        if linux:
            linux_notification(
                request_data_json["url"],
                f"{request_data_json['wpm']} wpm\n{request_data_json['accuracy']}% accuracy"
            )


        if "url" in request_data_json.keys():
            self.SaveData(request_data_json)


    def SaveData(self, request_data_json: dict):
        """[
            this function saves the data coming from POST request
            to a json corespondently to its date and website

            after save, updates automatically the results
            by
                generating stats
            and
                plotting the generate stats
        ]

        Args:
            request_data_json (dict): [
                a JSON that is coming from the extension with results
                of typing race
            ]
        """
        time = request_data_json['time']
        time = "_".join(time.split(":"))

        date = request_data_json['date']

        # analytics_folder is in remote appdata for this machine
        current_date_folder = analytics_folder / date
        if not current_date_folder.exists():
            current_date_folder.mkdir()


        # setting up JSON file name
        url = request_data_json["url"]
        if ten_fast_fingers_com in url:
            results_file_path = f"{ten_fast_fingers_com}_results.json"

        elif play_typeracer_com in url:
            results_file_path = f"{play_typeracer_com}_results.json"

        elif typing_io in url:
            results_file_path = f"{typing_io}_results.json"

        results_file_path = current_date_folder / results_file_path
        if results_file_path.exists():
            _json = read_json_from_file(results_file_path)

            # adding new sessions data to existing JSON
            _json.append(request_data_json)
            write_json_to_file(_json, results_file_path)


        else:
            # creating for the first time
            write_json_to_file([request_data_json], results_file_path)



        print("Result saved at:")

        print_cyan_bold(results_file_path.as_posix() + "\n")


        subprocess.call(["python", "StatsGenerator.py"])
        print("--- stats generated.")

        subprocess.call(["python", "PlotStats.py"])
        print("--- stats plotted.")

        print(f"\nResults {lime_green_bold('updated')} successfully!\n\n")


def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


def get_this_machine_IP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    server_ip_address = s.getsockname()[0]
    s.close()

    return server_ip_address


def run(
    address="localhost",
    port=8000
):
    if windows:
        os.system("cls")
    else:
        os.system("clear")

    server_address = (address, port)
    http_server = HTTPServer(server_address, TyperacerAnalyticsServer)


    CheckRemoteServerONLINE(remote_default_server, remote_default_port)

    print(f"Started {lime_green_bold(TyperacerAnalyticsServer.__name__)} SERVER on machine - {get_this_machine_IP()}\nListening on [ {underlined(f'http://{address}:{port}/')} ] (Windows 10) ...\n")
    print(f"cwd: {lime_green_underlined(os.getcwd())}\n")



    http_server.serve_forever()


if __name__ == "__main__":
    default_ip_address = "localhost"
    default_port = 8000

    while is_port_in_use(default_port):
        print(f"port: {default_port} IN USE.")
        default_port += 1

    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default=default_ip_address,
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=default_port,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()

    try:
        run(address=args.listen, port=args.port)

    except KeyboardInterrupt:
        print(f"\nServer: [ {lime_green_bold(TyperacerAnalyticsServer.__name__)} ] {red_bold('closed')} from [ {red_bold(KeyboardInterrupt.__name__)}]\n")


    except Exception as exception:
        logger_TyperacerAnalyticsWebServer.exception("error in server")
