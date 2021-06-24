
import pyperclip
from random import choice
from core.json__ import *
from core.aesthetics import *


def is_valid(item):
    return item != ""


pickup_lines_json_path = "pickup_lines.json"
pickup_lines_json = read_json_from_file(pickup_lines_json_path)
pickup_lines_json = [item for item in pickup_lines_json if is_valid(item)]


def random_pickupline(database: list):
    pickup_line = choice(database)
    print("Today's pickup line:")
    print_yellow(pickup_line)
    print_green("\ncopied to clipboard!")
    pyperclip.copy(pickup_line)


if __name__ == '__main__':
    random_pickupline(pickup_lines_json)
