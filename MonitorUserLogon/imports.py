
# python
import os
import sys
import time
import json
from random import choice
from string import Template
from getpass import getuser
from pathlib import Path
from datetime import datetime
import subprocess

# core
from core import json__
from core import aesthetics
from core import system
from core import logging__
from core import drive
from core import path__
from core import numbers__
from core import datetime__

# pypi
from pynput import mouse
from pynput import keyboard
import matplotlib.pyplot as plt
plt.style.use('Solarize_Light2')
plt.rcParams.update({'font.size': 16})


# prerequisities
system.colorize_error()
operating_system = system.get_operating_system()


logs_folder = Path("logs")

stream_handler_MonitorUserLogon = logging__.get_stream_handler()
file_handler_MonitorUserLogon = logging__.get_file_handler_with_datetime(
    logs_folder.as_posix(),
    "log"
)
