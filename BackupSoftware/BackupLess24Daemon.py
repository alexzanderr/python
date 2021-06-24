
from core.aesthetics import AnsiCodes, ansi_colored
from dependencies import *
from core.datetime__ import get_current_hour
from BackupClientRemoteServer import BackupClientRemoteServer
from time import sleep

BackupClientRemoteServer()

from core.system import (
    get_python_implementation
)


backup_preffered_hour="21"
backup_preffered_hour="21"
backup_preffered_hour="21"
backup_preffered_hour="21"
backup_preffered_hour="21"
try:
    while 1:
        hour = get_current_hour()
        if hour == backup_preffered_hour:
            client = BackupClientRemoteServer(
                server_username,
                server_ip,
                server_password,
                server_port
            )
            client.logger_backup.info(
                f"its {backup_preffered_hour} PM, its time for automated backup"
            )
            client.backup_to_server(less_24_mode=1, zip_mode=1)

            del hour, client
            sleep(60 * 60 * 20) # 20 hours sleep
        else:
            sleep(60 * 60) # 1 hour

except KeyboardInterrupt:
    print("\nBackupLess24Daemon killed. [ KeyboardInterrupt ]\n")
