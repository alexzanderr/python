#!/usr/bin/python3

import sys
import os
import time
from pathlib import Path
from youtube_dl import YoutubeDL
from core.aesthetics import *


downloaded_video_folder = Path("downloads")


def YTDownloader(video_url):
    if not video_url.startswith("https://www.youtube.com/watch?v="):
        raise ValueError(f"url is not youtube video valid url: {video_url}")


    print(f"Video URL: [ {red_bold_underlined(video_url)} ]")

    video_id = video_url.split("watch?v=")[1]
    print(f"Video ID: {red_bold(video_id)}")


    print_yellow_bold("\ndownloading...\n")

    # with YoutubeDL({}) as downloader:
    #     downloader.download([video_url])


    downloaded_video_path = downloaded_video_folder / f"{video_id}_video.%(ext)s"

    downloader = YoutubeDL({"outtmpl": downloaded_video_path.absolute().as_posix()})

    with downloader:
        json_data = downloader.extract_info(
            video_url,
            download=True # can be False
        )
        # write_json_to_file(json_data, json_data_path)


    print("\nVideo downloaded saved here:")
    print_green_bold_underlined(downloaded_video_path)
    #
    # print("Video JSON Data saved here:")
    # print(json_data_path)


if __name__ == '__main__':
    program_arguments = sys.argv

    if len(program_arguments) == 2:
        video_url = program_arguments[1]
        if isinstance(video_url, str):
            choice = input(f"\npress <enter> to start download\n>>> ")
            if choice == "" or choice == "y":
                YTDownloader(video_url)
            else:
                print("aborted.")

        elif isinstance(video_url, list):
            choice = input(f"\npress <enter> to start download\n>>> ")
            for video in video_url:
                YTDownloader(video)
                time.sleep(0.2)
        else:
            print("ERROR: asd asd")

