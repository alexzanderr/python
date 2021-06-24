
"""
    FaceCamLog/_FaceCamLog.py

    main project file
"""


# python
import os
import sys
import warnings
import subprocess
from time import sleep
from pathlib import Path
from random import choice
from string import Template
from getpass import getuser


# pypi
import cv2
from PIL import ImageFont
from numba.core.errors import (
    NumbaDeprecationWarning,
    NumbaWarning,
    NumbaPendingDeprecationWarning
)
warnings.simplefilter('ignore', category=NumbaWarning)
warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)

from pynput.keyboard import Listener as KeyboardListener
from pynput.keyboard import Key


# core
from core import json__
from core.aesthetics import *
from core import system
from core import logging__
from core import drive
from core import path__
from core.random__ import *
from core.datetime__ import *
from core.winapi__ import windows_notification
from core.linuxapi import linux_notification


# current project
from VideoRecorder import VideoRecorder, DrawTextOnFrame
from AudioRecorder import AudioRecorder


# prerequisities
system.colorize_error()


__appname__ = "CaptainsLog"
operating_system = system.get_operating_system()
linux = operating_system == "linux"


project_logs_folder = Path("logs")
# stream handler
stream_handler_FaceCamLog = logging__.get_stream_handler()
# file handler
file_handler_FaceCamLog = logging__.get_file_handler_with_datetime(
    project_logs_folder.as_posix(),
    "log"
)
# logger
logger_CaptainsLogger = logging__.Loggerr(
    name="_FaceCamLog.py",
    file_handler=file_handler_FaceCamLog,
    stream_handler=stream_handler_FaceCamLog
)
logger_CaptainsLogger.info(f"application {__appname__} loaded.")


def generate_video_id(length=5):
    return random_upper_str(length)


def merge_audio_video(audio, video, destination):
    """
        ffmpeg -hide_banner -loglevel error -y -i video_logs/log_3.mp4 -i audio_logs/log_3.wav -vcodec copy facecam_logs/test.mp4

        -hine_banner - no output on screenm
        -loglevel error - is printing on screen only if error
        -y - no confirmation
        -i - input file
    """

    subprocess.call(f"ffmpeg -hide_banner -loglevel error -y -i {video} -i {audio} -vcodec copy {destination}", shell=True)
    logger_CaptainsLogger.info(f"{audio} and {video} merged at {destination}")


def print_title():
    print(__appname__)
    print("=" * len(__appname__))


def exited_from_interrupt():
    print("\n")
    logger_CaptainsLogger.info(f"{aesthetics.yellow_bold(__appname__)}\napplication {aesthetics.red_bold('closed')} from [ {aesthetics.red_bold(KeyboardInterrupt.__name__)} ]")




def KeyPress(key):
    if key == Key.esc:
        print("key listener stopped with ESC")
        return False


def await_user_force_stop_the_recording():
    print_red_bold("look at the camera, pls.\nstop recording with [ CTRL+C ] or [ ESC ]\n")
    try:
        with KeyboardListener(on_press=KeyPress) as keyboard_listener:
            keyboard_listener.join()

    except KeyboardInterrupt:
        pass




video_id = generate_video_id(5)
logger_CaptainsLogger.info("video id generated")

username = "alexzander"
logger_CaptainsLogger.info(f"username is {username}")

captain_logs_folder = Path("captain_logs")
captain_logs_folder.mkdir(exist_ok=True)
logger_CaptainsLogger.info(f"folder:\n{captain_logs_folder.as_posix()} created")


# remote app data
remote_project = "/home/alexzander/Alexzander__/PythonApplicationsAppData/CaptainsLog"

remote_location_path = "/home/alexzander/Alexzander__/PythonApplicationsAppData/CaptainsLog/captain_logs"
remote_captain_logs_folder = Path(remote_location_path)
remote_captain_logs_folder.mkdir(exist_ok=True)
logger_CaptainsLogger.info(f"folder:\n{remote_captain_logs_folder.as_posix()} created")

current_date = get_current_date()

current_date_captain_logs_folder = captain_logs_folder / current_date
current_date_captain_logs_folder.mkdir(exist_ok=True)
logger_CaptainsLogger.info(f"folder:\n{current_date_captain_logs_folder.as_posix()} created")


# remote current date
remote_current_date_captain_logs_folder = remote_captain_logs_folder / current_date
remote_current_date_captain_logs_folder.mkdir(exist_ok=True)

logger_CaptainsLogger.info(f"folder:\n{current_date_captain_logs_folder.as_posix()} created")


video_number = len(list(current_date_captain_logs_folder.glob("*"))) + 1
logger_CaptainsLogger.info(f"current video number: {video_number}")

remote_video_number = len(list(remote_current_date_captain_logs_folder.glob("*"))) + 1
logger_CaptainsLogger.info(f"current remote video number: {video_number}")


captains_logs_filename = f"captains_log_{video_number}_{video_id}.mkv"

captains_log_file = current_date_captain_logs_folder / captains_logs_filename
logger_CaptainsLogger.info(f"this captains log file: {captains_log_file.as_posix()}")

