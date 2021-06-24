

# python
import os
import subprocess
import platform
from pathlib import Path
import json.decoder

operating_system = platform.system().lower()

windows = operating_system == "windows"
linux = operating_system == "linux"
macos = operating_system == "darwin"


# project
from TyperacerAnalytics.imports import *
from datetime import datetime


import matplotlib
import matplotlib.pyplot as plt



# pypi
import numpy as np

if windows:
    from TyperacerAnalytics.imports import *
    from core.json__ import *
    from core.numbers__ import *
    from core.datetime__ import *


# how to modify font of plot, google
# this is not working
# monaco_font = {"fontname": "monaco"}

plt.style.use('Solarize_Light2')


def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


def __plot_stats(stats_json, path):
    if isinstance(stats_json, dict):
        if stats_json:
            indices = [i for i in range(1, len(stats_json["wpm"]) + 1)]
            wpm_values = stats_json["wpm"]

            if len(wpm_values) == 1:
                width = 0.1
            else:
                width = 0.3

            x = np.arange(len(wpm_values))

            fig, ax = plt.subplots()
            rects = ax.bar(x - width / 2, wpm_values, width, label='WPM')


            ax.set_ylabel("WPM")
            space = " " * 3
            avg = "{:.2f}".format(float(stats_json['wpm_average']))
            xlabel_text = f"max: {stats_json['wpm_max']}{space}|{space}min: {stats_json['wpm_min']}{space}|{space}average: {avg}"

            ax.set_xlabel(xlabel_text)

            domain_name = list(filter(lambda x: x != "", stats_json['url'].split("/")))
            try:
                domain_name = domain_name[1]
            except IndexError:
                domain_name = domain_name[0]
            space = " " * 5

            try:
                ax.set_title(f"{domain_name}{space}-{space}[{stats_json['date']}]")
            except KeyError:
                ax.set_title(f"{domain_name}{space}-{space}[{get_current_date()}]")

            ax.set_xticks(x)
            ax.set_xticklabels(indices)
            # ax.set_facecolor((0.4, 0.4, 0.5))


            autolabel(rects, ax)
            fig.tight_layout()
            # plt.show()

            # ax_children = ax.get_children()
            # for index, children in enumerate(ax_children):
            #     print(children)
            #     if isinstance(children, matplotlib.patches.Rectangle):
            #         ax_children[index].set_color((1, 0.6, 0.3))

            plt.gcf().set_size_inches(30, 16) # 3000 x 1600 pixels
            if isinstance(path, Path):
                plt.savefig(path.as_posix())
            else:
                plt.savefig(path)

            plt.clf()


def PlotStats():
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
            stats_path = date_path / (ten_fast_fingers_com + "_stats.json")
            if stats_path.exists():
                stats_json = json.loads(stats_path.read_text())

                save_path = date_path / (ten_fast_fingers_com + "_plot")
                __plot_stats(stats_json, save_path.as_posix() + ".png")


            # playtyperacer
            stats_path = date_path / (play_typeracer_com + "_stats.json")
            if stats_path.exists():
                stats_json = json.loads(stats_path.read_text())

                save_path = date_path / (play_typeracer_com + "_plot")
                __plot_stats(stats_json, save_path.as_posix() + ".png")


            # typingio
            stats_path = date_path / (typing_io + "_stats.json")
            if stats_path.exists():
                stats_json = json.loads(stats_path.read_text())

                save_path = date_path / (typing_io + "_plot")
                __plot_stats(stats_json, save_path.as_posix() + ".png")


if __name__ == '__main__':
    PlotStats()
