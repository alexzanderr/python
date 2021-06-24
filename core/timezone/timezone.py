
"""

"""

# python
import os
from datetime import datetime

# 3rd party
import pytz # pip install pytz


class timezone_Exception(Exception):
    def __init__(self, message=""):
        self.message = message


class TimezoneNotFoundError(timezone_Exception):
    pass


def get_current_timezone(location="Europe/Bucharest"):
    """ @location: Continent/City"""
    if location not in pytz.all_timezones:
        raise TimezoneNotFoundError

    current_datetime = datetime.now(pytz.timezone(location)).strftime("%d.%m.%Y-%H:%M:%S")
    _location = "-".join(location.split("/"))
    return f"{_location}-{current_datetime}"


def get_current_timezone_time(location="Europe/Bucharest", time_format="%H:%M:%S"):
    """ @location: Continent/City"""
    if location not in pytz.all_timezones:
        raise TimezoneNotFoundError

    return datetime.now(pytz.timezone(location)).strftime(time_format)


def get_current_timezone_date(location="Europe/Bucharest", date_format="%d.%m.%Y"):
    """ @location: Continent/City"""
    if location not in pytz.all_timezones:
        raise TimezoneNotFoundError

    return datetime.now(pytz.timezone(location)).strftime(date_format)