

import os
from string import Template
from core.path__ import *


function_template = """
def {filename}_sound():
    play_commands(remote_sounds_json, "{filename}")

"""

def AutoGenerate(py_file: str, database_folder: dict):
    """
        inserts python functions into specified python file
        separated by 2 empty lines
    """
    if not is_file(py_file):
        raise NotAFileError
    if not py_file.endswith(".py") and not py_file.endswith(".pyw"):
        raise IncorrectExtensionError

    with open(py_file, "a+", encoding="utf-8") as f:

        for audio_file in os.listdir(database_folder):
            filename = audio_file.split(".")[0] # get rid of extension
            if "-" in filename:
                filename = filename.replace("-", "_")
            f.write(function_template.format(filename=filename))