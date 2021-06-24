
"""
    core/sounds/system/system.py
    module that contains system sounds as .wav files
    in folder original

    if this file is run for the first time
    on your computer, it will autogenerate
    all the sound files -15 db (because they are loud by original)
    and they are placed in a folder called 'sounds'
    in your home dir on your os

    author: @alexzander
"""


# core package ( pip install python-core )
from core.json__ import *

# core/sounds
from core.sounds.play import play_commands
from core.sounds.initialize import check_remote_database


# checking and reading remote database
remote_sounds_json_path = check_remote_database("system")
remote_sounds_json = read_json_from_file(remote_sounds_json_path)


# =========== variety of system sounds ===============

def allahu_akbar():
    play_commands(remote_sounds_json, "allahu")


def windows98_error():
    play_commands(remote_sounds_json, "error")


def electric_pulse():
    play_commands(remote_sounds_json, "pulse")


def windows98_remix():
    play_commands(remote_sounds_json, "remix")


def shutdown_sound():
    play_commands(remote_sounds_json, "shutdown")


def welcome_back():
    play_commands(remote_sounds_json, "welcome")

# =========== variety of system sounds ===============


# TESTING
if __name__ == '__main__':
    windows98_error()
    welcome_back()