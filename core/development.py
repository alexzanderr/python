
"""
    core/development.py

    useful module in development
    of executable python3 applications

    author: @alexzander
"""


# core package ( pip install python-core )
from core.aesthetics import *


def IntroductionMessage(message: str):
    if message == "":
        raise ValueError

    message = "\n" + message
    print_red_bold(message)
    print_yellow_bold("{}\n".format("=" * (len(message) - 1)))