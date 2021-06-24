
# python
import re
import logging
from getpass import getuser
from random import choice
from string import Template

# core
from core.system import *
from core.path__ import *
from core.json__ import *
from core.drive import *
from core.logging__ import *

# project
from PyPIAutoUpload.paths import *

colorize_error()

operating_system = get_operating_system()


logs_folder = "upload_logs"
if not os.path.exists(logs_folder):
    os.makedirs(logs_folder)

logs_folder_items = os.listdir(logs_folder)
if len(logs_folder_items) > 10:
    delete_folder_contents(logs_folder, __print=True)
del logs_folder_items


stream_handler_PyPIAutoUpload = get_stream_handler()
file_handler_PyPIAutoUpload = get_file_handler_with_datetime(
    logs_folder,
    "upload"
)