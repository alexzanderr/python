

import os
import subprocess as s
from PIL import Image
from core.drive import *
from core.path__ import *
from core.system import *
from core.aesthetics import *
from core.development import *
from core.winapi__ import windows_notification
from core.linuxapi import linux_notification


linux = get_operating_system() == "linux"


sizes_values = [
    (255, 255),
    (128, 128),
    (64, 64),
    (48, 48),
    (32, 32),
    (24, 24),
    (16, 16)
]


def ConvertImage(image_path, size=None):
    img = Image.open(image_path)
    w, h = img.size
    print("Original image size: ({}, {})".format(w, h))

    if size:
        selected_size = size
    else:
        # selecting size
        selected_size = None
        index = 0
        while True:
            __w, __h = sizes_values[index]
            if w >= __w and h >= __h:
                selected_size = (__w, __h)
                break
            else:
                index += 1
                if index == len(sizes_values) - 1:
                    selected_size = sizes_values[-1]
                    break

    print("Selected size for conversion: ({}, {})".format(*selected_size))


    if isinstance(image_path, Path):
        img.save(
            f"{image_path.parent}/{image_path.name}_{selected_size[0]}x{selected_size[1]}_converted.ico"
        )
        return image_path.parent

    elif isinstance(image_path,  str):
        destination = "/".join(image_path.split("/")[:-1])
        img.save(
            f"{destination}/{image_path.split('/')[-1]}_{selected_size[0]}x{selected_size[1]}_converted.ico"
        )
        return destination






def ImageToICO():
    while 1:
        clearscreen()
        IntroductionMessage("ImageToICO")

        image_path = input("[enter the path of your image] OR [DRAG AND DROP the image]:\n{} ".format(left_arrow_3_green_bold))

        # is not a file
        if not is_file(image_path):
            continue

        # being an ico is not valid
        ext = get_file_extension(image_path).lower()
        if ext == "ico":
            continue

        # is not an image
        if ext.lower() not in "jpg_jpeg_png":
            continue


        print("\nImage from path: {}".format(yellow_bold(image_path)))
        destination_folder = ConvertImage(image_path)

        os.system(f"nautilus {destination_folder} &")
        print_green_bold("folder opened!")

        # windows success notification
        if linux:
            linux_notification(
                "ImageToICO",
                "converted successfully!",
                "icons/1.ico"
            )
        else:
            windows_notification(
                "ImageToICO",
                "converted successfully!\n\nplaced in original folder",
                2,
                "icons/1.ico",
                1
            )

        print()
        pauseprogram()


if __name__ == '__main__':
    ImageToICO()