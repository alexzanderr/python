
"""
    core/algorithms.py

    powerful module for algo

    here are a lot of functions
    that you can use in your math programs

    author: @alexzander
"""


# python
import math


def greatest_common_divisor(x, y):
    while y:
        x, y = y, x % y
    return x


def absolute_value(real_number):
    if type(real_number) != float and type(real_number) != float:
        raise TypeError("param @real_number should be int or float.")

    return -real_number if real_number < 0 else real_number


def is_perfect_square(integer):
    if type(integer) != int:
        raise TypeError("param @integer should be int.")
    return math.sqrt(integer) == math.floor(math.sqrt(integer))


def is_prime(integer):
    if type(integer) != int:
        raise TypeError("param @integer should be int.")

    if integer < 2:
        return False
    elif integer > 2 and integer % 2 == 0:
        return False
    else:
        for divisor in range(3, int(math.sqrt(integer))):
            if integer % divisor == 0:
                return False
    return True


def factorial_recursive(integer):
    if type(integer) != int:
        raise TypeError("param @integer should be int.")

    if integer == 0:
        return 1
    return integer * factorial_recursive(integer - 1)


def factorial_iterative(integer):
    if type(integer) != int:
        raise TypeError("param @integer should be int.")

    computation = 1
    for value in range(2, integer):
        computation *= value

    return computation


def factorization(integer):
    """ returns a list with prime factors """
    if type(integer) != int:
        raise TypeError("param @integer should be int.")

    prime_factors = []
    while integer % 2 == 0:
        prime_factors.append(2)
        integer //= 2

    divisor = 3
    while divisor * divisor <= integer:
        while integer % divisor == 0:
            prime_factors.append(divisor)
            integer //= divisor

        divisor += 2
    if integer > 2:
        prime_factors.append(integer)

    return prime_factors


def reversed_number(integer):
    if type(integer) != int:
        raise TypeError("param @integer should be int.")

    reversed_number = 0
    while integer:
        reversed_number = reversed_number * 10 + integer % 10
        integer //= 10

    return reversed_number


def is_palindrome(integer):
    if type(integer) != int:
        raise TypeError("param @integer should be int.")

    return integer == reversed_number(integer)


def divisor_sum(integer):
    if type(integer) != int:
        raise TypeError("param @integer should be int.")

    import math

    computation = 0
    for divisor in range(1, int(math.sqrt(integer)) + 1):
        computation += divisor + integer // divisor

    if is_perfect_square(integer):
        computation -= math.sqrt(integer)

    return computation


def sieve_eratosthenes(dimension):
    if type(dimension) != int:
        raise TypeError("param @dimension should be int.")

    if dimension <= 1:
        raise ValueError("param @dimension cannot be <= 1")

    sieve = [1] * dimension
    sieve[0] = sieve[1] = 0

    import math
    for i in range(2, int(math.sqrt(dimension)) + 1):
        if sieve[i] == 1:
            for j in range(dimension + 1):
                expression = i ** 2 + j * i
                if expression < dimension:
                    sieve[expression] = 0
    primes = []
    for i in range(len(sieve)):
        if sieve[i]:
            primes.append(i)
    return primes


def power(base, exponent):
    if type(base) != int:
        raise TypeError("param @base should be int.")

    if type(exponent) != int:
        raise TypeError("param @exponent should be int.")

    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)

    calculation = 1
    for _ in range(exponent):
        calculation *= base
    return calculation


def compute_determinant(matrix):
    """ @matrix should be list of lists. """
    if type(matrix) != list:
        raise TypeError("param @matrix should be list of lists.")

    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        computation = 0
        for i in range(len(matrix)):
            minor_determinant = []
            for j in range(1, len(matrix)):
                minor_determinant.append([matrix[j][k] for k in range(len(matrix)) if k != i])

            computation += matrix[0][i] * (power(-1, i + 2)) * compute_determinant(minor_determinant)
        return computation


def anagram(str1ng, str2ng):
    if type(str1ng) != str:
        raise TypeError("param @w1 should be str.")

    if type(str2ng) != str:
        raise TypeError("param @w2 should be str.")

    frequency_str1ng = {}
    for character in str1ng:
        frequency_str1ng[character] = frequency_str1ng.get(character, 0) + 1

    frequency_str2ng = {}
    for character in str2ng:
        frequency_str2ng[character] = frequency_str2ng.get(character, 0) + 1

    return frequency_str1ng == frequency_str2ng


def is_corect_parantheses(pattern):
    """ "{[()[]()]}" returns True. """
    if type(pattern) != str:
        raise TypeError("param @pattern should be str.")

    stack = []
    mapped = {")":"(", "]":"[", "}":"{"}
    for character in pattern:
        if character in mapped:
            if stack:
                top_element = stack.pop()
            else:
                top_element = "#"

            if mapped[character] != top_element:
                return False
        else:
            stack.append(character)

    return True if stack else False


