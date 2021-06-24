
import logging
import time

file_handler = logging.FileHandler("logs\\test1.log")
file_handler.setLevel(logging.INFO)

time.sleep(1)

import os

os.remove("logs\\test1.log")