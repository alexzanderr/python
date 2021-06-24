

from tqdm import tqdm as progress_bar
import time
from core.datetime__ import (
    get_current_date,
    get_current_datetime,
    seconds_to_time
)
from core import drive


class BackupClientToHardDrive:
    def __init__(self, drive_chosen):
        self.drive_chosen = drive_chosen


    def get_external_drives(self):
        return drive.get_external_drives()


    def copy_file_to_harddrive(self, file_path, destiation_path):
        drive.__copy_content(file_path, destiation_path)


    def backup_to_harddrive(self, less_24_mode=True, zip_mode=True):

        # gather what you need and what is the mode
        files = []

        external_drives = self.get_external_drives()
        if not external_drives:
            raise ConnectionError("there are no external hard drives ONLINE to backup to.")

        drive_chosen = external_drives[0]
        if len(external_drives) > 1:

            print(external_drives)
            while 1:
                try:
                    index = int(input("choose drive to backup to:"))
                    if 1 <= index <= len(external_drives):
                        drive_chosen = external_drives[index - 1]

                    break
                except ValueError:
                    print("invalid index. repeat")

        before = time.time()

        print(f"\nBackup to: {drive_chosen} started at: {get_current_datetime()}\n")
        input("_____")

        for backup_file in progress_bar(
            iterable=files,
            desc="backup",
            total=len(files),
            unit="file",
            ncols=120
        ):
            self.copy_file_to_harddrive(backup_file.file, backup_file.destination)
        print(f"\nBackup to: {drive_chosen} ended at: {get_current_datetime()}")

        execution_time = time.time() - before
        execution_time = seconds_to_time(int(execution_time))
        print(f"\nbackup duration: [ {execution_time} ] seconds")