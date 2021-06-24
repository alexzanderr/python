
# python
import os
import sys
import logging
import subprocess
from string import Template

# core
from core.datetime__ import *
from core.json__ import *
from core.path__ import *
from core.drive import *
from core.system import *
import core.exceptions

colorize_error()

logs_folder = "py2exe_build_logs"
if not os.path.exists(logs_folder):
    os.makedirs(logs_folder)

logs_folder_items = os.listdir(logs_folder)
if len(logs_folder_items) > 10:
    delete_folder_contents(logs_folder)
del logs_folder_items

# formatter
formatter_Python2Executable = logging.Formatter(
    "[ %(asctime)s.%(msecs)04d - %(name)s - %(levelname)s ]\n%(message)s\n",
    datefmt="%d.%m.%Y-%H:%M:%S"
)

# stream handler
stream_handler_Python2Executable = logging.StreamHandler(sys.stdout)
stream_handler_Python2Executable.setLevel(logging.INFO)
stream_handler_Python2Executable.setFormatter(formatter_Python2Executable)

# datetime


# file handler
current_datetime = get_current_datetime(__format="%d.%m.%Y__%H_%M_%S")
log_file_name = os.path.join(logs_folder, f"py2exe_{current_datetime}.log")

file_handler_Python2Executable = logging.FileHandler(log_file_name)
file_handler_Python2Executable.setLevel(logging.INFO)
file_handler_Python2Executable.setFormatter(formatter_Python2Executable)

del log_file_name, current_datetime