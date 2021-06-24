
"""
    core/sounds/cs16/cs16.py

    module that contains cs 1.6
    multiplayer sounds as .wav files
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
remote_sounds_json_path = check_remote_database("cs16")
remote_sounds_json = read_json_from_file(remote_sounds_json_path)


# =========== variety of cs16 sounds ===============

def arcade_sound():
    play_commands(remote_sounds_json, "arcade")


def break_sound():
    play_commands(remote_sounds_json, "break")


def davai_sound():
    play_commands(remote_sounds_json, "davai")


def dominating_sound():
    play_commands(remote_sounds_json, "dominating")


def doublekill_sound():
    play_commands(remote_sounds_json, "doublekill")


def eagleeye_sound():
    play_commands(remote_sounds_json, "eagleeye")


def excellent_sound():
    play_commands(remote_sounds_json, "excellent")


def explosion_sound():
    play_commands(remote_sounds_json, "explosion")


def firstblood_sound():
    play_commands(remote_sounds_json, "firstblood")


def flawless_sound():
    play_commands(remote_sounds_json, "flawless")


def godlike_sound():
    play_commands(remote_sounds_json, "godlike")


def hattrick_sound():
    play_commands(remote_sounds_json, "hattrick")


def headhunter_sound():
    play_commands(remote_sounds_json, "headhunter")


def headshot_sound():
    play_commands(remote_sounds_json, "headshot")


def here_comes_the_money_sound():
    play_commands(remote_sounds_json, "here_comes_the_money")


def holyshit_sound():
    play_commands(remote_sounds_json, "holyshit")


def humiliating_defeat_sound():
    play_commands(remote_sounds_json, "humiliating_defeat")


def humiliating_sound():
    play_commands(remote_sounds_json, "humiliating")


def humiliation_sound():
    play_commands(remote_sounds_json, "humiliation")


def killingmachine_sound():
    play_commands(remote_sounds_json, "killingmachine")


def killingspree_sound():
    play_commands(remote_sounds_json, "killingspree")


def ludicrouskill_sound():
    play_commands(remote_sounds_json, "ludicrouskill")


def massacre_sound():
    play_commands(remote_sounds_json, "massacre")


def megakill_sound():
    play_commands(remote_sounds_json, "megakill")


def monsterkill_sound():
    play_commands(remote_sounds_json, "monsterkill")


def moonlight_sound():
    play_commands(remote_sounds_json, "moonlight")


def multikill_sound():
    play_commands(remote_sounds_json, "multikill")


def ownage_sound():
    play_commands(remote_sounds_json, "ownage")


def payback_sound():
    play_commands(remote_sounds_json, "payback")


def pick_up_your_weapons_and_fight_sound():
    play_commands(remote_sounds_json, "pick_up_your_weapons_and_fight")


def play_sound():
    play_commands(remote_sounds_json, "play")


def prepare_for_battle_sound():
    play_commands(remote_sounds_json, "prepare_for_battle")


def prepare_to_fight_sound():
    play_commands(remote_sounds_json, "prepare_to_fight")


def rampage_sound():
    play_commands(remote_sounds_json, "rampage")


def respect_sound():
    play_commands(remote_sounds_json, "respect")


def retribution_sound():
    play_commands(remote_sounds_json, "retribution")


def suka_sound():
    play_commands(remote_sounds_json, "suka")


def suprise_motafaca_sound():
    play_commands(remote_sounds_json, "suprise_motafaca")


def triplekill_sound():
    play_commands(remote_sounds_json, "triplekill")


def ultrakill_sound():
    play_commands(remote_sounds_json, "ultrakill")


def unstoppable_loud_sound():
    play_commands(remote_sounds_json, "unstoppable_loud")


def unstoppable_sound():
    play_commands(remote_sounds_json, "unstoppable")


def where_the_hood_at_sound():
    play_commands(remote_sounds_json, "where_the_hood_at")


def whickedsick_sound():
    play_commands(remote_sounds_json, "whickedsick")

# =========== /variety of cs16 sounds ===============


# TESTING
if __name__ == '__main__':
    doublekill_sound()
    triplekill_sound()