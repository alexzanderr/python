
from string import Template




# 1
imports_py_template = Template("""
# python
import os
import sys
from random import choice
from string import Template
from getpass import getuser
from pathlib import Path

# core
from core import json__
from core import aesthetics
from core import system
from core import logging__
from core import drive
from core import path__

# prerequisities
system.colorize_error()
operating_system = system.get_operating_system()


logs_folder = Path("logs")

stream_handler_${project_name} = logging__.get_stream_handler()
file_handler_${project_name} = logging__.get_file_handler_with_datetime(
    logs_folder.as_posix(),
    "log"
)
""")




# 2
main_py_template = Template(r"""
from ${project_name}.imports import *


__appname__ = "${project_name}"


logger_${project_name} = logging__.Loggerr(
    name="_${project_name}.py",
    file_handler=file_handler_${project_name},
    stream_handler=stream_handler_${project_name}
)
logger_${project_name}.info(f"application {__appname__} loaded.")



def print_title():
    print(__appname__)
    print("=" * len(__appname__))


def exited_from_interrupt():
    print("\n")
    logger_${project_name}.info(f"{aesthetics.yellow_bold(__appname__)}\napplication {aesthetics.red_bold('closed')} from [ {aesthetics.red_bold(KeyboardInterrupt.__name__)} ]")


prompt_message = f"\nenter something:\n>>> "

def ${project_name}():
    # main function of entire project
    print("the entire project its functioning properly!")

    while True:
        try:
            system.clearscreen()
            print_title()

            choice = input(prompt_message)
            try:
                choice = int(choice)
            except ValueError:
                if choice == "":
                    continue
            else:
                print("do something with choice")
                # INSERT CODE HERE

            # INSERT CODE HERE

        except KeyboardInterrupt:
            exited_from_interrupt()
            break

        except Exception as exception:
            logger_${project_name}.info(aesthetics.red_bold(exception) + "\n" + aesthetics.yellow_bold(type(exception)))
            logger_${project_name}.exception(f"error in {logger_${project_name}.name}")

            try:
                system.pauseprogram(f"{aesthetics.red_bold('error')} occured in function {${project_name}.__name__}() [{aesthetics.yellow_bold('program paused')}]\n")

            except KeyboardInterrupt:
                exited_from_interrupt()
                break


# TESTING PROJECT
if __name__ == "__main__":
    ${project_name}() # calling main function of entire project
""")




# 3
TestingProject_py_template = Template("""
from ${project_name}.imports import *


""")




# 4
__init__py_template = \
"""
# nothing here, yet"
"""