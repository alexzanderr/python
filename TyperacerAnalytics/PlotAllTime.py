

from imports import *
from core.json__ import *
from core.numbers__ import *

from PlotStats import __plot_stats


def average(array):
    if len(array) == 1:
        return array[0]

    return sum(array) / len(array)

def GenerateAllTimeAnalytics(website):
    wpms = []
    accuracies = []
    dates = []
    total_results = 0
    for folder in analytics_folder.iterdir():
        try:
            stats_json = read_json_from_file(folder / f"{website}_stats.json")
            wpms.extend(stats_json["wpm"])
            accuracies.extend(stats_json["accuracy"])

            dates.append(stats_json["date"])
            total_results += stats_json["total_results"]

        except FileNotFoundError:
            pass

    wpms = list(map(float, wpms))
    accuracies = list(map(float, accuracies))

    all_time_stats_json = {
        "wpm": wpms,
        "wpm_min": min(wpms),
        "wpm_max": max(wpms),
        "wpm_average": fixed_set_precision_float(average(wpms), 2),
        "accuracy": accuracies,
        "accuracy_min": min(accuracies),
        "accuracy_max": max(accuracies),
        "accuracy_average": fixed_set_precision_float(average(accuracies), 2),
        "dates": dates,
        "url": website,
        "total_results": total_results
    }

    all_time_stats_json_file = all_time_analytics_folder / f"{website}_all_time_stats.json"
    write_json_to_file(all_time_stats_json, all_time_stats_json_file)

    __plot_stats(all_time_stats_json, all_time_analytics_folder / f"{website}_all_time_plot.png")





if __name__ == '__main__':

    print(GenerateAllTimeAnalytics(ten_fast_fingers_com))
    print(GenerateAllTimeAnalytics(play_typeracer_com))
    print(GenerateAllTimeAnalytics(typing_io))
