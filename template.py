
import os
import sys
from core.system import *
from datetime import datetime
from core.aesthetics import *

appname = \
                """
                  _______                   _       _
                 |__   __|                 | |     | |
                    | | ___ _ __ ___  _ __ | | __ _| |_ ___
                    | |/ _ \ '_ ` _ \| '_ \| |/ _` | __/ _ \\
                    | |  __/ | | | | | |_) | | (_| | |_  __/
                    |_|\___|_| |_| |_| .__/|_|\__,_|\__\___|
                                     | |
                                     |_|
                """

class ConsoleInterface:
    def __init__(self):
        self.datetime_format = "\ncurrent datetime: %H:%M:%S - %d.%m.%Y\n"
        self.menuOptions = []
        self.menuOptions.append('first option')
        self.menuOptions.append('second option')
        self.menuOptions.append('third option')
        self.menuOptions.append(ConsoleColored('__EXIT__', 'red'))

    def run(self):
        clearscreen()
        # UseProgressBar(70) not required necesarily
        # if you use a big application like tinder bot
        # and it needs a lot of time to load you can use this method
        self.MenuFunction()

    def DisplayInformation(self):
        print(red_bold(appname))
        print(ConsoleColored('python script from =>', color='yellow', underlined=True))
        print(ConsoleColored('\t' + __file__, color='blue', underlined=True))
        print(ConsoleColored('running with interpreter =>', color='yellow', underlined=True))
        print(ConsoleColored("\t" + get_python_interpreter_path(), color='blue', underlined=True))
        print(datetime.now().strftime(self.datetime_format))

    def DisplayMenu(self):
        for index, option in enumerate(self.menuOptions[:len(self.menuOptions) - 1]):
            print(f"\t[ {underlined(str(index + 1))} ]. {option}")

        greenBracketLeft = ConsoleColored('\t[ ', 'green')
        greenBracketRight = ConsoleColored(' ]. ', 'green')
        redBracketLeft = ConsoleColored('\t[ ', 'red')
        redBracketRight = ConsoleColored(' ]. ', 'red')
        exit_option = redBracketLeft + \
            ConsoleColored(str(len(self.menuOptions)), 'red', underlined=True) + \
            redBracketRight + self.menuOptions[len(self.menuOptions) - 1]
        print(exit_option)

    def MenuFunction(self):
        clearscreen()
        self.DisplayInformation()
        self.DisplayMenu()

        action = input('\nchoose your action:\n')
        try:
            action = int(action)
            if action == 1:

                # load app

                self.MenuFunction()
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
    app = ConsoleInterface()
    app.run()