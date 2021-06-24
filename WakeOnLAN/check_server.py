

from core.system import clearscreen
from core.json__ import *
from core.logging__ import *
from core.datetime__ import *
from time import sleep
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
desktop_json = read_json_from_file("computers/server.json")
hostname = desktop_json["ip_address"]
port = 22

logger_server = Loggerr("ServerChecker")

def check_online(hostname, port):
    try:
        print(f"checking {hostname}:{port} ...")
        s.connect((hostname, port))
        s.close()
        return True

    except socket.error as e:
        print(e)
        return False


clearscreen()
while 1:
    result = check_online(hostname, port)
    if result:
        status = "ONLINE"
    else:
        status = "OFFLINE"

    curr_datetime = get_current_datetime()
    logger_server.info(f"server {hostname}:{port} is {status} at: {curr_datetime}")

    sleep(60)