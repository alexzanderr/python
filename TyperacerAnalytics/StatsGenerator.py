

import os
from pathlib import Path
import platform
import json
from datetime import datetime

operating_system = platform.system().lower()

windows = operating_system == "windows"
linux = operating_system == "linux"
macos = operating_system == "darwin"


from TyperacerAnalytics.imports import *
from core.json__ import *
from core.datetime__ import *


def average(array):
    if len(array) == 1:
        return array[0]

    return sum(array) / len(array)


def __generate_stats(_json):
    if isinstance(_json, list):
        if _json:
            stats = {
                "wpm": "",
                "wpm_min": "",
                "wpm_max": "",
                "wpm_average": "",
                "accuracy": "",
                "accuracy_min": "",
                "accuracy_max": "",
                "accuracy_average": "",
                "date": _json[0]["date"],
                "url": _json[0]["url"],
                "total_results": len(_json)
            }

            wpm_array = [item["wpm"] for item in _json]
            accuracy_array = [item["accuracy"] for item in _json if item["accuracy"] != 'None']
            # print(wpm_array)
            # print(accuracy_array)

            if wpm_array:
                stats["wpm"] = wpm_array
                stats["wpm_min"] = min(wpm_array)
                stats["wpm_max"] = max(wpm_array)
                stats["wpm_average"] = average(wpm_array)
            else:
                stats["wpm_min"] = None
                stats["wpm_max"] = None
                stats["wpm_average"] = None

            if accuracy_array:
                stats["accuracy"] = accuracy_array
                stats["accuracy_min"] = min(accuracy_array)
                stats["accuracy_max"] = max(accuracy_array)
                stats["accuracy_average"] = average(accuracy_array)
            else:
                stats["accuracy_min"] = None
                stats["accuracy_max"] = None
                stats["accuracy_average"] = None

            return stats


def GenerateStats():
    # iterating through the results folder
    if windows:
        current_date = get_current_date()
    elif linux:
        current_date = datetime.now().strftime("%d.%m.%Y")

    for date_folder in analytics_folder.iterdir():

        # current date
        if date_folder.name == current_date:
            date_path = analytics_folder / date_folder

            # 10fastfingers
            results_path = date_path / (ten_fast_fingers_com + "_results.json")
            if results_path.exists():
                results_json = json.loads(results_path.read_text())
                stats_json = __generate_stats(results_json)

                # saving data at location
                stats_path = date_path / (ten_fast_fingers_com + "_stats.json")
                stats_path.write_text(json.dumps(
                    stats_json, indent=4
                ))

            # playtyperacer
            results_path = date_path / (play_typeracer_com + "_results.json")
            if results_path.exists():
                results_json = json.loads(results_path.read_text())
                # pretty_print(ten_fast_fingers_results_json)
                stats_json = __generate_stats(results_json)

                stats_path = date_path / (play_typeracer_com + "_stats.json")
                stats_path.write_text(json.dumps(
                    stats_json, indent=4
                ))

            # typingio
            results_path = date_path / (typing_io + "_results.json")
            if results_path.exists():
                results_json = json.loads(results_path.read_text())

                stats_path = date_path / (typing_io + "_stats.json")

                stats_json = __generate_stats(results_json)
                stats_path.write_text(json.dumps(
                    stats_json, indent=4
                ))


if __name__ == '__main__':
    GenerateStats()