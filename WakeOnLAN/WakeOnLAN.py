
from wakeonlan import send_magic_packet
from time import sleep
from pathlib import Path
from core.json__ import *


computers_folder = Path("computers")
computers_folder.mkdir(exist_ok=1)

desktop_json_file = computers_folder / "desktop.json"
laptop_json_file = computers_folder / "laptop.json"
server_json_file = computers_folder / "server.json"

desktop_json = read_json_from_file(desktop_json_file)
laptop_json = read_json_from_file(laptop_json_file)
server_json = read_json_from_file(server_json_file)

class NetworkSpecs:
    def __init__(self, ip, mac):
        self.ip = ip
        self.mac = mac

desktop = NetworkSpecs(desktop_json["ip_address"], desktop_json["mac_address"])
laptop = NetworkSpecs(laptop_json["ip_address"], laptop_json["mac_address"])
server = NetworkSpecs(server_json["ip_address"], server_json["mac_address"])



def WakeOnLANPersistent(mac_adress, total_tries=1000):
    if total_tries <= 0:
        raise ValueError(f"total_tries=({total_tries}) should be positive and greater than 0")

    for _ in range(total_tries):
        send_magic_packet(mac_adress)
        print(f"magic packet sent to: {mac_adress} with FFFF and its mac address.")
        # sleep(0.001)


WakeOnLANPersistent(desktop.mac, -1)
WakeOnLANPersistent(server.mac)
