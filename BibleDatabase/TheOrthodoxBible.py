
from BibleDatabase.essentials import *
from BibleDatabase.functions import *
import requests
from bs4 import BeautifulSoup
import re
from collections import OrderedDict
from core.aesthetics import *
from datetime import datetime
import sys
from BibleDatabase.Bible import *

appname = \
"""
  _______ _             ____       _   _               _             ____  _ _     _
 |__   __| |           / __ \     | | | |             | |           |  _ \(_) |   | |
    | |  | |__   ___  | |  | |_ __| |_| |__   ___   __| | _____  __ | |_) |_| |__ | | ___
    | |  | '_ \ / _ \ | |  | | '__| __| '_ \ / _ \ / _` |/ _ \ \/ / |  _ <| | '_ \| |/ _ \\
    | |  | | | |  __/ | |__| | |  | |_| | | | (_) | (_| | (_) >  <  | |_) | | |_) | |  __/
    |_|  |_| |_|\___|  \____/|_|   \__|_| |_|\___/ \__,_|\___/_/\_\ |____/|_|_.__/|_|\___|
"""

class ConsoleInterface:
    def __init__(self):
        self.datetime_format = "\ncurrent datetime: %H:%M:%S - %d.%m.%Y\n"
        self.menuOptions = [
            "read from beginning",
            "read from where you left of",
            "select section to read",
            "{}".format(ConsoleColored("__EXIT__", "red"))
        ]
        self.bibleInterface = Bible()

    def run(self):
        clearscreen()
        self.MenuFunction()

    def DisplayInformation(self):
        print(ConsoleColored(appname, "yellow"), '\n')
        print(ConsoleColored('python script from =>', color='yellow', underlined=True))
        print(ConsoleColored('\t' + __file__, color='blue', underlined=True))
        print(ConsoleColored('running with interpreter =>', color='yellow', underlined=True))
        print(ConsoleColored('\t' + get_python_interpreter_path(), color='blue', underlined=True))
        print(datetime.now().strftime(self.datetime_format))

    def DisplayMenu(self):
        for index, option in enumerate(self.menuOptions[:len(self.menuOptions) - 1]):
            print(f"\t[ {underlined(str(index + 1))} ]. {option}")

        greenBracketLeft = ConsoleColored('\t[ ', 'green')
        greenBracketRight = ConsoleColored(' ]. ', 'green')
        redBracketLeft = ConsoleColored('\t[ ', 'red')
        redBracketRight = ConsoleColored(' ]. ', 'red')
        print(
            redBracketLeft + \
            ConsoleColored(str(len(self.menuOptions)), 'red', underlined=True) + \
            redBracketRight + self.menuOptions[len(self.menuOptions) - 1]
        )
        print()

    def GetSectionInPages(self):
        clearscreen()
        print()
        for index, sectionName in enumerate(bibleSectionsCollection):
            print(f'\t[ {index + 1} ]. ___{sectionName}___')
        print()
        userInput = input('choose bible section:\n')
        try:
            userInput = int(userInput)
        except ValueError:
            self.MenuFunction()
        pageIndex = 0
        for index, sectionName in enumerate(bibleSectionsCollection):
            if index + 1 == userInput:
                for page in self.bibleInterface.pages:
                    for pageLine in page:
                        if not isinstance(pageLine, list) and sectionName == pageLine:
                            return pageIndex
                    pageIndex += 1

    def MenuFunction(self):
        clearscreen()
        self.DisplayInformation()
        self.DisplayMenu()

        userInput = input('choose your action:\n')
        try:
            userInput = int(userInput)
            if userInput == 1:
                self.bibleInterface.ReadFromPoint(0)
                self.MenuFunction()
            elif userInput == 2:
                self.bibleInterface.ReadFromPoint(self.bibleInterface.lastPage)
                self.MenuFunction()
            elif userInput == 3:
                self.bibleInterface.ReadFromPoint(self.GetSectionInPages())
                self.MenuFunction()
            elif userInput == len(self.menuOptions):
                # exit the program or return to main menu
                return
            else:
                self.MenuFunction()
        except ValueError:
            if userInput == 'exit' or \
                    userInput == "EXIT" or \
                    userInput == 'return' or \
                    userInput == 'RETURN':
                return
            self.MenuFunction()
        sys.exit(0)

if __name__ == '__main__':
    app = ConsoleInterface()
    app.run()