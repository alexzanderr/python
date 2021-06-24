
"""
core/download.py

useful for downloading
stuff from internet

author: @alexzander
"""


# python
import requests

# 3rd party
from tqdm import tqdm
from bs4 import BeautifulSoup # pip install bs4
from requests_html import HTMLSession # pip install requests_html

# core package ( pip install python-core )
from core.json__ import *
from core.drive import *


def download_file(
    url: str,
    destination: str,
    name=None,
    show_progress=False,
    open_destination=False,
    __print=False
):
    if not os.path.exists(destination):
        os.makedirs(destination)

    if not os.path.isdir(destination):
        raise NotADirectoryError(destination)

    response = requests.get(url, stream=True)
    if response.status_code != 200:
        response.raise_for_status()

    response.raw.decode_content = True

    # name plus extension
    file_name = os.path.basename(url)
    if name:
        # using custom file name
        file_path = os.path.join(destination, name + "." + file_name.split(".")[1])
    else:
        file_path = os.path.join(destination, file_name)

    if show_progress:
        # progess bar time

        chunk = 1024
        total = int(response.headers["content-length"])

        _bytes = response.iter_content(chunk_size=chunk)
        print(f"Downloading from: {blue(url)} ...")

        with open(file_path, "wb") as binary_file:
            for byte in tqdm(
                iterable=_bytes,
                total=total // chunk,
                unit="KB",
                desc=green(file_name),
                ncols=140,
                bar_format="{l_bar}%s{bar}%s{r_bar}" % (AnsiCodes.yellow, AnsiCodes.endc)
            ):
                binary_file.write(byte)

        print_yellow_bold("download complete.")
        print(f"at location: {file_path}")

    else:
        with open(file_path, "wb") as binary_file:
            binary_file.truncate(0)
            binary_file.write(response.raw.data)

        if __print:
            print(f"file: {file_name}")
            print(f"from url: {url}")
            print_green_bold("downloaded successfully")
            print(f"at location: {file_path}")

    if open_destination:
        open_folder(destination)

    return destination
