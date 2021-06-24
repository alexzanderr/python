
"""
    core/drive.py

    useful in development of programs that
    involve work with the disk drive or any

    disk drive

    copy files and folders

    open folders

    delete folder

    author: @alexzander
"""


# python
import os
import shutil
import string
import ctypes
from string import ascii_uppercase, ascii_lowercase
import platform
import threading
import subprocess
import multiprocessing
from pathlib import Path
from time import time, sleep
from concurrent.futures import ThreadPoolExecutor

# core package (pip install python-core)
from core.system import *
from core.numbers__ import *
from core.path__ import *
from core.aesthetics import *
import core.exceptions



operating_system = platform.system().lower()
windows = operating_system == "windows"
linux = operating_system == "linux"
macos = operating_system == "darwin"

if windows:
# pypi
    from win32 import win32api # pip install pywin32
    from win32com.client import Dispatch # pip install pywin32


def GetDriveLetterName(drive_letter: str):
    """
        gets drive name by parsing letter
    """
    if not isinstance(drive_letter, str):
        raise TypeError(drive_letter)

    if len(drive_letter) == 1:
        drive_letter = drive_letter.lower()
        if not drive_letter in ascii_lowercase:
            raise ValueError(f"drive letter doesnt contain letters: {drive_letter}")

        drive_letter = f"{drive_letter}:\\"

    elif len(drive_letter) > 1:
        if not os.path.isdir(drive_letter):
            raise NotADirectoryError(drive_letter)


    kernel32 = ctypes.windll.kernel32
    volumeNameBuffer = ctypes.create_unicode_buffer(1024)
    fileSystemNameBuffer = ctypes.create_unicode_buffer(1024)

    result = kernel32.GetVolumeInformationW(
        ctypes.c_wchar_p(drive_letter),
        volumeNameBuffer,
        ctypes.sizeof(volumeNameBuffer),
        fileSystemNameBuffer,
        ctypes.sizeof(fileSystemNameBuffer)
    )

    return volumeNameBuffer.value


def __copy_content(
    source: str,
    destination: str,
    __print=False
) -> bool: #):
    """
        @source is absolute path and file.
        @destination is absolute path and file.

        @__copy_content()
            deletes the content from @destination,
            reads from @source in binary and
            writes in binary to @destination
    """
    try:
        process = "copied"
        if os.path.exists(destination):
            process = "overwrited"

        with open(source, "rb") as source_binary:
            with open(destination, "wb") as destination_binary:
                # if the @destination file doesnt exist
                # is created automatically

                # deleted existed content
                destination_binary.truncate(0)
                # replaced with brand-new one
                destination_binary.write(source_binary.read())

        if __print:
            print("[" + "=" * 50 + "]")
            print(f"source_path: {blue_bold(source)}")
            print("[~]")
            print(f"destintation_path: {cyan_bold(destination)}")
            print("[~]")
            print(f"file: {yellow_bold(os.path.basename(source))}")
            print("[~]")
            print(green_bold(f"[ {process} ] successfully!"))
            print("[" + "=" * 50 + "]\n")

    except BaseException as exception:
        print_red_bold(type(exception))
        print_red_bold(exception)
        return False

    # copy in binary was successful
    return True


def gather_relatives(
    source,
    relative=os.path.sep,
    __ignore=[]
) -> list: #):
    """
        function @__gather_relatives() works recursively

        example:
            @input
            source: D:\\Alexzander__\\programming\\python\\xerox_data

            @return contents from @source folder
            relative_paths = [
                \\script.py
                \\xerox_data.jpg
                \\xerox_data.txt
                \\WorkCentre3225_Configuration_Report.json
            ]
    """
    relative_paths = []
    for content in os.listdir(source):
        # full path of content
        path = os.path.join(source, content)

        # is file
        if os.path.isfile(path):
            # verify if @content is in @__ignore
            if __ignore != []:
                extension = "*" + os.path.splitext(path)[1]
                # *.spec or PythonFile.spec
                if extension in __ignore or content in __ignore:
                    continue

            relative_paths.append(relative + content)

        # is dir
        elif os.path.isdir(path):
            # verify if @content is in @__ignore
            if __ignore != [] and content in __ignore:
                continue

            # putting recursively
            relative_paths.extend(gather_relatives(
                source   = path,
                relative = relative + content + os.path.sep,
                __ignore = __ignore
            ))

    return relative_paths


