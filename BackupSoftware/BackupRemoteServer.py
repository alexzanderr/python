
import os
import json
import socket
import argparse
import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

import sys
from dependencies import *

from string import Template
unzip_command_template = Template(
    "unzip -o ${zip_path}"
)

global_ip = None
global_port = None
class BackupSoftwareServer(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()


    def format_response(self, request_type, **kwargs):
        response_json = {
            "request_type": request_type,
            "status_code": 200,
            "request_date": datetime.now().strftime("%d.%m.%Y-%H:%M:%S"),
            "user_ip": self.client_address[0],
            "server_ip": global_ip,
            "server_port": global_port,
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

            if "folder" in request_data_json.keys():
                folder_path = request_data_json["folder"]
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

            elif "extract" in request_data_json.keys():
                if request_data_json["extract"]:
                    zpath = request_data_json["zip_path"]

                    cwd = os.getcwd()
                    os.chdir(server_backup_folder)
                    # xtract process
                    subprocess.call(unzip_command_template.safe_substitute(
                        zip_path = zpath
                    ), shell=True)
                    # after xtract delete the zip
                    os.chdir(cwd)

                    del cwd, zpath

                self.send_response_back(
                    request_type,
                    received_data=request_data_json,
                    extract_result="success"
                )

        except json.JSONDecodeError as error:
            pass



def run(
    address="localhost",
    port=8000
):
    global global_ip, global_port
    operating_system = get_operating_system()
    if operating_system == "windows":
        os.system("cls")
    else:
        os.system("clear")

    server_address = (address, port)
    http_server = HTTPServer(server_address, BackupSoftwareServer)
    global_ip = address
    global_port = port

    print(f"Started BackupSoftwareServer\nListening on [ {f'http://{address}:{port}/'} ] ...\n")
    print(f"cwd: {os.getcwd()}\n")
    http_server.serve_forever()


def get_operating_system():
    return platform.system().lower()


def is_port_in_use(port):
    print(f"checking if port: [ {port} ] is in use...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("done.")
        return s.connect_ex(('localhost', port)) == 0


def get_this_machine_IP():
    print("getting current ip address...")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 10))
    server_ip_address = s.getsockname()[0]
    s.close()

    print("done.")
    return server_ip_address


if __name__ == "__main__":
    default_ip = get_this_machine_IP()
    default_port = 6000

    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default=default_ip,
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
        print(f"\nBackupSoftwareServer server OFFLINE.\n")