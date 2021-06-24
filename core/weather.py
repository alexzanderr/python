
"""
    system.py

    wheather module wrapped around
    pyowm ( open wheather map api)

    author: @alexzander
"""


# 3rd party
from pyowm import OWM

# core package (pip install python-core)
from core.system import *


class Wheather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.manager = OWM(self.api_key)



    def get_temperature(self, location, unit_measurement="celsius"):
        w = self.manager.weather_at_place(location).weather
        return w.temperature(unit_measurement)["temp"]




def __kelvin_celsius(temperature, operator: str):
    if type(temperature) not in [str, int, float]:
        raise TypeError(f"temperature: {temperature} is invalid type: {type(temperature)}")

    if operator == "+":
        return float(temperature) + 273.15
    elif operator == "-":
        return float(temperature) - 273.15


def celsius_to_kelvin(temperature):
    """
        Celsius -> Kelvin
    """
    return __kelvin_celsius(temperature, '+')


def kelvin_to_celsius(temperature):
    """
        Kelvin -> Celsius
    """
    return __kelvin_celsius(temperature, '-')


def __celsius_fahrenheit(temperature, operator: str):
    if type(temperature) not in [str, int, float]:
        raise TypeError(f"temperature: {temperature} is invalid type: {type(temperature)}")

    if operator == "+":
        return float(temperature) * 9 / 5 + 32
    elif operator == "-":
        return 5 / 9 * (float(temperature) - 32)


def celsius_to_fahrenheit(temperature):
    """
        Celsius -> Fahrenheit
    """
    return __celsius_fahrenheit(temperature, '+')


def fahrenheit_to_celsius(temperature):
    """
        Fahrenheit -> Celsius
    """
    return __celsius_fahrenheit(temperature, '-')


def fahrenheit_to_kelvin(temperature):
    """
        Fahrenheit -> Kelvin
    """
    _celsius_temp = fahrenheit_to_celsius(temperature)
    return celsius_to_kelvin(_celsius_temp)


def kelvin_to_fahrenheit(temperature):
    """
        Kelvin -> Fahrenheit
    """
    _celsius_temp = kelvin_to_celsius(temperature)
    return celsius_to_fahrenheit(_celsius_temp)


# TESTING
if __name__ == '__main__':
    # usage
    # api_key = "your api key from open weather map website"
    # w = Wheather(api_key)
    # t = w.get_temperature("Aalbord")
    # print(t)
    pass