def copy_content(
    source,
    destination,
    open_destination_when_done=False,
    __print=False,
    __ignore=[]
) -> bool: #):
    """
        the function will copy only the contents from
        @source, meaning that the dirname is excluded
        if @source is a dir.

        if @source and @destination are lists with full
        paths, then we copy every item from @source to
        item from@destination.
    """
    try:
        # list with source full paths and list with dest full paths
        if  isinstance(source, list) and \
            isinstance(destination, list):
            # copy items using parallel iteration
            for _source, _destination in zip(source, destination):
                # creating the folders
                path = os.path.dirname(_destination)
                if not os.path.exists(path):
                    os.makedirs(path)

                if not os.path.isfile(_source) and not os.path.isabs(_destination):
                    raise ValueError(f"contents from @source list and @destination list are NOT files.")

                code0 = __copy_content(_source, _destination, __print)
                if not code0:
                    raise RuntimeError("something went wrong; __copy_content() returned False")

            if open_destination_when_done:
                _destination = os.path.dirname(destination[0])
                open_folder(_destination)

        # list with source full paths and dir
        elif    isinstance(source, list) and \
                isinstance(destination, str):

                # creating the folders
                if not os.path.exists(destination):
                    os.makedirs(destination)

                destination_full_paths = [
                    os.path.join(destination, os.path.basename(source_fp))
                    for source_fp in source
                ]

                for _source, _destination in zip(source, destination_full_paths):

                    if  not os.path.isfile(_source) and \
                        not os.path.isabs(_destination):
                        raise ValueError(f"contents from @source list and @destination list are NOT files.")

                    code0 = __copy_content(_source, _destination, __print)
                    if not code0:
                        raise RuntimeError("something went wrong; __copy_content() returned False")

                if open_destination_when_done:
                    open_folder(destination)

        else:
            # dir to dir
            if os.path.isdir(source) and os.path.isdir(destination):
                # generating relative paths from source
                relative_paths = gather_relatives(
                    source   = source,
                    __ignore = __ignore
                )
                # generating full paths with relatives for source and destination
                source_full_paths = [source + relative for relative in relative_paths]
                destination_full_paths = [destination + relative for relative in relative_paths]

                # creating dirs if they dont exist
                for destination_fp in destination_full_paths:
                    # path from absolute
                    path = os.path.dirname(destination_fp)
                    if not os.path.exists(path):
                        os.makedirs(path)

                # copy process
                for source_fp, destination_fp in zip(source_full_paths, destination_full_paths):
                    code0 = __copy_content(source_fp, destination_fp, __print)
                    if not code0:
                        raise RuntimeError("something went wrong; __copy_content() returned False")

                # open destination when done
                if open_destination_when_done:
                    open_folder(destination)

            # file to dir
            elif os.path.isfile(source) and os.path.isdir(destination):
                file_name_plus_extension = os.path.basename(source)
                code0 = __copy_content(source, destination + os.path.sep + file_name_plus_extension, __print)
                if not code0:
                    raise RuntimeError("something went wrong; __copy_content() returned False")

                # open destination when done
                if open_destination_when_done:
                    open_folder(destination)

            # file to file
            elif os.path.isfile(source) and os.path.isfile(destination):
                code0 = __copy_content(source, destination, __print)
                if not code0:
                    raise RuntimeError("something went wrong; __copy_content() returned False")

                # open destination when done
                if open_destination_when_done:
                    dest = os.path.dirname(destination)
                    open_folder(dest)

            # dir to file (impossible)
            else:
                raise ValueError(f"you cant copy a dir({source}) into a file({destination})")


    except BaseException as exception:
        # pe linux asta nu merge
        # print_blue_bold(BaseException.with_traceback(exception))
        # print_red_bold(type(exception))
        # print_red_bold(exception)
        # code != 0
        return False

    # code=0
    return True


def create_shortcut(
    source: str,
    destination: str,
    __print=False
) -> bool: #):
    """
        creates shortcut of @src and puts it into
        @dst with name

        prints output of code=0 to the screen if __print
    """
    # params validation
    if not os.path.isfile(source):
        raise NotAFileError(source)
    if not os.path.isdir(destination):
        raise NotADirectoryError(destination)
    # /params validation

    destination = os.path.normpath(destination)

    # creation of shortcut
    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(
        os.path.join(
            destination,
            os.path.basename(source) + ".lnk"
        )
    )
    shortcut.TargetPath = source
    shortcut.WorkingDirectory = os.path.dirname(source)
    shortcut.IconLocation = source
    shortcut.save()

    if __print:
        print()
        print("[" + "=" * 50 + "]")
        print("source: {}".format(blue(source)))
        print("[~]")
        print("destination: {}".format(cyan(destination)))
        print("[~]")
        print(green_bold("was made shortcut successfully!"))
        print("[" + "=" * 50 + "]")
        print()

    # code=0
    return True


