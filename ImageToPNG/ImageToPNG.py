
from core.system import *
from PIL import Image
from core.aesthetics import *
from core.path__ import *
from core.winapi__ import windows_notification
from core.exceptions import *
from time import sleep

def convert(source_path: str, destination_foler: str=""):
    sep = get_path_sep(source_path)
    if destination_foler == "":
        destination_foler = sep.join(source_path.split(sep)[:-1])

    filename = get_file_name(source_path)
    png_to_same_location = destination_foler + sep + filename + ".png"

    img = Image.open(source_path)
    img.save(png_to_same_location)
    return destination_foler

def notification():
    windows_notification(
        "ImageToPNG",
        "converted successfully!\nplaced in original folder",
        5,
        "icons/suc.ico",
        1
    )

def intro(message: str):
    print_red_bold(message)
    print_yellow_bold("[{}]\n\n".format("=" * 50))

__appname__ = "ImageToPNG"

def ImageToPNG():
    while 1:
        clearscreen()
        print(green_bold(__appname__))
        print(green_bold("=" * len(__appname__)))

        image_path = input(f"\n[enter the path of image] or [drag and drop the image]:\n{left_arrow_3_green_bold} ")
        if image_path == "":
            continue

        if not is_file(image_path):
            continue

        ext = get_file_extension(image_path).lower()
        if ext == "png":
            print_blue_bold("file is already PNG.")
            sleep(2)
            continue

        if ext not in "jpg_ico_jpeg":
            continue

        choice = input("\nare you sure about this converstion? [y or <enter> /n]:\n")
        if choice == "y" or choice == "":
            dest_folder = convert(image_path)
            print_green("\ndestination folder opened!\n")
            os.system("explorer {}".format(dest_folder))
            notification()

if __name__ == '__main__':
    ImageToPNG()