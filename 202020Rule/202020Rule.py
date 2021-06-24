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


endc_effect = "\033[0m"
bold_effect = "\033[1m"
underlined_effect = "\033[4m"
reversed_effect = "\u001b[7m"
ansi_codes = {
    'purple': '\033[95m',
    'blue': '\033[94m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'endc': '\033[0m',
    'bold': '\033[1m',
    'underlined': '\033[4m',
    'white': "\u001b[37;1m",
    "cyan": '\x1b[38;5;44m',
    "darkcyan": '\033[36m',
    "magenta": "\033[35m",
    "black": "\033[30m",
    "grey": "\x1b[38;5;246m",
    "orange": "\x1b[38;5;208m"
}

def ConsoleColored(string, color, bold=0, underlined=0):
    if type(string) != str:
        string = str(string)


    # incorrect color
    if color not in ansi_codes and color != 'random':
        raise

    # bold == 0 and underlined == 0
    if not bold and not underlined:
        if color == "random":
            from random import choice
            return ansi_codes[choice(list(ansi_codes.keys()))] + string + endc_effect

        return ansi_codes[color] + string + endc_effect

    # bold == 0 and underlined == 1
    elif not bold and underlined:
        if color == "random":
            from random import choice
            return ansi_codes[choice(list(ansi_codes.keys()))] + \
                ansi_codes["underlined"] + string + endc_effect

        return ansi_codes[color] + ansi_codes["underlined"] + string + endc_effect

    # bold == 1 and underlined == 0
    elif bold and not underlined:
        if color == "random":
            from random import choice
            return ansi_codes[choice(list(ansi_codes.keys()))] + \
                ansi_codes["bold"] + string + endc_effect

        return ansi_codes[color] + ansi_codes["bold"] + string + endc_effect

    # bold == 1 and underlined == 1
    if color == "random":
        from random import choice
        return ansi_codes[choice(list(ansi_codes.keys()))] + \
            ansi_codes["bold"] + ansi_codes["underlined"] + string + endc_effect

    return ansi_codes[color] + ansi_codes["bold"] + ansi_codes["underlined"] + string + endc_effect

def yellow_bold(__string):
    return ConsoleColored(__string, "yellow", bold=1)


def red_bold(__string):
    return ConsoleColored(__string, "red", bold=1)



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

# pip3 install playsound
# or
# python3.7 -m pip install playsound

# python
import os
import sys
from pathlib import Path


from string import Template

notify_send_template = Template(
    "notify-send '${title}' '${message}'"
    " --icon=${icon_path}"
)

notify_send_without_icon_template = Template(
    "notify-send '${title}' '${message}"
)



# notify-send '202020Rule' 'ITS TIME NOW !!!' --icon=/home/alexzander/Alexzander__/programming/python/202020_order/assets/icons/202020-order-icon.png

def linux_notification(title, message, icon_path=None):
    if icon_path:
        subprocess.call(notify_send_template.safe_substitute(
            title=title,
            message=message,
            icon_path=icon_path
        ), shell=True)
    else:
        subprocess.call(notify_send_without_icon_template.safe_substitute(
            title=title,
            message=message,
        ), shell=True)


__appname__ = "202020Rule"

assets_folder = Path("assets")

sounds_json = read_json_from_file(assets_folder / "sounds" / "sounds.json")

rule_202020_icon_file = assets_folder / "icons" / "202020-order-icon.png"



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

def number_sound(number):
    playsound(sounds_json[number])

def order_sound():
    playsound(sounds_json["order"])

def rule_202020_sound():
    number_sound("20")
    number_sound("20")
    number_sound("20")
    order_sound()




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


def Rule202020(total_time_seconds):
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

    print(f"\n\n{red_bold('20 20 20 ORDER')} !!! ( {get_current_time()} )")

    # warning before announcement
    for _ in range(3):
        warning_sound()
        comma_sound()
    bizwarn_sound()

    rule_202020_sound()

    linux_notification(
        "20 20 20 ORDER",
        "ITS TIME NOW!!",
        rule_202020_icon_file.absolute().as_posix()
    )
    print(f"notification sent at {get_current_datetime()}")

    countdown(20, "red", 1)
    print("\n")




# TODO: add key listener for reloading the 20 20 20 rule
# control + r should be the one


import platform

if __name__ == '__main__':
    os.system("clear")

    print("========== 202020 Rule ==========\n")
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
        total_time_seconds = 18 * 60


    print()
    while 1:
        try:
            Rule202020(total_time_seconds)
        except KeyboardInterrupt:
            print()
            break


        except BaseException as err:
            print(err)
            break