def is_flash_drive(drive: str):
    """ checks if a drive is USB-drive or NOT """
    try:
        os.listdir(drive)
        return True
    except PermissionError:
        return False


import platform
operating_system = platform.system().lower()

windows = operating_system == "windows"
linux = operating_system == "linux"
macos = operating_system == "darwin"

def get_available_drives():
    """ gets all available drives """
    ops = get_operating_system()
    if ops == "windows":
        return win32api.GetLogicalDriveStrings().split("\000")[:-1]
    elif ops == "linux":
        return os.listdir("/media")
    elif ops == "darwin":
        return os.listdir("/Volumes")


def get_available_drives_non_usb():
    """ return all NON-USB drives that you can copy files to """
    return [dv for dv in get_available_drives() if is_flash_drive(dv)]


def get_external_drives():
    all_drives = get_available_drives_non_usb()

    if windows:
        return list(filter(lambda item: "d" not in item.lower() and "c" not in item.lower(), all_drives))

    return all_drives


def open_folder(path: str):
    """ opens folder """

    # validation
    if not os.path.isdir(path):
        raise NotAFolderError(path)
    # /validation

    ops = get_operating_system()
    if ops == "Windows":
        os.system(f'powershell invoke-item "{path}"')
    elif ops == "Linux":
        os.system("xdg-open \"{}\"".format(path))
    elif ops == "Darwin":
        os.system("open \"{}\"".format(path))


def open_file(path: str):
    """ opens a file """

    # validation
    if not os.path.isfile(path):
        raise NotAFileError
    # /validation

    ops = get_operating_system()
    if ops == "Windows":
        os.startfile(path)
    elif ops == "Linux":
        os.system("xdg-open \"{}\"".format(path))
    elif ops == "Darwin":
        os.system("open \"{}\"".format(path))


def delete_folder(folder: str, verbose=False):
    """
        deletes a folder recursively
    """
    try:
        if isinstance(folder, str):
            folder = Path(folder)
            shutil.rmtree(folder)
            if verbose:
                print(f"deleted: {folder.absolute().as_posix()} [ code=0 ]\n")

        elif isinstance(folder, Path):
            shutil.rmtree(folder)
            if verbose:
                print(f"deleted: {folder.absolute().as_posix()} [ code=0 ]\n")

    except Exception as exception:
        print(f"error: {exception}")
        return False

    # success
    return True

def delete_folder_contents(folder: str, ignore=[], __print=False):
    if not os.path.isdir(folder):
        raise NotADirectoryError(folder)

    try:
        __contents = os.listdir(folder)
    except PermissionError:
        if __print:
            print(f"{red_bold('access denied')}: [ {lime_green(folder)} ]")
            print(f"cant delete this folder")
    else:
        for content in __contents:
            if content in ignore:
                continue

            path = os.path.join(folder, content)

            if os.path.isfile(path):
                os.remove(path)
                if __print:
                    print(f"{red_bold('deleted')}: [ {lime_green(path)} ]")

            elif os.path.isdir(path):
                delete_folder_contents(path, __print)

    # code=0
    return True


def extract_folders(file: str, path: str, curr_lvl=1, deep_lvl=2, __print=False):
    """
        function used to gather folders on different
        deepness level in order to maximize efficient in
        file searching on disk

        return => @extracted_folders, list of folder paths
            that will be helpful for creating a thread
            searching on that folder path for @file

        raise core.exceptions.StopRecursive exception if file is found
    """

    # list with paths
    extracted_folders = []
    try:
        sep = get_path_sep(path)
        for item in os.listdir(path):
            full_path = path + sep + item

            if os.path.isdir(full_path):
                if __print:
                    print_red(full_path)
                if curr_lvl < deep_lvl:
                    extracted_folders.extend(extract_folders(file, full_path, curr_lvl + 1, deep_lvl, __print))
                elif curr_lvl == deep_lvl:
                    extracted_folders.append(full_path)

            elif os.path.isfile(full_path):
                if file == item:
                    if __print:
                        print_green("\nfile found!\n")
                        print("located on: {}".format(blue_underlined(full_path)))
                    raise core.exceptions.StopRecursive(full_path)
                else:
                    if __print:
                        print_red(full_path)

    except NotADirectoryError:
        if file == path.split(sep)[-1]:
            if __print:
                print_green_bold("\nfile found!\n")
                print("located on: {}".format(blue_underlined(path)))
            raise core.exceptions.StopRecursive(path)

    except PermissionError:
        pass

    return extracted_folders