def quicksort(array, left, right, reverse=False):
    """ sorts the array in-place. """
    i = left
    j = right
    pivot = array[(left + right) >> 1]

    while i <= j:
        if reverse:
            while array[i] > pivot:
                i += 1
            while array[j] < pivot:
                j -= 1
        else:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if left < j:
        quicksort(array, left, j, reverse)
    if i < right:
        quicksort(array, i, right, reverse)


def quicksorted(array, reverse=False):
    """ returns a sorted copy of initial array. """
    if type(array) != list:
        raise TypeError("param @array should be list.")
    if type(reverse) != bool:
        raise TypeError("param @reverse should be bool.")

    new_array = array.copy()
    quicksort(array, 0, len(new_array) - 1, reverse)
    return new_array


def mergesort(array):
    if len(array) > 1:
        half = len(array) >> 1

        arr1 = array[:half]
        arr2 = array[half:]

        mergesort(arr1)
        mergesort(arr2)

        i = 0
        j = 0
        k = 0
        len_arr1 = len(arr1)
        len_arr2 = len(arr2)

        while i < len_arr1 and j < len_arr2:
            if arr1[i] < arr2[j]:
                array[k] = arr1[i]
                i += 1
            else:
                array[k] = arr2[j]
                j += 1
            k += 1

        for t in range(i, len_arr1):
            array[k] = arr1[t]
            k += 1

        for t in range(j, len_arr2):
            array[k] = arr2[t]
            k += 1


def mergesorted(array, reverse=False):
    new_array = array.copy()
    mergesort(new_array)
    if reverse:
        return list(reversed(new_array))
    return new_array


def binarysearch(array, element):
    """ returns index of found element """

    # validation
    if type(array) != list:
        raise TypeError("param @array should be list.")
    if type(element) != int:
        raise TypeError("param @element should be int.")

    left = 0
    right = len(array) - 1
    while left <= right:
        index = (left + right) >> 1
        if array[index] == element:
            return index
        elif array[index] > element:
            right = index - 1
        else:
            left = index + 1

    # no element found
    return -1


def binary_repr(self, integer):
    """ returns an aesthetic representaion of binary version of the transmited number. """

    # validation
    if type(integer) != int:
        raise TypeError("param @integer should be int.")

    binaryv = bin(integer)
    byte = [0 for _ in range(8)]
    index_byte = len(byte) - 1
    index_bin = len(binaryv) - 1

    for _ in range(len(binaryv)):
        if binaryv[index_bin] == "1":
            byte[index_byte] = 1
        elif binaryv[index_bin] == "b":
            break
        index_bin -= 1
        index_byte -= 1

    # print("Binary representation: {}(base 10) ----> {}(base 2)".format(number, byte))
    fill = ""
    result = ['' for _ in range(len(str(integer)))]
    for char in result:
        fill += char

    str_byte = "[ "
    for b in byte:
        str_byte += str(b) + " "
    str_byte += "]"

    indexes = [i for i in range(7, -1, -1)]
    str_indexes = "[ "
    for i in indexes:
        str_indexes += str(i) + " "
    str_indexes += "]"

    print("{:=^25}".format("BinaryRepr"))
    print("{} : {}".format(integer, str_byte))
    print("{} : {}".format(fill, str_indexes))
    print("=" * 25)


def subsets(instance):
    if type(instance) != set:
        raise TypeError("param @instance should be set.")

    import itertools
    result = []
    for counter in range(len(instance) + 1):
        combinations = itertools.combinations(instance, counter)
        for comb in combinations:
            result.append(set(comb))
    return result


def digit_to_word(digit):
    if type(digit) != int and type(digit) != str:
        raise TypeError("param @digit should be int or str.")

    if digit == "0" or digit == 0:
        return "zero"
    elif digit == "1" or digit == 1:
        return "one"
    elif digit == "2" or digit == 2:
        return "two"
    elif digit == "3" or digit == 3:
        return "three"
    elif digit == "4" or digit == 4:
        return "four"
    elif digit == "5" or digit == 5:
        return "five"
    elif digit == "6" or digit == 6:
        return "six"
    elif digit == "7" or digit == 7:
        return "seven"
    elif digit == "8" or digit == 8:
        return "eight"
    elif digit == "9" or digit == 9:
        return "nine"

    raise ValueError("a number with total digits bigger than 9 was given/")


