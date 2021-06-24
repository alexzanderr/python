
import os
import re
import pyperclip
from core.aesthetics import *
from core.system import clearscreen, pauseprogram
from core.development import IntroductionMessage


def __converter(__input: str):
    __input = __input.strip()

    # remove \"  \"
    __input = __input.replace('"', "")

    # count \\ and /
    backslashes_total = __input.count("\\")
    slashes_total = __input.count("/")

    if backslashes_total > 0 and slashes_total == 0:
        __items = __input.split("\\")
        __items = [item for item in __items if item != ""]
        return "/".join(__items)

    elif backslashes_total == 0 and slashes_total > 0:
        __items = __input.split("/")
        __items = [item for item in __items if item != ""]
        return "\\".join(__items)

    elif backslashes_total == 0 and slashes_total == 0:
        return None
    else:
        # we have both \\ and /
        __items = re.findall("[a-zA-Z0-9]+", __input)
        return "/".join(__items)


def SlashConverter():
    clearscreen()
    IntroductionMessage("SlashConverter (\\\\) application")
    while 1:
        try:
            __input = input("\nenter PATH or CONTENT:\n{} ".format(green_bold(">>>")))
            if __input == "":
                continue

            result = __converter(__input)
            if result is None:
                continue

            pyperclip.copy(result)
            print("\n[\n\t{}\n]\n{}\n".format(yellow_bold(result), green_bold("copied to cliboard!")))

        except Exception as error:
            print(error)
            print(type(error))

            print()
            pauseprogram()



if __name__ == '__main__':
    SlashConverter()