def find_file_on_drive(file: str, path: str, __threading=True, deep_level=1, __print=False):
    """
        if @__threading is True
            this function search the @file on many threads concurrently
            no. of threads == no. of folder in the @path folder

            it is recommended to have as many folders as possible in the @path folder
            otherwise if you have 3 folders means 3 threads and if you are searching in 1 TB of data
                its gonna take a while


        else
            searches recursively on a single thread (not recommended)

        if file was found
            return file_path
        else
            return False

    """
    if __threading:
        search_tasks = []
        try:
            extracted_folders = extract_folders(file, path, deep_lvl=deep_level, __print=__print)
        except core.exceptions.StopRecursive as result:
            # we found the file before
            # creating the search threads
            return result.message

        max_workers = len(extracted_folders)
        for path in extracted_folders:
            search_tasks.append((__find_file_on_drive, [file, path, __print]))

        if __print:
            print()
            for task in search_tasks:
                print(task)
            print("\nThere are [ {} ] threads prepared for execution.\n".format(red_bold(len(search_tasks))))

            choice = input("proceed? [y/n]:\n")
            if choice != "y":
                return red_bold("finding-process-canceled")

            print_yellow_bold("\nsearching...\n")

            before = None

        try:
            workers_results = []
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                if __print:
                    before = time()

                for task in search_tasks:
                    workers_results.append(executor.submit(task[0], *task[1]))

                for wr in workers_results:
                    wr = wr.result()
                    if wr != None and os.path.isabs(wr):
                        if __print:
                            after = time() - before
                            after = fixed_set_precision_str(after, 2)
                            print("from thread-pool")
                            print("execution time: [ {} seconds(s) ]".format(yellow_bold(after)))
                        return wr

        except core.exceptions.StopRecursive as result:
            if __print:
                after = time() - before
                after = fixed_set_precision_str(after, 2)
                print("from exception")
                print("execution time: [ {} seconds(s) ]".format(yellow_bold(after)))
            return result.message

    else:
        # non-threaded version (ignore)
        try:
            __find_file_on_drive(file, path, __print)
        except core.exceptions.StopRecursive as result:
            return result.message

    # file was not found on the entire disk
    # case 1: it doesnt exist
    # case 2: file name is incorrectly provided
    return False


def __find_file_on_drive(file: str, path: str, __print=False):
    try:
        sep = get_path_sep(path)
        for item in os.listdir(path):
            full_path = path + sep + item

            if os.path.isdir(full_path):
                if __print:
                    print_red(full_path)
                __find_file_on_drive(file, full_path, __print)

            elif os.path.isfile(full_path):
                if file == item:
                    if __print:
                        print_green(full_path)
                        print_green_bold("\n\nfile found!")
                        print("located on: {}\n\n".format(blue_underlined(full_path)))
                    raise core.exceptions.StopRecursive(full_path)
                else:
                    if __print:
                        print_red(full_path)

    except NotADirectoryError:
        if file == path.split(sep)[-1]:
            print_green_bold("\nfile found!\n")
            print("located on: {}".format(blue_underlined(path)))

    except PermissionError:
        # this is a system folder
        # or another process is using this
        # file or folder
        pass


def get_size_in_bytes(path: str):
    size = 0
    if os.path.isfile(path):
        size += os.path.getsize(path)

    elif os.path.isdir(path):
        sep = get_path_sep(path)
        for __item in os.listdir(path):
            size += get_size_in_bytes(path + sep + __item)

    return size


chunk_size = 1000
digital_units = ["KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]

def convert_size_in_bytes(size):
    """
        return tuple (
            size,
            digital measurement unit for size
        )
    """
    if size < chunk_size:
        return size, "bytes"

    index = -1
    while (size % chunk_size) != size:
        size //= chunk_size
        index += 1

    return size, digital_units[index]


def get_size_on_disk(path: str):
    """
        return tuple (
            size,
            digital measurement unit for size
        )
    """
    return convert_size_in_bytes(get_size_in_bytes(path))


def is_folder_empty(path: str):
    """ tests whether the @source_folder is empty or not """

    # validation
    if type(path) != str:
        path = str(path)
    if not is_folder(path):
        raise NotAFolderError
    # /validation
    return os.listdir(path) == 0


def is_file_empty(path: str):
    if not is_file(path):
        raise NotAFileError

    try:
        content = open(path, "r+").read()
        if content == "ÿþ" or content == "":
            return True
    except Exception as error:
        print(error)
        print(error.message)
        print(type(error))

    return False




# TESTING
if __name__ == '__main__':
    # testing copy function
    source = r"D:\Alexzander__\programming\python\Python2Executable"
    destination = r"D:\Alexzander__\programming\python\testing_copy_func"

    # print(os.listdir(source))
    copy_content(source, destination, open_destination_when_done=True, __print=True)