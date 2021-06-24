
import imageio
imageio.plugins.ffmpeg.download()

# url for downloading the ffmpeg.exe file
# https://github.com/imageio/imageio-binaries/raw/master/ffmpeg/ffmpeg.win32.exe
# saved in
# C:\Users\${username}\AppData\Local\imageio\ffmpeg\ffmpeg.win32.exe

import cv2 as cv
import numpy as np
import pyautogui as gui
from core.__datetime import *
from time import sleep
import os
from core.aesthetics import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from pathlib import Path


screen_dim = (1920, 1080)

def RecordScreen(__iterations=100):
    fourcc = cv.VideoWriter_fourcc(*"XVID")
    output_name = "recording_{}.mkv".format(get_current_date())
    output_handler = cv.VideoWriter(output_name, fourcc, 20.0, (screen_dim))

    print("recording...")
    for _ in range(__iterations):
        screen_shot = gui.screenshot()
        frame = np.array(screen_shot)
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        output_handler.write(frame)
    print("done recording...")
    p = os.getcwd() + "/" + output_name
    print("located at: {}".format(underlined(p)))


def extract_video(_path: str, start, stop, destination):
    path = Path(_path)

    video_name, extension = path.name, path.suffix

    ffmpeg_extract_subclip(
        path,
        start,
        stop,
        targetname=(path / f"{video_name}_cutted{extension}").as_posix()
    )


if __name__ == '__main__':
    RecordScreen(100)