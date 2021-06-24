

# python
import os
import json
import socket
import platform
import argparse
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
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
        print(f"{request_type} Response sent with this data:")
        print(response)
        print()


    def send_response_back(self, request_type, **kwargs):
        json_response = self.format_response(request_type, **kwargs)
        self.wfile.write(json_response.encode("utf-8"))
        self.print_details(json_response, request_type)


    def do_GET(self):
        """ GET REQUEST """

        self._set_headers()
        request_type = "GET"
        self.send_response_back(request_type)


    def do_HEAD(self):
        """ HEAD REQUEST """

        self._set_headers()
        request_type = "HEAD"
        self.send_response_back(request_type)


    def do_POST(self):
        """ POST REQUEST """

        self._set_headers()
        request_type = "POST"

        # size of data
        content_length = int(self.headers['Content-Length'])
        # data
        post_data = self.rfile.read(content_length)
        post_data = post_data.decode("utf-8")

        try:

            request_data_json = json.loads(post_data)
            print("POST Request received with data:")
            print(json.dumps(
                request_data_json, indent=4
            ))
            print()

            self.send_response_back(request_type, received_data=request_data_json)

        except json.JSONDecodeError as error:
            print(error)
            print("~" * 50)
            print("Data:")
            print(post_data)

        # save the data to file
        with open("google_searches.log", "a+", encoding="utf-8") as logger:
            logger.write(f"[{request_data_json['datetime']}] [{request_data_json['search']}]\n")

        with open("total_google_searches.log", "w+", encoding="utf-8") as file:
            file.truncate(0)
            with open("google_searches.log", "r+", encoding="utf-8") as logger:
                file.write(str(len(logger.readlines())))



def get_operating_system():
    return platform.system().lower()


def run(
    address="localhost",
    port=8000
):
    operating_system = get_operating_system()
    if operating_system == "windows":
        os.system("cls")
    else:
        os.system("clear")

    server_address = (address, port)
    http_server = HTTPServer(server_address, SimpleHTTPServer)

    print(f"Started {SimpleHTTPServer.__name__} SERVER\
           \nListening on [ {f'http://{address}:{port}/'} ] ...\n")
    print(f"cwd: {os.getcwd()}\n")

    http_server.serve_forever()


def is_port_in_use(port):
    print(f"checking if port: [ {port} ] is in use...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("done.")
        return s.connect_ex(('localhost', port)) == 0


def get_this_machine_IP():
    print("getting current ip address...")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    server_ip_address = s.getsockname()[0]
    s.close()

    print("done.")
    return server_ip_address


if __name__ == "__main__":
    default_ip_address = get_this_machine_IP()
    default_port = 8080 # because HTTP

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
        print(f"\n{SimpleHTTPServer.__name__} server OFFLINE.\n")

