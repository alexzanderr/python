#!/usr/bin/python3

import sys
import os
from pathlib import Path
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from core.aesthetics import *



if __name__ == "__main__":
    args = sys.argv
    if len(args) > 2:
        print(args)

        if "-v" in args and "-start" in args and "-stop" in args:
            video_path_index = args.index("-v") + 1
            start_value_index = args.index("-start") + 1
            stop_value_index = args.index("-stop") + 1

            path = Path(args[video_path_index])
            start_value = int(args[start_value_index])
            stop_value = int(args[stop_value_index])

            video_name, extension = path.stem, path.suffix
            ffmpeg_extract_subclip(
                path,
                start_value,
                stop_value,
                targetname=(path.parent / f"{video_name}_cropped_{start_value}_{stop_value}{extension}").as_posix()
            )
            print_yellow_bold(f"video {video_name} cropped successfully")
            print_yellow_bold(f"from start({start_value}) -> stop({stop_value})")


    elif len(args) == 2:
        if args[1] == "--help":
            print("example usage:")
            print("\tpython3 crop-video.py -v Hristos_a_inviat.mkv -start 16 -stop 309\n")
            print("\t-v [video_file_path]")
            print("\t-start [start value in seconds]")
            print("\t-stop [stop value in seconds]")


    else:
        print("use --help")





    pass

