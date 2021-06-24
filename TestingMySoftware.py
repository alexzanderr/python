import math
import os
import sys
from colored_traceback.colored_traceback import Colorizer
import traceback
from core.system import colorize_error
from core.aesthetics import *

colorize_error()


def function():
    x = 3
    raise ValueError("hello my friend. from function")


def another():
    function()


def another1():
    another()


def another2():
    another1()


traceback__ = \
r"""Traceback (most recent call last):
  File ".\TestingMySoftware.py", line 18, in <module>
    another()
  File ".\TestingMySoftware.py", line 15, in another
    function()
  File ".\TestingMySoftware.py", line 12, in function
    raise ValueError("hello my friend. from function")
ValueError: hello my friend. from function
"""
# print(yellow_bold(traceback__))

# try:
#     another2()
# except ValueError as err:
#     # one method to print the traceback, but its not colored
#     print('hello')

#     exc_type, exc_value, exc_traceback = sys.exc_info()
#     c = Colorizer("dark")
#     c.colorize_traceback(exc_type, exc_value, exc_traceback)
#     # traceback.print_exc(file=sys.stdout)
#     print('hello')

    # print("~" * 100)

    # traceback_lines = traceback.format_exc().splitlines()

    # first_line = traceback_lines[0].replace("Traceback", red("Traceback"))
    # first_line = first_line.replace("(", yellow("(")).replace(")", yellow(
    # ")"))

    # index = traceback_lines[-1].find(":") + 2
    # exc_message = traceback_lines[-1][index: ]
    # exc_type = traceback_lines[-1][ :index - 2]
    # last_line = traceback_lines[-1].replace(exc_type, red(exc_type))
    # last_line = last_line.replace(exc_message, white_yellow(exc_message))

    # # modifying the frames
    # frames = traceback.extract_tb(exc_traceback)
    # for i, frame in enumerate(frames):

    #     filename = str(frame.filename)
    #     if not os.path.isabs(filename):
    #         if os.path.sep in filename:
    #             index = filename.find(os.path.sep)
    #             filename = filename[:index] + filename[index + 1:]

    #         if "." in filename:
    #             index = filename.find(".")
    #             filename = filename[:index] + filename[index + 1:]

    #         frames[i].filename = os.path.join(os.getcwd(), filename)

    # traceback_lines_colored = [first_line]
    # for frame in frames:
    #     traceback_lines_colored.append(
    #         f'  File: "{AnsiCodes.lime_green + frame.filename +
    #         AnsiCodes.endc}{yellow_bold(":")}{blue_bold(frame.lineno)}"
    #         Line: {frame.lineno} in {frame.name}\n\t{frame.line}'
    #     )
    #     # break
    # traceback_lines_colored.append(last_line)

    # for line in traceback_lines_colored:
    #     print(line)

    # to_format_list = []
    # for frame in frames:
    #     to_format_list.append((
    #         AnsiCodes.lime_green + frame.filename + endc_effect,
    #         frame.lineno,
    #         frame.name,
    #         AnsiCodes.cyan + frame.line + endc_effect
    #     ))
    # to_format_list.append(error_lines[-1])

    # print("~" * 56)
    # colored_traceback = traceback.format_list(to_format_list)
    # for line in colored_traceback:
    #     print(line, end="")
    # print(colored_traceback)














import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()