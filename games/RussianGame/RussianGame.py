
"""
    This is the main application where the actions happens
"""

from core.aesthetics import *
from core.system import *
from datetime import datetime
import sys, os
from ActualGame import *

appname = \
"""
  _____               _                _____
 |  __ \             (_)              / ____|
 | |__) |   _ ___ ___ _  __ _ _ __   | |  __  __ _ _ __ ___   ___
 |  _  / | | / __/ __| |/ _` | '_ \  | | |_ |/ _` | '_ ` _ \ / _ \\
 | | \ \ |_| \__ \__ \ | (_| | | | | | |__| | (_| | | | | | |  __/
 |_|  \_\__,_|___/___/_|\__,_|_| |_|  \_____|\__,_|_| |_| |_|\___|
"""

flagLine = '=' * 100

class ConsoleInterface:
    def __init__(self):
        self.datetime_format = "\ncurrent datetime: %H:%M:%S - %d.%m.%Y\n"
        self.menuOptions = [
            "{}".format(ConsoleColored('__PLAY__', 'green')),
            "{}".format(ConsoleColored('__EXIT__', 'red'))
        ]

    def run(self):
        clearscreen()
        self.MenuFunction()

    def DisplayInformation(self):
        print(ConsoleColored(appname, "yellow"))
        print(flagLine)
        print(flagLine)
        print(flagLine)
        print()
        print(ConsoleColored('python script from =>', color='yellow', underlined=True))
        print(ConsoleColored('\t' + __file__, color='blue', underlined=True))
        print(ConsoleColored('running with interpreter =>', color='yellow', underlined=True))
        print(ConsoleColored('\t' + get_python_interpreter_path(), color='blue', underlined=True))
        print(datetime.now().strftime(self.datetime_format))

    def DisplayMenu(self):
        greenBracketLeft = ConsoleColored('\t[ ', 'green')
        greenBracketRight = ConsoleColored(' ]. ', 'green')
        print(
            greenBracketLeft + \
            ConsoleColored('1', 'green', underlined=True) + \
            greenBracketRight + self.menuOptions[0]
        )

        redBracketLeft = ConsoleColored('\t[ ', 'red')
        redBracketRight = ConsoleColored(' ]. ', 'red')
        print(
            redBracketLeft + \
            ConsoleColored('2', 'red', underlined=True) + \
            redBracketRight + self.menuOptions[1]
        )
        print()

    def MenuFunction(self):
        clearscreen()
        self.DisplayInformation()
        self.DisplayMenu()

        userInput = input('choose your action:\n')
        try:
            userInput = int(userInput)
            if userInput == 1:
                PlayGame()
                self.MenuFunction()
            elif userInput == 2:
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