
"""

    core/__random.py

    useful random stuff to import in your scripts
    contents (random):
        lowchar
        upperchar
        digit
        number
        lowerstring
        upperstring
        string
        date str
        date struct

    author: @alexzander
"""



# python
import time
from datetime import datetime
from random import randint, choice, random


# codes
# a-z 97-122
# A-Z 65-90
# 0-9 48 57
random_lowerchar = lambda : chr(randint(97, 122))
random_upperchar = lambda : chr(randint(65, 90))
random_digit = lambda : randint(0, 9)


def random_digits(dimension):
    if dimension is None:
        raise TypeError
    if dimension <= 0:
        raise ValueError
    return "".join([str(randint(0, 9)) for _ in range(dimension)])


def random_number(dimension):
    if dimension is None:
        raise TypeError
    if dimension <= 0:
        raise ValueError
    return int(str(randint(1, 9)) + "".join([str(randint(0, 9)) for _ in range(dimension - 1)]))


def random_lower_str(dimension):
    if dimension is None:
        raise TypeError
    return "".join([
        chr(randint(ord("a"), ord("z"))) for _ in range(dimension)
    ])


def random_upper_str(dimension):
    if dimension is None:
        raise TypeError
    return "".join([
        chr(randint(ord("A"), ord("Z"))) for _ in range(dimension)
    ])


def random_str(dimension):
    if dimension is None:
        raise TypeError
    return "".join([
        choice([
            chr(randint(ord("a"), ord("z"))),
            chr(randint(ord("A"), ord("Z")))
        ]) for _ in range(dimension)
    ])


def random_date_str(starting_date="01.01.1971", ending_date=datetime.now().strftime("%d.%m.%Y")):
    if starting_date is None or ending_date is None:
        raise TypeError

    datetime_format = "%d.%m.%Y"
    start_time = time.mktime(time.strptime(starting_date, datetime_format))
    stop_time = time.mktime(time.strptime(ending_date, datetime_format))
    random_time = start_time + random() * (stop_time - start_time)
    return time.strftime(datetime_format, time.localtime(random_time))


def random_date_struct(starting_date="01.01.1971", ending_date=datetime.now().strftime("%d.%m.%Y")):
    if starting_date is None or ending_date is None:
        raise TypeError

    datetime_format = "%d.%m.%Y"
    start_time = time.mktime(time.strptime(starting_date, datetime_format))
    stop_time = time.mktime(time.strptime(ending_date, datetime_format))
    random_time = start_time + random() * (stop_time - start_time)
    return time.strptime(time.strftime(datetime_format, time.localtime(random_time)), datetime_format)