

import warnings
import zipfile as z
import os
from tqdm import tqdm as progress_bar
from ExtractFiles import ExtractFiles
from MainContents import GetMainContents
from pathlib import Path
from core.datetime__ import *
from core.drive import *

warnings.simplefilter('ignore', category=UserWarning)

zipped_contents_folder_path = "zipped"
zipped_contents_folder = Path(zipped_contents_folder_path)
zipped_contents_folder.mkdir(exist_ok=1)


def CompressFiles(files, name, zip_extension="tar.gz", overwrite=False):
    zipped_file = zipped_contents_folder / get_current_date() / f"{name}.{zip_extension}"
    if zipped_file.exists():
        if overwrite:
            os.remove(zipped_file.absolute().as_posix()) # nu sterge, unfortunatelly
        else:
            return zipped_file
    else:
        if not zipped_file.parent.exists():
            zipped_file.parent.mkdir(exist_ok=1)

    zip_file_client = z.ZipFile(zipped_file.as_posix(), "w", z.ZIP_DEFLATED)

    print("\nUserWarnings for duplicate files in zip are supressed.\ncompressing ...")
    compress_progress = progress_bar(
        iterable=files,
        desc="compress",
        total=len(files),
        unit="file",
        ncols=120
    )
    for file in files:
        compress_progress.update(1)
        if file in zip_file_client.namelist():
            print(f"{file} already exists...")
            continue

        if file == zipped_file.absolute().as_posix():
            print(f"skipped: {file}")
            continue

        try:
            zip_file_client.write(file, compress_type=z.ZIP_DEFLATED)
            compress_progress.desc = file
        except (PermissionError, FileNotFoundError):
            pass

    compress_progress.close()
    zip_file_client.close()
    print(f"files compressed at: {zipped_file.as_posix()}")

    return zipped_file



if __name__ == '__main__':
    current_date = get_current_date()
    delete_folder_contents(f"zipped/{current_date}")

    sleep(1)
    files_collection = ExtractFiles(
        *GetMainContents(),
        less_24_mode=1,
        verbose=1,
        overwrite=1
    )
    tar_gz_file = CompressFiles(files_collection, "less_24_files")
    print(tar_gz_file)