remote_captains_log_file = remote_current_date_captain_logs_folder / captains_logs_filename
logger_CaptainsLogger.info(f"this remote captains log file: {remote_captains_log_file.as_posix()}")


stop_all = [False]
video_stop_flag = [False]
audio_stop_flag = [False]



# destinations and temp folder
temp_folder = Path("temp")
temp_folder.mkdir(exist_ok=True)
logger_CaptainsLogger.info(f"created {temp_folder.as_posix()} folder")


# remote destinations and remote temp folder
remote_temp_folder = Path(remote_project + "\\temp")
remote_temp_folder.mkdir(exist_ok=True)
logger_CaptainsLogger.info(f"created {remote_temp_folder.as_posix()} folder")


# temp video name
video_log_destination = temp_folder / "video.mkv"
# temp audio name
audio_log_destination = temp_folder / "audio.wav"

# remote video name
remote_video_log_destination = remote_temp_folder / "video.mkv"
# remote audio name
remote_audio_log_destination = remote_temp_folder / "audio.wav"


# loading monaco font
font_size = 20
monaco_font_file = Path("assets/fonts/monaco.ttf")
monaco_font = ImageFont.truetype(monaco_font_file.as_posix(), font_size)
logger_CaptainsLogger.info(f"monaco font loaded from: {monaco_font_file.as_posix()}")


# text putted on live camera color
color = (255, 255, 0) # yellow

# starting coordinates because we use multiple lines
text_y = 5
text_x = 20



def CaptainsLog():
    """
        main function where all happiness and fun happens
    """
    # init video recorder object (takes some time)
    logger_CaptainsLogger.info("loading video recorder...")
    video_recorder = VideoRecorder(
        video_log_destination,
        remote_video_log_destination,
        video_stop_flag,
        video_number,video_id,
        username,
        monaco_font,
        color,
        text_x,
        text_y,
        stop_all,
        show_live=False
    )


    # init audio recorder object (takes less time)
    logger_CaptainsLogger.info("loading audio recorder...")
    audio_recorder = AudioRecorder(
        audio_log_destination,
        remote_audio_log_destination,
        audio_stop_flag,
        stop_all
    )


    # run for the first time
    # with JIT will be compiled to machine code
    # this function needs to be made binary, otherwise the rendering is laggy
    # when we save the video
    logger_CaptainsLogger.info("compiling to machine code DrawTextOnFrame()")
    # just calling the function with dummmy parameters
    DrawTextOnFrame(
        cv2.imread("assets/background.png"), 10, 20, 50, 3,
        video_number, username, get_current_datetime(), video_id, monaco_font, color
    )


    # start
    logger_CaptainsLogger.info("\nrecording audio and video in background...\n")
    audio_recorder.start_thread()
    video_recorder.start_thread()



    # wait for user to force stop the video and audio recording
    await_user_force_stop_the_recording()


    # stop
    video_recorder.stop_video_thread()
    audio_recorder.stop_audio_thread()



    # waiting for classes to end (close, delete stuff from RAM, etc)
    logger_CaptainsLogger.info("awaiting to finish the video and audio classes")
    while (not audio_stop_flag[0] or not video_stop_flag[0]) and not stop_all[0]:
        sleep(.1) # sleeping until done


    # merge audio with video using ffmpeg software
    # and save here -> captains_log_file.as_posix() ofc
    logger_CaptainsLogger.info("merging audio with video...")
    merge_audio_video(
        audio_log_destination.as_posix(),
        video_log_destination.as_posix(),
        captains_log_file.as_posix()
    )


    # merge audio withj video suing ffmpeg sofware
    # and save to remote location
    # remote location: ~/Alexzander/PythonApplicationsAppData/CaptainsLog/...
    merge_audio_video(
        audio_log_destination.as_posix(),
        video_log_destination.as_posix(),
        remote_captains_log_file.as_posix()
    )


    # deleting local temp video and audio
    audio_log_destination.unlink()
    logger_CaptainsLogger.info(f"{audio_log_destination.as_posix()} deleted.")
    video_log_destination.unlink()
    logger_CaptainsLogger.info(f"{video_log_destination.as_posix()} deleted.")


    # update total logs number
    total_logs_file = captain_logs_folder / "total_logs.txt"
    if not total_logs_file.exists():
        total_logs_file.write_text("0")

    total_videos = int(total_logs_file.read_text()) + 1
    total_logs_file.write_text(str(total_videos))
    logger_CaptainsLogger.info(f"{total_logs_file.as_posix()} updated with {total_videos}.")


    # opened current date folder
    # folder = os.path.realpath(remote_current_date_captain_logs_folder.absolute().as_posix())
    # os.system("xdg-open {}".format(folder))
    # logger_CaptainsLogger.info(f"opened {folder}")
    # del folder


    # /home/alexzander/Alexzander__/programming/python/CaptainsLog/captain_logs/15.05.2021/captains_log_9_SIRDZ.mkv


    result_video_path = f"parole {captains_log_file.absolute().as_posix()} -i"
    print_red_bold(result_video_path)
    os.system(result_video_path)




if __name__ == "__main__":
    CaptainsLog()