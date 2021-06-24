
"""
    core/__numbers.py

    module designed especially for numbers
    but its not like numpy, numpy is god compared to this

    author: @alexzander
"""


def fixed_set_precision_str(real_number: float, precision: int):
    """ takes a @real_number and returns it with specified @precision

        return: str version of the number
    """

    # validation
    if type(real_number) not in [float, int]:
        raise TypeError

    return "{:.{decimals}f}".format(real_number, decimals=precision)


def fixed_set_precision_float(real_number: float, precision: int):
    """ takes a @real_number and returns it with specified @precision

        return: float version of the number
    """

    return float(fixed_set_precision_str(real_number, precision))


def hex_to_int(hex_string: str):
    if not isinstance(hex_string, int):
        raise TypeError(f"{hex_string} should be type str.")

    return int(hex_string, 16)