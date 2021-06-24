

from core.audio import playaudio


def play_commands(database_json, *commands):
    for arg in commands:
        playaudio(database_json[arg.lower()])