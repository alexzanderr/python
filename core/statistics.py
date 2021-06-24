
"""
    core/statistics.py

    its obvious what it is for

    author: @alexzander
"""


def average(*arguments):
    if len(arguments) == 0:
        raise ValueError
    if len(arguments) == 1:
        if type(arguments[0]) != list:
            raise TypeError

        total_sum = 0
        for item in arguments[0]:
            total_sum += item
        return total_sum / len(arguments[0])

    total_sum = 0
    occurrences = 0
    for arg in arguments:
        if type(arg) == int:
            total_sum += arg
            occurrences += 1
        elif type(arg) == list:
            total_sum += sum(arg)
            occurrences += len(arg)
        else:
            raise TypeError
    return total_sum / occurrences


def median(*arguments):
    if len(arguments) == 0:
        raise ValueError
    if len(arguments) == 1:
        if type(arguments) != list:
            raise TypeError

        if len(arguments[0]) % 2 == 0:
            # midlle index
            i = len(arguments[0]) // 2
            return (arguments[0][i] + arguments[0][i - 1]) / 2
        else:
            # middle element
            return arguments[0][len(arguments[0]) // 2]

    for arg in arguments:
        if type(arg) != int:
            raise TypeError

    if len(arguments) % 2 == 0:
        # middle index
        i = len(arguments) // 2
        return (arguments[i] + arguments[i - 1]) / 2
    else:
        # middle element
        return arguments[len(arguments) // 2]


def mode(*arguments):
    if len(arguments) == 0:
        raise ValueError
    if len(arguments) == 1:
        if type(arguments[0]) != list:
            raise TypeError
        frequencies = {arg: arguments[0].count(arg) for arg in arguments[0]}
        most_frequent = max(frequencies.values())

        if most_frequent == 1:
            return None

        chosenones = [k for k, v in frequencies.items() if v == most_frequent]
        return tuple(chosenones)

    for arg in arguments:
        if type(arg) != int:
            raise TypeError

    frequencies = {arg: arguments.count(arg) for arg in arguments}
    most_frequent = max(frequencies.values())

    if most_frequent == 1:
        return None

    chosenones = [k for k, v in frequencies.items() if v == most_frequent]
    return tuple(chosenones)


def variance(*arguments):
    if len(arguments) == 0:
        raise ValueError
    if len(arguments) == 1:
        if type(arguments[0]) != list:
            raise TypeError

        _average = average(arguments[0])
        sumation = 0
        for value in arguments[0]:
            sumation += (value - _average) ** 2
        return sumation / (len(arguments[0]) - 1)

    for arg in arguments:
        if type(arg) != int:
            raise TypeError

    _average = average(arguments)
    sumation = 0
    for value in arguments:
        sumation += (value - _average) ** 2
    return sumation / (len(arguments) - 1)


def standard_deviation(*arguments):
    if len(arguments) == 0:
        raise ValueError
    if len(arguments) == 1:
        if type(arguments[0]) != list:
            raise TypeError
        import math
        return math.sqrt(variance(arguments[0]))

    for arg in arguments:
        if type(arg) != int:
            raise TypeError
    return math.sqrt(variance(*arguments))


def coeff_of_variation(*arguments):
    return standard_deviation(*arguments) + average(*arguments)


def covariance(leftset, rightset):
    varleft = variance(leftset)
    varright = 0
    meanright = average(rightset)
    for item in rightset:
        varright += (item - meanright) ** 2
    return (varleft * varright) / (len(leftset) - 1)


def correl_coeff(leftset, rightset):
    leftsd = standard_deviation(leftset)
    rightsd = standard_deviation(rightset)
    return covariance(leftset, rightset) / (leftsd * rightsd)