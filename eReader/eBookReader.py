
from datetime import datetime
from eReader.ebook import eBook
from eReader.createEBook import CreateEBook
from eReader.essentials import *
from eReader.functions import *
from core.system import *
from core.aesthetix import *
import threading, sys

appname = \
        """
               ____              _      _____                _           
              |  _ \            | |    |  __ \              | |          
           ___| |_) | ___   ___ | | __ | |__) |___  __ _  __| | ___ _ __ 
          / _ \  _ < / _ \ / _ \| |/ / |  _  // _ \/ _` |/ _` |/ _ \ '__|
         |  __/ |_) | (_) | (_) |   <  | | \ \  __/ (_| | (_| |  __/ |   
          \___|____/ \___/ \___/|_|\_\ |_|  \_\___|\__,_|\__,_|\___|_| 
        """

bookIdName = \
        """
          ____              _      _____    _ 
         |  _ \            | |    |_   _|  | |
         | |_) | ___   ___ | | __   | |  __| |
         |  _ < / _ \ / _ \| |/ /   | | / _` |
         | |_) | (_) | (_) |   <   _| |_ (_| |
         |____/ \___/ \___/|_|\_\ |_____\__,_|
        """

class ConsoleInterface:
    """
        This class is used as console
            interface for the application.
    """
    def __init__(self):
        """
            - creating datetime format
            - creating a dictionary with all the books from databse
            - adding __ADD__ button with adding a new book functionality
            - adding at the final exit button
            :param appColor: this color is used for :appName
        """
        self.datetimeFormat = "\ncurrent datetime: %H:%M:%S - %d.%m.%Y\n"

        self.eBooksDictMenu = OrderedDict()
        for dictKey in eBookStats:
            if type(dictKey) == int:
                self.eBooksDictMenu[dictKey] = eBook(dictKey)

        self.integerKeys = self.GetTotalIntegerKeys()

        self.eBooksDictMenu['add'] = ConsoleColored('__ADD__', 'green')
        self.eBooksDictMenu['exit'] = ConsoleColored('__EXIT__', 'red')

    def run(self):
        """ Running the application. """
        self.MenuFunction()

    def DisplayInformation(self):
        """
            - printing appName with color
            - printing python script path
            - printing python interpreter path
            - printing current time
            :return: nothing
        """
        print(ConsoleColored(appname, "green"), '\n')
        print(ConsoleColored('python script from =>', color='yellow', underlined=True))
        print(ConsoleColored('\t' + __file__, color='blue', underlined=True))
        print(ConsoleColored('running with interpreter =>', color='yellow', underlined=True))
        print(ConsoleColored('\t' + get_python_interpreter_path(), color='blue', underlined=True))
        print(datetime.now().strftime(self.datetimeFormat))

    def DisplayMenu(self):
        """
            - book0
            - book1
            ...
            - bookN
            - __ADD__
            - __EXIT__
            :return: nothing
        """
        for dictKey in self.eBooksDictMenu:
            if type(dictKey) == int:
                print(f'\t[ {underlined(str(dictKey + 1))} ]. {self.eBooksDictMenu[dictKey].bookNameAndAuthor}')

        greenBracketLeft = ConsoleColored('\t[ ', 'green')
        greenBracketRight = ConsoleColored(' ]. ', 'green')
        redBracketLeft = ConsoleColored('\t[ ', 'red')
        redBracketRight = ConsoleColored(' ]. ', 'red')
        print(
            greenBracketLeft + \
            ConsoleColored(str(self.integerKeys + 1), 'green', underlined=True) + \
            greenBracketRight + self.eBooksDictMenu['add']
        )
        print(
            redBracketLeft + \
            ConsoleColored(str(self.integerKeys + 2), 'red', underlined=True) + \
            redBracketRight + self.eBooksDictMenu['exit']
        )
        print()

    def MenuFunction(self):
        """
            cls()
            - printing appname, stats and menu
            - inputing user input
            - validating
            - accessing eBooks
            - adding new eBooks
            - exit
            :return: nothing
        """
        clearscreen()
        self.DisplayInformation()
        self.DisplayMenu()

        userInput = input('choose your action:\n')
        try:
            userInput = int(userInput)
            if 1 <= userInput <= self.integerKeys:
                ebook = eBook(userInput - 1)
                ebook.EBookMenu()
                del ebook
                self.MenuFunction()
            elif userInput == self.integerKeys + 1:
                self.AddNewBook()
                self.MenuFunction()
            elif userInput == self.integerKeys + 2:
                print("eBookReader app was shut down.")
                sys.exit(0)
            else:
                self.MenuFunction()
        except ValueError:
            if userInput == 'exit' or \
                    userInput == "EXIT" or \
                    userInput == 'return' or \
                    userInput == 'RETURN':
                print("eBookReader app was shut down.")
                return
            self.MenuFunction()
        sys.exit(0)

    def GetTotalIntegerKeys(self):
        result = 0
        for dictKey in self.eBooksDictMenu:
            if type(dictKey) == int:
                result += 1
        return result

    def AddNewBook(self):
        clearscreen()
        print('\n', ConsoleColored(bookIdName, "blue"), '\n')
        userInput = input('enter book id:\n')
        try:
            userInput = int(userInput)
            userDeicison = input('Are you sure you want to add this book? [y/n]:\n')
            if userDeicison == 'y':
                print('wait untill the process is finished...')
                newBook = CreateEBook(userInput)
                del newBook
                LoadProgressBar(1000)
                self.eBooksDictMenu[self.integerKeys] = eBook(self.integerKeys)
                self.integerKeys += 1
            elif userDeicison == 'n':
                return
            else:
                self.AddNewBook()
        except ValueError:
            if userInput == 'abort':
                return
            self.AddNewBook()

if __name__ == '__main__':
    app = ConsoleInterface()
    app.run()