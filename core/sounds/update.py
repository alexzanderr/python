

# python
import os

# core package ( pip install python-core )
from core.drive import *
from core.json__ import *
from core.path__ import *
from core.audio import modify_volume


def UpdateSounds(original_remote_folder: str,
                 modified_remote_folder: str,
                 remote_sounds_json_path: str):
    """
        modifies every original sound with -15 dB and
            puts all the files into modified folder.

        if modified folder has items inside, will be
            deleted and replaced with brand new ones.
    """
    # verifying if is empty
    __items = os.listdir(modified_remote_folder)
    if __items != []:
        delete_folder(modified_remote_folder)
        # for file in __items:
        #     os.remove(modified_remote_folder + "/" + file)

    # saving all paths from original folder
    files = [
        original_remote_folder + "/" + file for file in os.listdir(original_remote_folder) if is_file((original_remote_folder + "/" + file))
    ]

    # -15 dB for every file in the original folder
    # -15 dB is the best volume you can get
    for f in files:
        modify_volume(f, modified_remote_folder, units=-15)

    # creating a json with paths for every modified sound
    sounds_modified_json = {}
    for file in os.listdir(modified_remote_folder):
        name = file.split("_")[0]
        sounds_modified_json[name] = modified_remote_folder + "/" + file

    # writing sounds json to disk in the remote location
    # creating sounds.json under:
    # C:/Users/$username/sounds/$type (windows)
    # or
    # /home/$username/sounds/$type (linux)
    # or
    # /Users/$username/sounds/$type (mac)
    write_json_to_file(sounds_modified_json, remote_sounds_json_path)