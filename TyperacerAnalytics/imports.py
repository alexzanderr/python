


import os
from pathlib import Path

friend_ip = "192.168.1.106"


import platform
operating_system = platform.system().lower()

linux = operating_system == "linux"

if operating_system == "windows":
    analytics_folder = Path(r"D:\Alexzander__\PythonApplicationsAppData\TyperacerAnalytics\analytics")
    all_time_analytics_folder = Path(r"D:\Alexzander__\PythonApplicationsAppData\TyperacerAnalytics\all_time_analytics")

elif operating_system == "linux":
    analytics_folder = Path("/home/alexzander/Alexzander__/PythonApplicationsAppData/TyperacerAnalytics/analytics")

    all_time_analytics_folder = Path("/home/alexzander/Alexzander__/PythonApplicationsAppData/TyperacerAnalytics/all_time_analytics/")


analytics_folder.mkdir(exist_ok=True)
all_time_analytics_folder.mkdir(exist_ok=True)

ten_fast_fingers_com = "10fastfingers.com"
play_typeracer_com = "play.typeracer.com"
typing_io = "typing.io"