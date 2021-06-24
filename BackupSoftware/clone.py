
# python
import time
import requests
import subprocess
from string import Template
from pathlib import Path
from datetime import datetime

# core
from core.json__ import *
from core import drive
from core.aesthetics import *
from core.numbers__ import fixed_set_precision_str
from core.datetime__ import (
    get_current_date,
    get_current_datetime,
    seconds_to_time
)
from core.logging__ import *
from core.winapi__ import windows_notification

# project
from dependencies import *
from ExtractFiles import ExtractFiles
from MainContents import GetMainContents, main_content_to_backup_file
from Prepare import InstantiateWithBackupApplicationFile
from ZipContents import CompressFiles

# pypi
from tqdm import tqdm as progress_bar


metadata_folder_path = "metadata"
metadata_folder = Path(metadata_folder_path)
metadata_folder.mkdir(parents=1, exist_ok=1)

remote_metadata_folder_path = r"D:\Alexzander__\PythonApplicationsAppData\BackupSoftware\metadata"
remote_metadata_folder = Path(remote_metadata_folder_path)
remote_metadata_folder.mkdir(parents=1, exist_ok=1)

current_date_remote_metadata_folder = remote_metadata_folder / get_current_date()
current_date_remote_metadata_folder.mkdir(parents=1, exist_ok=1)


