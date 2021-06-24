
import os
from subprocess import Popen, PIPE, call
from string import Template
from core.json__ import (
    read_json_from_file,
    write_json_to_file
)
from pathlib import Path
from core.datetime__ import *
import json

speedtest_command_save_data_template = Template(
    "speedtest-cli --secure --json"
)

speedtest_save_data_command = "speedtest-cli --secure --json"

speedtest_results_folder = Path(
    os.path.expanduser("~/Alexzander__/logs/speedtest")
)
speedtest_results_folder.mkdir(exist_ok=1)


while True:
    print("started speedtest ...")

    print("speedtest in progress...")
    process = Popen(speedtest_save_data_command,
                    shell=1, stderr=PIPE, stdout=PIPE)

    out, err = process.communicate()
    err = err.decode("utf-8")
    out = out.decode("utf-8")

    print("results:\n")
    print(out)
    current_datetime = get_current_datetime()
    save_file_path = speedtest_results_folder / \
        f"speedtest_{current_datetime}.json"

    write_json_to_file(json.loads(out), save_file_path)

    print(f"\nresults saved at: {save_file_path.absolute().as_posix()}")
