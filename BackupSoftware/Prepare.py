
import os
from core.json__ import *
from dependencies import *
from ExtractFiles import ExtractFiles
from MainContents import (
    GetMainContents,
    main_content_to_backup_file,
    backup_folder
)

class BackupApplicationFile:
    def __init__(self, file, dest):
        self.file = file
        self.root_folder = dest

        if windows:
            items = self.file.split(os.path.sep)
            self.dest = dest \
            + "/".join(items[1:])

            self.dirname = self.root_folder + "/".join(items[1:-1])
        else:
            self.dest = dest + self.file
            self.dirname = self.root_folder + "/".join(self.file.split(os.path.sep)[:-1])

    def __str__(self):
        return f"(file={self.file_path}, dest_folder={self.destination_folder})"


def InstantiateWithBackupApplicationFile(files, destination, name):
    less_24_json = []
    backup_application_files = []
    for file in files:
        b = BackupApplicationFile(file, destination)
        backup_application_files.append(b)
        less_24_json.append({
            "file": b.file,
            "root_folder": b.root_folder,
            "dirname": b.dirname,
            "dest": b.dest
        })
    write_json_to_file(less_24_json, (backup_folder / f"{name}.json").absolute().as_posix())
    return backup_application_files


if __name__ == '__main__':

    pass