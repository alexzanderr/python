
from core.aesthetics import *
from core.system import *
from core.path__ import *
from datetime import datetime
import sys, os

appname = \
            """
              _______               _____
             |__   __|             |  __ \
                | |_   _ _ __   ___| |__) |__ _  ___ ___ _ __
                | | | | | '_ \ / _ \  _  // _` |/ __/ _ \ '__|
                | | |_| | |_) |  __/ | \ \ (_| | (__  __/ |
                |_|\__, | .__/ \___|_|  \_\__,_|\___\___|_|
                    __/ | |
                   |___/|_|
            """

class ConsoleInterface:
    def __init__(self, appcolor: str):
        self.appcolor = appcolor
        self.datetime_format = "\ncurrent datetime: %H:%M:%S - %d.%m.%Y\n"
        self.menuOptions = list()
        self.menuOptions.append('Practice typing')
        self.menuOptions.append('Practice typing for eternity')
        self.menuOptions.append(ConsoleColored('__EXIT__', 'red'))

    def run(self):
        clearscreen()
        # UseProgressBar(70) not required necesarily
        # if you use a big application like tinder bot
        # and it needs a lot of time to load you can use this method
        self.MenuFunction()

    def DisplayInformation(self):
        print(ConsoleColored(appname, self.appcolor), '\n')
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

    def MenuFunction(self):
        clearscreen()
        self.DisplayInformation()
        self.DisplayMenu()

        action = input('choose your action:\n')
        try:
            action = int(action)
            if action == 1:
                from game import PracticeTyperacing
                PracticeTyperacing()
                self.MenuFunction()
            if action == 2:
                from game import PracticeTyperacing
                while True:
                    PracticeTyperacing()
            elif action == len(self.menuOptions):
                # exit the program or return to main menu
                return
            else:
                self.MenuFunction()
        except ValueError:
            if action == 'exit' or \
                    action == "EXIT" or \
                    action == 'return' or \
                    action == 'RETURN':
                return
            self.MenuFunction()
        sys.exit(0)

if __name__ == '__main__':
    app = ConsoleInterface('yellow')
    app.run()