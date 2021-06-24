
from core.system import *
from pynput.keyboard import Key, Listener
import sys
from eReader.functions import *
from eReader.essentials import *
from core.aesthetix import *

class eBook:
    """
        This class is used to store and have access
            to the text file where the ebook is located.
    """
    def __init__(self, eBookIndex):
        """
            :param eBookIndex: just the index my
                friend and the class will take care of
        """
        self.bookNameAndAuthor = eBookStats[eBookIndex]['bookNameAndAuthor']
        self.bookName = GetBookName(self.bookNameAndAuthor)
        self.authorName = GetAuthor(self.bookNameAndAuthor)
        self.eBookIndex = eBookIndex
        self.eBookAbsolutePath = eBookStats[eBookIndex]['contentAbsPath']
        self.lastLineAbsolutePath = eBookStats[eBookIndex]['lastLineAbsPath']
        self.bookIdAbsolutePath = eBookStats[eBookIndex]['idAbsPath']
        self.bookId = eBookStats[eBookIndex]['id']
        self.lastLine = eBookStats[eBookIndex]['lastLine']
        self.eBookContent = eBookStats[eBookIndex]['content']

        # creating attributes with the text copyed from the text file
        self.lines, self.formatedText, self.formatedLines, self.pages = \
            CreateAttributes(self.eBookContent, copyingMode=True)

        self.eBookMenuOptions = list()
        self.eBookMenuOptions.append('Read from beginning')
        self.eBookMenuOptions.append('Read from where you left of')
        self.eBookMenuOptions.append(ConsoleColored('__RETURN__', 'yellow'))
        self.eBookMenuOptions.append(ConsoleColored('__EXIT__', 'red'))

        lastPage = self.GetLastPage()
        if lastPage >= 0:
            self.ColorSavedLine(lastPage, 'save')
        else:
            raise IndexError('We cant find the last page where the user left of.')

    def GetLastLineFromFile(self):
        """
            :return: integer of the last line where the user left of
        """
        with open(self.lastLineAbsolutePath, 'r', encoding='utf-8') as lastLineFile:
            return int(lastLineFile.readline())

    def GetLastPage(self):
        """
            Getting the last page by getting the last from the file
                and searching into the pages array if exists
            :return: the last page eBookIndex if found else - 1
        """
        lastline = self.GetLastLineFromFile()
        for index in range(len(self.pages)):
            for pageline in self.pages[index]:
                if pageline[0] == lastline:
                    return index
        return -1

    def DisplayEBookMenu(self):
        """
            Displaying in an aesthetic mode to the user
        """
        for index, option in enumerate(self.eBookMenuOptions):
            print(f'\t[ {underlined(str(index + 1))} ]. {option}')
        print()

    # aesthetics purpose only
    arrowsSize = 22
    pageArrowsLeft = '<' * arrowsSize
    pageArrowsRight = '>' * arrowsSize

    def PagesMenu(self):
        """
            Displays the current page with prev and
                next button to iterate through the book.
            :return:
        """
        clearscreen()
        if self.currentIndex == -1:
            self.currentIndex = len(self.pages) - 1
        elif self.currentIndex == len(self.pages):
            self.currentIndex = 0
        self.DisplayPage(self.currentIndex)
        print(self.pageArrowsLeft + \
              f'= [{ConsoleColored("PREV", "yellow")}] ' + '=' * 29 + \
              f' [{ConsoleColored("NEXT", "yellow")}] =' + self.pageArrowsRight)
        print(self.pagesMenuINFO)

    def OnPressFunction(self, key):
        """
            Method used for the key listener
                to navigate prev or next through the ebook.
        """
        if key == Key.left:
            self.currentIndex -= 1
            self.PagesMenu()
        elif key == Key.right:
            self.currentIndex += 1
            self.PagesMenu()

    def InputLastLine(self):
        """
            Entering the last line from the
                keyboard where the user left of.
        """
        self.PagesMenu()
        line = input('\nenter line where you left:\n')
        try:
            line = int(line)
        except ValueError:
            if line == 'abort':
                return 'abort'
            elif line == 'exit' or line == 'EXIT':
                sys.exit(0)
            else:
                return
        return line

    def ValidateLine(self, line: int):
        """
            Checking if the user input is correct.
            :param line: current reading line
            :return:
        """
        if not line:
            return False
        found = False
        for pageLine in self.pages[self.currentIndex]:
            if line == pageLine[0]:
                found = True
        return found

    def DisplaySavedLine(self, ):
        """
            Just printing the saved line.
            :return: nothing
        """
        print('you saved line:')
        for pageLine in self.pages[self.currentIndex]:
            if pageLine[0] == self.lastLine:
                print(pageLine[1])
                return

    def ColorSavedLine(self, pageIndex: int, color: str):
        """
            We first eliminate the ANSI escape
                sequences and we color the line again with ANSI.

            :param pageIndex: current reading page eBookIndex
            :param color: what color to use
            :return:
        """
        lastline = self.GetLastLineFromFile()
        for index in range(len(self.pages[pageIndex])):
            if self.pages[pageIndex][index][0] == lastline:
                self.pages[pageIndex][index][1] = \
                    delete_ansi_escape_codes(
                    self.pages[pageIndex][index][1]
                )
                if color == 'white':
                    self.pages[pageIndex][index][1] = \
                        ConsoleColored(self.pages[pageIndex][index][1], "white")
                elif color == 'save':
                    self.pages[pageIndex][index][1] = green_bold(self.pages[pageIndex][index][1])

                return

    def SaveLastLine(self):
        """
            Just saving to the database where we left of by:
                - inputing the last line
                - validating it
                - getting last page
                - coloring the lastPage with white (back to normal)
                - deleting and updating the last line file with the last line
                - displaying the last line
                - and coloring the last line with red to identify the last line
            :return:
        """
        self.keyListener.stop()
        self.lastLine = self.InputLastLine()
        if self.lastLine == 'abort':
            return
        while not self.ValidateLine(self.lastLine):
            self.lastLine = self.InputLastLine()

        # we need to save the last line to a file
        lastPage = self.GetLastPage()
        self.ColorSavedLine(lastPage, 'white')

        eBookStats[self.eBookIndex]['lastLine'] = self.lastLine

        # before updating we have to color back to white the last line
        with open(self.lastLineAbsolutePath, 'w', encoding='utf-8') as lastLineFile:
            lastLineFile.truncate(0)
            lastLineFile.write(str(self.lastLine))

        self.ColorSavedLine(self.currentIndex, 'save')
        self.DisplaySavedLine()
        input(f'press [{ConsoleColored("ENTER", "red")}] to return')

    def ReadFrom(self, startIndex: int):
        """
            Activating a key listener on a separate thread
                to navigate through the ebook.
            Displaying the menu page and reading input.
            :param startIndex:
            :return:
        """
        self.currentIndex = startIndex
        self.keyListener = Listener(on_press=self.OnPressFunction)
        self.keyListener.start()
        self.pagesMenuINFO = f'<press [{ConsoleColored("ENTER", "red")}] to return>\n' \
                             f'<input [{ConsoleColored("s", "blue")}] or [{ConsoleColored("S", "blue")}] to save>'
        self.PagesMenu()
        userInput = input()  # we need to stop program flow for menu to be active
        if userInput == 's' or \
                userInput == 'S' or \
                '1s' in userInput or \
                's1' in userInput or \
                's' in userInput:
            self.SaveLastLine()
        # stopping it after returning to main menu
        self.keyListener.stop()

    def DisplayAsciifyEBookName(self):
        """
            Displaying asciify version of the book bookNameAndAuthor
                + authorName bookNameAndAuthor below.
            :return:
        """
        print('eBook =>')
        exec(f'from eReader.bookNames import book_{self.eBookIndex}_name')
        print(ConsoleColored(eval(f'book_{self.eBookIndex}_name'), 'yellow'))
        print('\t' * 10 + underlined('by ' + self.authorName))
        print()

    def EBookMenu(self):
        """
            - displaying book bookNameAndAuthor
            - displaying ebook menu
            - reading input to choose an action
            - validating and executing something
            - exiting if user choice is that
            :return: nothing
        """
        clearscreen()
        self.DisplayAsciifyEBookName()
        self.DisplayEBookMenu()

        decision = input('select your action:\n')
        try:
            decision = int(decision)
            if decision == 1:
                self.ReadFrom(0)
                self.EBookMenu()
            elif decision == 2:
                self.ReadFrom(self.GetLastPage())
                self.EBookMenu()
            elif decision == 3:
                return
            elif decision == 4:
                sys.exit(0)
            else:
                self.EBookMenu()
        except ValueError:
            if decision == 'exit' or decision == 'EXIT':
                sys.exit(0)
            self.EBookMenu()

    pageDelimiter = '=' * 40
    def DisplayPage(self, index: int):
        """
            - displaying the name and authorName
            - displaying the page
            - displaying the page eBookIndex
            :param index: eBookIndex of the current page
            :return:
        """
        if not (0 <= index < len(self.pages)):
            raise IndexError('Incorrect page number')
        print('eBook => ')
        print(f'\t{ConsoleColored(self.bookNameAndAuthor, "green", underlined=True)}')
        print(self.pageDelimiter * 2 + '=' * 15)
        print()
        for page_line in self.pages[index]:
            print(page_line[1])
        print()
        print(self.pageDelimiter + \
              f'[{ConsoleColored("PAGE", "yellow")}][ {ConsoleColored(str(index + 1), "yellow", underlined=True)} ]' \
              + self.pageDelimiter)

# usage
if __name__ == "__main__":
    book = eBook(0)
    book.EBookMenu()