def tenth_to_word(tenth):
    if type(tenth) != int and type(tenth) != str:
        raise TypeError("param @digit should be int or str.")
    if len(tenth) != 2:
        raise ValueError("param @tenth shuld have length of 2.")

    if tenth[0] == "1":
        if tenth[1] == "0":
            return "ten"
        elif tenth[1] == "1":
            return "eleven"
        elif tenth[1] == "2":
            return "twelve"
        elif tenth[1] == "3":
            return "thirteen"
        elif tenth[1] == "4":
            return "fourteen"
        elif tenth[1] == "5":
            return "fithteen"
        elif tenth[1] == "6":
            return "sixteen"
        elif tenth[1] == "7":
            return "seventeen"
        elif tenth[1] == "8":
            return "eighteen"
        elif tenth[1] == "9":
            return "nineteen"

    elif tenth[0] == "2":
        if tenth[1] == "0":
            return "twenty"
        else:
            return "twenty-" + digit_to_word(tenth[1])
    elif tenth[0] == "3":
        if tenth[1] == "0":
            return "thirty"
        else:
            return "thirty-" + digit_to_word(tenth[1])
    elif tenth[0] == "4":
        if tenth[1] == "0":
            return "forty"
        else:
            return "forty-" + digit_to_word(tenth[1])
    elif tenth[0] == "5":
        if tenth[1] == "0":
            return "fifty"
        else:
            return "fifty-" + digit_to_word(tenth[1])
    elif tenth[0] == "6":
        if tenth[1] == "0":
            return "sixty"
        else:
            return "sixty-" + digit_to_word(tenth[1])
    elif tenth[0] == "7":
        if tenth[1] == "0":
            return "seventy"
        else:
            return "seventy-" + digit_to_word(tenth[1])
    elif tenth[0] == "8":
        if tenth[1] == "0":
            return "eighty"
        else:
            return "eighty-" + digit_to_word(tenth[1])
    elif tenth[0] == "9":
        if tenth[1] == "0":
            return "ninety"
        else:
            return "ninety-" + digit_to_word(tenth[1])


def number_to_words(integer):
    if type(integer) != int:
        raise TypeError("param @interger should be int.")

    amplifiers = ["quadrillion", "trillion", "billion", "million", "thousand", ""]

    digits_rev = list(str(integer))[::-1]
    index = 3
    while index <= len(digits_rev):
        digits_rev.insert(index, "/")
        index += 4

    digits_rev.reverse()
    digits_rev = "".join(digits_rev).split("/")

    if digits_rev[0] == "":
        del digits_rev[0]

    print(digits_rev)
    number_name = ""
    for amp, group in zip(amplifiers[::-1], digits_rev[::-1]):
        if len(group) == 3:
            first = group[0]
            second = group[1]
            third = group[2]

            if first == "0" and second == "0" and third == "0":
                group_name = ""
            else:
                if first == "0" and second != "0" and third != "0":
                    group_name = tenth_to_word(second + third) + " " + amp
                elif first == "0" and second == "1" and third == "0":
                    group_name = tenth_to_word(second + third) + " " + amp
                elif first == "0" and second == "0" and third != "0":
                    group_name = digit_to_word(third) + " " + amp
                else:
                    group_name = digit_to_word(first) + " hundred"
                    if second == "0" and third != "0":
                        group_name += " " + digit_to_word(third)
                    else:
                        group_name += " " + tenth_to_word(second + third)
                    group_name += " " + amp
        elif len(group) == 2:
            group_name = tenth_to_word(group) + " " + amp
        elif len(group) == 1:
            group_name = digit_to_word(group) + " " + amp
        number_name = group_name + " " + number_name

    return number_name


def collection_depth(__collection):
    if isinstance(__collection, list):
        if __collection == []:
            return 0
        else:
            return 1 + max(map(collection_depth, __collection))

    elif isinstance(__collection, dict):
        if __collection == {}:
            return 0
        else:
            return 1 + max(map(collection_depth, __collection))
    return 0



# """
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1
# """

# dim = 3
# sol = [0] * dim
# pos = 0

# def Succesor():
#     if sol[pos] < dim:
#         sol[pos] += 1
#         return True
#     return False

# def Valid():
#     for i in range(pos):
#         if sol[i] == sol[pos]:
#             return False
#     return True

# while pos > -1:
#     succ = Succesor()
#     while succ and not Valid():
#         succ = Succesor()
#     if succ:
#         if dim - 1 == pos:
#             print(sol)
#         else:
#             pos += 1
#             sol[pos] = 0
#     else:
#         pos -= 1


def CombinationsFromNumber(dim, k):
    """
        this is old method of using
        backtracking for generating all
        combiations

        returns a list with all combinations
    """
    dim = 10
    k = 2
    pos = 0
    sol = [0] * dim # [0, 0, 0, 0, 0, 0, 0, 0, 0]
    solutions = []

    def Init():
        if pos == 0:
            sol[0] = 0
        else:
            sol[pos] = sol[pos - 1]

    def Succesor():
        if sol[pos] < dim:
            sol[pos] += 1
            return True
        return False

    def Valid():
        for i in range(pos):
            if sol[i] == sol[pos]:
                return False
        return True

    while pos > - 1:
        succ = Succesor()
        while succ and not Valid():
            succ = Succesor()
        if succ:
            if k - 1 == pos:
                # print(sol[:k])
                solutions.append(sol[:k])
            else:
                pos += 1
                Init()
        else:
            pos -= 1
    return solutions