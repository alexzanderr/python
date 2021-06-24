#!/usr/bin/python3

"""
    202020 order helpful application for eye health stabilitty
"""

from collections import namedtuple

TimeInterval = namedtuple("TimeIntervals", ["name", "seconds"])
TimeIntervals = [
    TimeInterval(name=_name, seconds=_value) for _name, _value in (
        ("millennia", 60 * 60 * 24 * 365 * 1000),
        ("century", 60 * 60 * 24 * 365 * 100),
        ("decade", 60 * 60 * 24 * 365 * 10),
        ("year", 60 * 60 * 24 * 365),
        ("week", 60 * 60 * 24 * 7),
        ("day", 60 * 60 * 24),
        ("hour", 60 * 60),
        ("minute", 60),
        ("second", 1)
    )
]

def seconds_to_time(seconds):
    """
        example of result:
        Time(
            millennials=0,
            centuries=0,
            decades=5,
            years=1,
            weeks=9,
            days=2,
            hours=0,
            minutes=38,
            seconds=5
        )
        you can select whatever you want from this named tuple
    """
    if type(seconds) not in [str, int, float]:
        raise TypeError(f"seconds: {type(seconds)}; not int or str")

    seconds = int(seconds)
    intervals = ["millennials", "centuries", "decades", "years", "weeks", "days", "hours", "minutes", "seconds"]
    TimeDict = dict(zip(intervals, [0] * len(intervals)))
    # {'millennials': 0, 'centuries': 0, 'decades': 0, 'years': 0, 'days': 0, 'hours': 0, 'minutes': 0, 'seconds': 0}

    for (_, _seconds), k in zip(TimeIntervals, intervals):
        result = seconds // _seconds
        seconds -= result * _seconds
        TimeDict[k] = result

    for i, inter in enumerate(intervals):
        if TimeDict[inter] != 0:
            values = list(TimeDict.values())[i:]
            return namedtuple("Time", intervals[i:])(*values)

    return namedtuple("Time", "seconds")(seconds)


from datetime import datetime

def get_current_time(__format="%H:%M:%S"):
    return datetime.now().strftime(__format)

def get_current_datetime(__format="%d.%m.%Y-%H:%M:%S"):
    return datetime.now().strftime(__format)


end = "\033[0m"
bold = "\033[1m"
underlined_effect = "\033[4m"
reversed_effect = "\u001b[7m"
yellow = "\033[93m"
red = "\033[91m"


def yellow_bold(__string):
    return yellow + bold + __string + end


def red_bold(__string):
    return red + bold + __string + end



import json
def read_json_from_file(__path: str):
    """ reads .json from @path"""

    if isinstance(__path, str):
        with open(__path, "r+", encoding="utf-8") as _json:
            return json.loads(_json.read())

    elif isinstance(__path, Path):
        return json.loads(__path.read_text())

    else:
        raise TypeError(
            f"{__path} is not type str; type({__path})=={type(__path)}")


# pypi
import subprocess
from time import sleep
try:
    from playsound import playsound
