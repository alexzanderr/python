#!/usr/bin/python3

import os
import subprocess as s
import time
import platform


def get_uptime():
    process = s.Popen("cat /proc/uptime", shell=True, stdout=s.PIPE, stderr=s.PIPE)
    output, _ = process.communicate()
    output = output.decode("utf-8")
    output = output.strip()
    return float(output.split()[0])


def print_uptime():
    while 1:
        os.system("clear")

        print(f"python3 --version: {platform.python_version()}\n")

        # print(neofetch)
        total_seconds = get_uptime()
        total_hours = int(total_seconds // 3600)
        if total_hours == 0:
            minutes = int(total_seconds / 60)
            seconds = int(total_seconds % 60)

        else:
            hours = int(total_hours)
            _seconds = int(total_seconds % 3600)

            minutes = int(_seconds / 60)
            seconds = int(_seconds % 60)

        hours = str(hours)
        minutes = str(minutes)
        seconds = str(seconds)
        # print(f"Total Seconds: {total_seconds}")
        # print(f"Minutes: {minutes}")
        # print(f"Seconds: {seconds}")
        print(f"Platform: {platform.platform()}\n")
        print(f"{' '*8}[ Hours : Minutes : Seconds ]")
        # if int(seconds) < 10:
        #     print(f"Uptime: [ {minutes.center(8)}:{seconds.center(8)} ]", end="\r")
        # else:
        print(f"Uptime: [{hours.center(7)}:{minutes.center(9)}:{seconds.center(9)}]")

        time.sleep(1)

if __name__ == "__main__":
    try:
        print_uptime()
    except KeyboardInterrupt:
        print("\nstopped.")