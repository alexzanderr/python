
from core.aesthetics import *
from core.system import *
from datetime import datetime
import sys, webbrowser, json

appname = \
                """
                 _                          _   _
                | |                        | | (_)
                | |__  _   _ ______ _ _ __ | |_ _  ___  _ __
                | '_ \| | | |_  / _` | '_ \| __| |/ _ \| '_ \\
                | |_) | |_| |/ / (_| | | | | |_| | (_) | | | |
                |_.__/ \__, /___\__,_|_| |_|\__|_|\___/|_| |_|
                        __/ |
                        |___/
                """


class ConsoleInterface:
    def __init__(self):
        self.database_json_path = "byzantion/database.json"
        self.datetime_format = "\ncurrent datetime: %H:%M:%S - %d.%m.%Y\n"
        self.database = json.loads(open(self.database_json_path).read())

    def DisplayStats(self):
        print(ConsoleColored(appname, "yellow"))
        print(ConsoleColored('python script from =>', color='yellow', underlined=True))
        print(ConsoleColored('\t' + __file__, color='blue', underlined=True))
        print(ConsoleColored('running with interpreter =>', color='yellow', underlined=True))
        print(ConsoleColored('\t' + get_python_interpreter_path(), color='blue', underlined=True))
        print(datetime.now().strftime(self.datetime_format))

    def DisplayMenu(self):
        """ database is a list with dictionaries in format
            [
                {
                    "name": "$song_name",
                    "url": "$song_url"
                }
                ...
            ]
        """
        for index, songDICT in enumerate(self.database):
            print(f"[ {underlined(str(index + 1))} ]. {songDICT['name']}")
        left_bracket = ConsoleColored("[ ", "red")
        dimension = str(len(self.database) + 1)
        dimension = ConsoleColored(dimension, "red", underlined=True)
        right_bracket = ConsoleColored(" ]. ", "red")
        exit_red = ConsoleColored("__EXIT__", "red") + "\n"
        exit_option = left_bracket + dimension + right_bracket + exit_red
        print(exit_option)

    def OpenURL(self, index):
        if type(index) != int:
            raise TypeError("index parameter should be int.")

        for counter in range(1, len(self.database) + 1):
            if counter == index:
                webbrowser.open(self.database[index - 1]["url"])
                return

    def run(self):
        self.MenuFunction()

    def MenuFunction(self):
        clearscreen()
        self.DisplayStats()
        self.DisplayMenu()

        user_input = input('choose your action:\n')
        try:
            user_input = int(user_input)
            if 1 <= user_input < len(self.database):
                self.OpenURL(user_input)
                self.MenuFunction()
            elif user_input == len(self.database) + 1:
                # exit
                print("byzantion database was shut down.")
                return
            else:
                self.MenuFunction()
        except ValueError:
            if user_input == 'exit' or \
                    user_input == "EXIT" or \
                    user_input == 'return' or \
                    user_input == 'RETURN':
                return
            self.MenuFunction()
        sys.exit(0)

if __name__ == '__main__':
    app = ConsoleInterface()
    app.run()