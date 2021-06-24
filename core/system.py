
"""
    system.py

    useful module in accesing and using system stuff

    author: @alexzander
"""

# python
import os
import sys
import platform

# core package ( pip install python-core )
import core.exceptions
import core.aesthetics


def get_operating_system():
    return platform.system().lower()


def get_python_path():
    """ return folder path """
    if os.environ["PYTHONPATH"].endswith(";"):
        return os.environ["PYTHONPATH"][:-1]
    return os.environ["PYTHONPATH"]


def get_computer_name():
    return platform.node()


def get_tesseract_path():
    """ return executable of tesseract engine (if installed) """
    if "TESS" not in os.environ.keys():
        raise core.exceptions.NotFoundError("TESS is not environment variables")
    return os.environ["TESS"]


def colorize_error():
    import colored_traceback  # pip install colored_traceback
    colored_traceback.add_hook(always=True)


def clearscreen():
    """ clears the shell screen depending on the opearting system """
    o = get_operating_system()
    if o == "windows":
        os.system("cls")
    else:
        os.system("clear")


def pauseprogram(
        message=f"[ press {core.aesthetics.green_bold('<enter>')} to continue... ]\n"):
    input(message)


def get_arhitecture():
    return platform.architecture()[0]


def get_python_version():
    return platform.python_version()


def get_python_implementation():
    return platform.python_implementation()


def get_processor():
    return platform.processor()


def get_python_interpreter_path():
    return sys.executable



# TESTING
if __name__ == '__main__':
    o = get_operating_system()
    print(o)
