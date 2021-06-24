
"""
    core/__datetime.py

    wrapped around selenium

    author: @alexzader
"""


# 3rd party
from selenium import webdriver # pip install selenium

# core package ( pip install python-core )
from core.system import *


def init_chrome_driver(
    chrdv_path="C:/Applications__/chrome_driver/88/chromedriver.exe",
    user_agent=None,
    icognito=True
):
    options = webdriver.ChromeOptions()

    # only on windows
    __os = get_operating_system()
    if __os == "Windows":
        options.binary_location = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
    elif __os == "Linux":
        options.binary_location = "/usr/bin/firefox/firefox-bin"
    elif __os == "Darwin":
        options.binary_location = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"

    if user_agent is not None:
        options.add_argument(f"user-agent={user_agent}")

    if icognito:
        options.add_argument("--incognito")

    driver = webdriver.Chrome(
        executable_path=chrdv_path,
        options=options
    )
    return driver