

import os
import time
from pathlib import Path
from datetime import datetime
from core.datetime__ import seconds_to_time
from concurrent.futures import ThreadPoolExecutor
from MainContents import GetMainContents, backup_folder


def collect_all(folder):
    files = []
    if isinstance(folder, str):
        for item in os.listdir(folder):
            path = os.path.join(folder, item)
            if os.path.isfile(path):
                files.append(path)
            else:
                files.extend(collect_all(path))

    elif isinstance(folder, Path):
        for item in folder.iterdir():
            if item.is_file():
                files.append(item.absolute().as_posix())
            else:
                files.extend(collect_all(item))
    return files


def less_than_24_hours(file_path):
    hours_difference = datetime.fromtimestamp(time.time()) - datetime.fromtimestamp(os.path.getmtime(file_path))
    hours_difference = int(round(hours_difference.total_seconds() / 3600))
    return hours_difference < 24


def collect_less_than_24_hours(folder):
    collected_4backup = []
    if isinstance(folder, str):
        for item in os.listdir(folder):
            path = os.path.join(folder, item)
            if os.path.isfile(path) and less_than_24_hours(path):
                collected_4backup.append(path)
            elif os.path.isdir(path):
                collected_4backup.extend(collect_less_than_24_hours(path))

    elif isinstance(folder, Path):
        for item in folder.iterdir():
            if item.is_file() and less_than_24_hours(item):
                collected_4backup.append(item.absolute().as_posix())
            elif item.is_dir():
                collected_4backup.extend(collect_less_than_24_hours(item))
    return collected_4backup


def gather_contents_4backup(folder, ignore=[]):
    files = []
    folders = []

    if isinstance(folder, str):
        for item in os.listdir(folder):
            if ignore:
                if item in ignore:
                    continue

            full_path = folder + os.path.sep + item
            if os.path.isdir(full_path):
                folders.append(full_path)
            else:
                files.append(full_path)

    elif isinstance(folder, Path):
        for item in folder.iterdir():
            if item.is_dir():
                folders.append(item.absolute().as_posix())
            else:
                files.append(item.absolute().as_posix())

    return files, folders


def __extract_files_using_threads(
    main_files_array, main_folders_array,
    less_24_mode=True, verbose=False
):
    # copy
    files = main_files_array.copy()
    # params for tasks
    folders_threads = []
    # gathering all items from level=1
    for folder in main_folders_array:
        files, folders = gather_contents_4backup(folder)
        files.extend(files)
        folders_threads.extend(folders)

    if less_24_mode:
        tasks = [(collect_less_than_24_hours, [item]) for item in folders_threads]
        if verbose:
            print(f"Extracting all less than 24 hours files ... (running {len(tasks)} threads) with ThreadPoolExecutor")
    else:
        tasks = [(collect_all, [item]) for item in folders_threads]
        if verbose:
            print(f"Extracting all files ... (running {len(tasks)} threads) with ThreadPoolExecutor")

    # we run a thread for every folder
    # we extract the result to extend to less_24_files
    # printing current status if verbose=True
    with ThreadPoolExecutor(max_workers=len(folders_threads)) as executor:
        for thread_id, task in enumerate(tasks, start=1):
            argument = task[1][0]
            thread_result = executor.submit(task[0], argument)
            if verbose:
                print(f"Thread-{thread_id}: Finished --- ( {argument} )")
            files.extend(thread_result.result())

    return files


def ExtractFiles(
    main_files_array, main_folders_array,
    less_24_mode=True, verbose=False, overwrite=False
):
    extraction_start_time = time.time()

    if less_24_mode:
        files_file = backup_folder / "less_24.txt"
    else:
        files_file = backup_folder / "all_files.txt"

    if not files_file.exists():
        files = __extract_files_using_threads(
            main_files_array,
            main_folders_array,
            less_24_mode=less_24_mode,
            verbose=verbose,
        )
        files_file.write_text("\n".join(files))
    else:
        if overwrite:
            files = __extract_files_using_threads(
                main_files_array,
                main_folders_array,
                less_24_mode=less_24_mode,
                verbose=verbose,
            )
            files_file.write_text("\n".join(files))
        else:
            if verbose:
                print(f"[ {files_file.name} ] already exists, reading from file...")
            files = files_file.read_text().split("\n")

    extraction_duration = seconds_to_time(int(time.time() - extraction_start_time))
    if verbose:
        if less_24_mode:
            print(f"\nless than 24 extraction duration: {extraction_duration}")
        else:
            print(f"\nall files extraction duration: {extraction_duration}")
        print(f"total files that have less than 24 hours modification time: {len(files)}")

    return files


if __name__ == '__main__':
    files = ExtractFiles(*GetMainContents(), 1, 1, 1)