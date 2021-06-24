
"""
    core/zip__.py

    wrapper for zipfile.py

    author: @alexzander
"""


import os
import zipfile


def unzip(path, folder):
    if not os.path.isfile(path):
        raise ValueError
    if not os.path.isdir(folder):
        raise ValueError

    with zipfile.ZipFile(path, "r") as file:
        file.extractall(folder)


def zip_files(folder, zipname):
    if type(folder) == list:
        for file in folder:
            if not os.path.isfile(file):
                raise ValueError
    elif type(folder) == str:
        if not os.path.isfile(folder):
            raise ValueError
        folder = [folder]

    sep = "/" if "/" in folder[0] else "\\"
    working_directory = folder[0].split(sep)
    working_directory = sep.join(working_directory[:len(working_directory) - 1])


    wd_name = working_directory.split(sep)
    wd_name = wd_name[len(wd_name) - 1]
    for file in folder:
        items = file.split(sep)
        folder_name = items[len(items) - 2]
        if folder_name != wd_name:
            print(folder_name)
            print(working_directory)
            raise ValueError("files should be from the same directory.")

    originalWD = os.getcwd()
    os.chdir(working_directory)

    items = [file.split(sep) for file in folder]
    # just the filename
    folder = [item[len(item) - 1] for item in items]

    with zipfile.ZipFile("{}.zip".format(zipname), "w") as filesZIP:
        for file in folder:
            filesZIP.write(file)
    print("{}.zip created successfully.".format(zipname))
    return working_directory + "\\" + zipname + ".zip"


def zip_folder(folder, zipname):
    if not os.path.isdir(folder):
        raise ValueError

    originalWD = os.getcwd()
    os.chdir(folder)
    files = os.listdir(folder)

    with zipfile.ZipFile("{}.zip".format(zipname), "w") as file_zip:
        for file in files:
            file_zip.write(file)
    os.chdir(originalWD)

    print("{}.zip created successfully.".format(zipname))
    return folder + "\\" + zipname + ".zip"