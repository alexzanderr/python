
"""
    core/animations.py

    interesting module which includes
    colored animations

    included stuff:
        - colored progress bar
        - colored xmas tree

    author: @alexzander
"""


# python
from time import sleep
from random import choice

# core package ( pip install python-core )
from core.numbers__ import *
from core.aesthetics import *
from core.system import clearscreen

# 3rd party
from colorama import Fore, Style


def progress_bar(
    iteration,
    length,
    decimals=2,
    progressbar_length=40,
    fill_symbol="█",
    color="yellow"
):
    """
        [Progress]: |███████████████████████_________________| [58.00] [Complete]
    """
    if iteration > length:
        raise ValueError("iteration({}) value is greater than total_length({})".format(iteration, length))

    progress_percent = 100 * (iteration / float(length))
    progress_percent = fixed_set_precision_str(progress_percent, decimals)
    filled_length = int(progressbar_length * iteration // length)
    completed = fill_symbol * filled_length + "_" * (progressbar_length - filled_length)

    if iteration == length:
        progressbar = f"[Progress]: |{completed}| [{progress_percent}] [Completed]"
        progressbar = ConsoleColored(progressbar, "green")
    else:
        progressbar = f"[Progress]: |{completed}| [{progress_percent}] [Complete]"
        progressbar = ConsoleColored(progressbar, color)

    return progressbar


def load_progress_bar(
    length=100,
    sleep_duration=0.045,
    color="yellow"
):
    for i in range(length + 1):
        p = progress_bar(i, length, color=color)
        print(p, end="\r")
        sleep(sleep_duration)
    print()


def xmas_tree(
    message,
    allocated_space=None,
    __iterations=True,
    pause=0.8
):
    """
        example of animation wit @message="xmas_tree"
                       *
                       x
                      xma
                     xmas_
                    xmas_tr
                   xmas_tree
                     ||||
                     ||||
                 =============
                 =============
    """
    __len_message = len(message)
    if allocated_space == None:
        allocated_space = __len_message + 4
    else:
        if type(allocated_space) == int:
            if allocated_space <= __len_message:
                allocated_space = __len_message + 4
        else:
            raise TypeError

    tree_colors = [Fore.GREEN, Fore.BLUE, Fore.RED, Fore.YELLOW, Fore.WHITE, Fore.CYAN]

    if __iterations == True:
        while True:
            clearscreen()
            print(Style.BRIGHT + tree_colors[3] + "{:^{space}}".format("*", space=allocated_space))
            for i in range(1, __len_message + 1, 2):
                if i == __len_message:
                    print(Style.BRIGHT + choice(tree_colors) + "{:^{space}}".format(message, space=allocated_space))
                else:
                    print(Style.BRIGHT + choice(tree_colors) + "{:^{space}}".format(message[:i], space=allocated_space))

            print("{:^{space}}".format("||||", space=allocated_space))
            print("{:^{space}}".format("||||", space=allocated_space))
            print('=' * allocated_space)
            print('=' * allocated_space)
            sleep(pause)
        print(Style.RESET_ALL, end="")

    elif type(__iterations) == int and __iterations > 0:
        for _ in range(__iterations):
            clearscreen()
            print(Style.BRIGHT + tree_colors[3] + "{:^{space}}".format("*", space=allocated_space))
            for i in range(1, __len_message + 1, 2):
                if i == __len_message:
                    print(Style.BRIGHT + choice(tree_colors) + "{:^{space}}".format(message, space=allocated_space))
                else:
                    print(Style.BRIGHT + choice(tree_colors) + "{:^{space}}".format(message[:i], space=allocated_space))

            print("{:^{space}}".format("||||", space=allocated_space))
            print("{:^{space}}".format("||||", space=allocated_space))
            print('=' * allocated_space)
            print('=' * allocated_space)
            sleep(pause)
        print(Style.RESET_ALL, end="")





# TESTING
if __name__ == '__main__':
    xmas_tree("xmas_tree", __iterations=5)