class BackupClientRemoteServer:
    pscp_command_template = Template(
        'pscp ${quiet} ${recursive} -P 22 -pw ${password} "${file_path}" ${username}@${ip_address}:"${destination_folder}"'
    )

    def __init__(self, username, ip_address, password, port, overwrite=True):
        self.username = username
        self.ip_address = ip_address
        self.password = password
        self.port = port
        self.server_http_url = f"http://{self.ip_address}:{self.port}/"
        self.overwrite = overwrite

        # no output
        self.pscp_command = Template(self.pscp_command_template.safe_substitute(
            quiet="",
            recursive="",
            password=self.password,
            username=self.username,
            ip_address=self.ip_address,
        ))
        self.pscp_quiet_command = Template(self.pscp_command_template.safe_substitute(
            quiet="-q",
            recursive="",
            password=self.password,
            username=self.username,
            ip_address=self.ip_address,
        ))
        # for folders only
        self.pscp_recursive_command = Template(self.pscp_command_template.safe_substitute(
            quiet="",
            recursive="-r",
            password=self.password,
            username=self.username,
            ip_address=self.ip_address,
        ))
        # no output for folders only
        self.pscp_quiet_recursive_command = Template(self.pscp_command_template.safe_substitute(
            quiet="-q",
            recursive="-r",
            password=self.password,
            username=self.username,
            ip_address=self.ip_address,
        ))

        self.logger_backup = Loggerr(
            BackupClientRemoteServer.__name__,
            foldername="server_backup_logs",
            filename="backup"
        )


    def create_server_folder(self, folder):
        requests.post(self.server_http_url, json={
            "folder": folder  # example: /home/alexzander/testing_http_server/test1/test2
        })


    def is_server_online(self):
        try:
            self.logger_backup.info(f"checking server: {self.server_http_url} ...")
            response = requests.get(self.server_http_url)
            if response.status_code != 200:
                response.raise_for_status()
            return True

        except requests.RequestException:
            return False


    def copy_quiet(self, file, dest):
        self.create_server_folder(dest)
        subprocess.call(self.pscp_quiet_command.safe_substitute(
            file_path=file,
            destination_folder=dest
        ))


    def backup_to_server(self, less_24_mode=True, zip_mode=True):
        if not self.is_server_online():
            self.logger_backup.info(f"warning: server {self.server_http_url} is OFFLINE")

        backup_start_time = time()
        backup_start_datetime = get_current_datetime()

        if zip_mode:
            # files generation
            self.logger_backup.info("generating files ...")
            files_collection = ExtractFiles(
                *GetMainContents(),
                less_24_mode=less_24_mode,
                verbose=1,
                overwrite=self.overwrite
            )
            self.logger_backup.info("generated.")

            if less_24_mode:
                _name = "less_24_files"
            else:
                _name = "all_files"

            # Path object
            tar_gz_file = CompressFiles(
                files_collection,
                _name,
                overwrite=self.overwrite
            )
            del _name

            if not self.is_server_online():
                if windows:
                    windows_notification(
                        "Backup Client",
                        "start python webserver for backup! (2 mins left until start)",
                        5,
                        "assets/icons/backup.ico",
                        1
                    )
                self.logger_backup.info(f"server: {self.server_http_url} is OFFLINE (this time sleeping 2 minutes)")
                sleep(2 * 60)


            # last chance
            if not self.is_server_online():
                self.logger_backup.exception(f"server: {self.server_http_url} is OFFLINE")
                raise ConnectionError(f"server: {self.server_http_url} is OFFLINE")


            self.logger_backup.info(f"\nBackup to: {self.server_http_url} started at: {backup_start_datetime}\n")

            subprocess.call(self.pscp_command.safe_substitute(
                file_path=tar_gz_file.absolute().as_posix(),
                destination_folder=server_backup_folder
            ))

            tar_gz_file.unlink()

            response = requests.post(self.server_http_url, json={
                "extract": 1,
                "zip_path": server_backup_folder + tar_gz_file.name
            })
            if response.status_code != 200:
                try:
                    response.raise_for_status()
                except requests.RequestException:
                    self.logger_backup.exception(f"Status code: {response.status_code}\n")
                    response.raise_for_status()

            if not response.json()["extract_result"] == "success":
                raise ValueError(response.json()["extract_result"])


            backup_finish_datetime = get_current_datetime()
            self.logger_backup.info(
                f"tar.gz extracted on server successfully\nBackup to: {self.server_http_url} ended at: {backup_finish_datetime}"
            )

            # tar_gz_file.unlink(missing_ok=False)
            self.logger_backup.info(f"{tar_gz_file.name} deleted")

        else:
            # NON ZIP MODE

            # files generation
            self.logger_backup.info("generating files ...")
            files_collection = ExtractFiles(
                *GetMainContents(),
                less_24_mode=less_24_mode,
                verbose=1,
                overwrite=1
            )
            self.logger_backup.info("generated.")
            if less_24_mode:
                _name = "less_24_files"
            else:
                _name = "all_files"

            self.logger_backup.info("generating array with BackupApplicationFiles files ...")
            files_collection = InstantiateWithBackupApplicationFile(
                files_collection,
                server_backup_folder,
                _name
            )
            del _name
            self.logger_backup.info("generated.")


            if not self.is_server_online():
                if windows:
                    windows_notification(
                        "Backup Client",
                        "start python webserver for backup! (2 mins left until start)",
                        5,
                        "assets/icons/backup.ico",
                        1
                    )

                self.logger_backup.warning(f"server: {self.server_http_url} is OFFLINE (this time sleeping 2 minutes)")
                sleep(2 * 60)


            # last chance
            if not self.is_server_online():
                self.logger_backup.exception(f"server: {self.server_http_url} is OFFLINE")
                raise ConnectionError(f"server: {self.server_http_url} is OFFLINE")


            distance = len(files_collection)
            backup_progress = progress_bar(
                iterable=range(distance),
                desc="backup_to_server",
                total=distance,
                unit="file",
                ncols=120
            )

            self.logger_backup.info(f"\nBackup to: {self.server_http_url} started at: {get_current_datetime()}\n")
            if less_24_mode:
                self.logger_backup.info("copying less 24 files ...")
            else:
                self.logger_backup.info("copying all files ...")


            backup_start_time = time()
            total_exception_during_backup = 0
            iterator = 0
            while iterator < distance:
                try:
                    self.copy_quiet(
                        files_collection[iterator].file,
                        files_collection[iterator].dirname
                    )
                    backup_progress.update(1)

                except Exception as error:
                    total_exception_during_backup += 1
                    self.logger_backup.exception(
                        f"\nexception occured at index={iterator}\nfile: {self.files_collection[iterator].file}\ndirname: {self.files_collection[iterator].dirname}\n",
                        print__=False
                    )

                    backup_progress.update(-1)
                    iterator -= 1

                iterator += 1

            backup_progress.close()

            self.logger_backup.info(
                f"{total_exception_during_backup} exceptions occured during backup (see them in log)"
            )
            self.logger_backup.info(
                f"\nBackup to: {self.server_http_url} ended at: {get_current_datetime()}"
            )

        backup_duration = seconds_to_time(int(time() - backup_start_time))
        self.logger_backup.info(f"\nbackup duration: {backup_duration}")

        if windows:
            windows_notification(
                "Backup Client",
                f"backup finished:\n({backup_duration})",
                5,
                "assets/icons/backup.ico",
                1
            )

        size_in_bytes = 0
        for file in files_collection:
            try:
                size_in_bytes += os.path.getsize(file)
            except (FileNotFoundError, PermissionError):
                pass

        total_size = convert_size_in_bytes(size_in_bytes)
        orig_seconds = backup_duration.seconds
        orig_minutes = backup_duration.minutes
        try:
            orig_hours = backup_duration.hours
        except AttributeError:
            orig_hours = 0

        try:
            orig_minutes = backup_duration.minutes
        except AttributeError:
            orig_minutes = 0

        hours = orig_hours + orig_minutes / 60 + orig_seconds / 3600
        minutes = orig_hours * 60 + orig_minutes +  orig_seconds / 60
        seconds = orig_hours * 3600 + orig_minutes * 60 + orig_seconds

        metadata = {
            "started_datetime": backup_start_datetime,
            "finish_datetime": backup_finish_datetime,
            "total_files": len(files_collection),
            "total_size": f"{total_size[0]}{total_size[1]}",
            "total_size_in_bytes": size_in_bytes,
            "total_exceptions": 0,
            "process_interrupted": False,
            "process_interrupted_times": 0,
            "duration_hours": fixed_set_precision_float(hours, 3),
            "duration_minutes": fixed_set_precision_float(minutes, 3),
            "duration_seconds": fixed_set_precision_float(seconds, 3)
        }

        metadata_name = f"backup_metadata_{get_current_date()}_{get_current_time().replace(':', '.')}.json"
        # remote location
        write_json_to_file(
            metadata,
            current_date_remote_metadata_folder / metadata_name
        )

        # local project
        write_json_to_file(
            metadata,
            metadata_folder / metadata_name
        )



if __name__ == '__main__':
    client = BackupClientRemoteServer(
        server_username,
        server_ip_d3h,
        server_password,
        server_port_d3h,
        overwrite=0
    )
    client.backup_to_server()

    # client = BackupClientRemoteServer(
    #     server_username,
    #     server_ip_a88x,
    #     server_password,
    #     server_port_a88x,
    #     overwrite=0
    # )
    # client.backup_to_server()