except ImportError:
    process = subprocess.Popen("pip3 install playsound", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, _ = process.communicate()
    output = output.decode("utf-8")
    print(output)
    sleep(2)

    try:
        from playsound import playsound
    except ImportError:
        print("it was installed, but importing after install from code doesnt work")


import os
import sys
from pathlib import Path

from string import Template

notify_send_template = Template(
    "notify-send '${title}' '${message}'"
    " --icon=${icon}"
)


def linux_notification(title, message, icon):
    subprocess.call(notify_send_template.safe_substitute(
        title=title,
        message=message,
        icon=icon
    ), shell=True)


__appname__ = "202020Rule"

sounds_folder = Path("sounds")

sounds_json = read_json_from_file(sounds_folder / "sounds.json")

psaltirea_reminder_icon = Path("icons") / "202020-order-icon.png"



# project_logs_folder = Path("logs")
# project_logs_folder.mkdir(exist_ok=1)
#
# # stream handler
# stream_handler_FaceCamLog = logging__.get_stream_handler()
# # file handler
# file_handler_FaceCamLog = logging__.get_file_handler_with_datetime(
#     project_logs_folder.as_posix(),
#     "announcements"
# )
# # logger
# logger_20_20_20 = logging__.Loggerr(
#     name="202020Rule.py",
#     file_handler=file_handler_FaceCamLog,
#     stream_handler=stream_handler_FaceCamLog
# )
# logger_20_20_20.info(f"application {__appname__} loaded.")


def comma_sound():
    playsound(sounds_json["comma"])

def warning_sound():
    playsound(sounds_json["warning"])

def bizwarn_sound():
    playsound(sounds_json["bizwarn"])


def notification_sound():
    playsound(sounds_json["it"])
    playsound(sounds_json["is"])
    playsound(sounds_json["time"])
    playsound(sounds_json["for"])
    playsound(sounds_json["beyond"])




def countdown(start=20, color="yellow", __pause=.4):
    if start > 20:
        raise ValueError("this cannot be > 10")

    for i in range(start, -1, -1):
        if i > 9:
            print("[  {}  ]".format(ConsoleColored(str(i), color, bold=1)))
        else:
            print("[   {}  ]".format(ConsoleColored(str(i), color, bold=1)))

        playsound(sounds_json[str(i)])
        sleep(__pause)


psaltirea_reminder_icon = Path("icons/psaltirea-png.png")

def PsaltireaReminder(total_time_seconds):
    for _seconds in range(total_time_seconds, -1, -1):
        time_left = seconds_to_time(_seconds)
        seconds = time_left.seconds

        try:
            minutes = time_left.minutes
            if minutes < 10:
                minutes = f"0{minutes}"

        except AttributeError:
            minutes = "00"

        try:
            hours = time_left.hours
            if hours < 10:
                hours = f"0{hours}"

        except AttributeError:
            hours = "00"


        if seconds < 10:
            seconds = f"0{seconds}"

        time_left = yellow_bold(f"{hours}:{minutes}:{seconds}")
        print(f"Time Left: [  {time_left}  ]", end="\r")
        sleep(1)

    print(f"\n\n{red_bold('PsaltireaReminder - ITS TIME')} !!! ( {get_current_time()} )\n")

    # warning before announcement
    for _ in range(3):
        warning_sound()
        comma_sound()

    bizwarn_sound()
    notification_sound()

    linux_notification(
        "PsaltireaReminder",
        "dont forget about Psaltirea Every Day!",
        psaltirea_reminder_icon.absolute().as_posix()
    )







# TODO: add key listener for reloading the 20 20 20 rule
# control + r should be the one


import platform

if __name__ == '__main__':
    os.system("clear")

    print("========== Psaltirea Reminder ==========\n")
    print(f"python3-script: {__file__}")
    print(f"script-folder: {os.getcwd()}\n")
    print(f"python3 --version: {platform.python_version()}\n\n")


    program_arguments = sys.argv
    print(f"Args: {program_arguments}")

    if len(program_arguments) >= 2:
        total_time_seconds = 0

        if "-s" in program_arguments:
            seconds_arg_position = program_arguments.index("-s")
            total_time_seconds += int(program_arguments[seconds_arg_position + 1])

        if "-m" in program_arguments:
            minutes_arg_position = program_arguments.index("-m")
            total_time_seconds += int(program_arguments[minutes_arg_position + 1]) * 60

        if "-h" in program_arguments:
            hours_arg_position = program_arguments.index("-h")
            total_time_seconds += int(program_arguments[hours_arg_position + 1]) * 3600

    else:
        total_time_seconds = 60 * 100


    print()
    while 1:
        try:
            PsaltireaReminder(total_time_seconds)
        except KeyboardInterrupt:
            print()
            break


        except Exception as err:
            print(err)
            break
