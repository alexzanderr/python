
import sys
from BibleDatabase.essentials import *
from core.system import *
from pynput.keyboard import Listener, Key

class Bible:
    def __init__(self):
        self.bible = bibleSectionsCollection
        self.pages = CreateBiblePagesList(self.bible)
        self.lastPage = self.GetLastPage()
        if self.lastPage >= 0:
            self.ColorSavedLine(self.lastPage, 'save')
        else:
            raise IndexError('We cant find the last page where the user left of.')

    def GetLastLineFromFile(self):
        with open(filesPath + '\\lastLine.txt', 'r', encoding='utf-8') as lastLineFile:
            return int(lastLineFile.readline())

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

    def ReadFromPoint(self, pageIndex: int):
        """
            Activating a key listener on a separate thread
                to navigate through the ebook.
            Displaying the menu page and reading input.
            :param pageIndex:
            :return:
        """
        self.currentIndex = pageIndex
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
            if isinstance(pageLine, list):
                if line == pageLine[0]:
                    found = True
        return found

    def GetLastPage(self):
        """
            Getting the last page by getting the last from the file
                and searching into the pages array if exists
            :return: the last page eBookIndex if found else - 1
        """
        lastline = self.GetLastLineFromFile()
        for index in range(len(self.pages)):
            for pageline in self.pages[index]:
                if isinstance(pageline, list):
                    if pageline[0] == lastline:
                        return index
        return -1

    def ColorSavedLine(self, pageIndex: int, color: str):
        """
            We first eliminate the ANSI escape
                sequences and we color the line again with ANSI.

            :param pageIndex: current reading page
            :param color: what color to use
            :return:
        """
        lastline = self.GetLastLineFromFile()
        for index in range(len(self.pages[pageIndex])):
            if isinstance(self.pages[pageIndex][index], list):
                if self.pages[pageIndex][index][0] == lastline:

                    self.pages[pageIndex][index][2] = \
                        delete_ansi_escape_codes(
                        self.pages[pageIndex][index][2]
                    )

                    if color == 'white':
                        self.pages[pageIndex][index][2] = \
                            ConsoleColored(
                                self.pages[pageIndex][index][2],
                                "white"
                            )

                    elif color == 'save':
                        self.pages[pageIndex][index][2] = green_bold(self.pages[pageIndex][index][2])
                    
                    return

    def DisplaySavedLine(self):
        """
            Just printing the saved line.
            :return: nothing
        """
        print('you saved line:')
        for pageLine in self.pages[self.currentIndex]:
            if isinstance(pageLine, list):
                if pageLine[0] == self.lastLine:
                    print(pageLine[2])
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
        self.lastPage = self.GetLastPage()
        self.ColorSavedLine(self.lastPage, 'white')

        # before updating we have to color back to white the last line
        with open(filesPath + '\\lastLine.txt', 'w', encoding='utf-8') as lastLineFile:
            lastLineFile.truncate(0)
            lastLineFile.write(str(self.lastLine))

        self.lastPage = self.GetLastPage()

        self.ColorSavedLine(self.currentIndex, 'save')
        self.DisplaySavedLine()

        input(f'press [{ConsoleColored("ENTER", "red")}] to return')

    # aesthetics purpose only
    arrowsSize = 22
    pageArrowsLeft = '<' * arrowsSize
    pageArrowsRight = '>' * arrowsSize

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
        print(ConsoleColored('\t\tThe Orthodox Bible', 'yellow'))
        print(self.pageDelimiter * 2 + '=' * 15)
        print()
        for page_line in self.pages[index]:
            if isinstance(page_line, list):
                print(page_line[2])
            else:
                print(ConsoleColored(f'___{page_line}___', 'yellow'), '\n')
        print()
        print(self.pageDelimiter + \
              f'[{ConsoleColored("PAGE", "yellow")}][ {ConsoleColored(str(index + 1), "yellow", underlined=True)} ]' \
              + self.pageDelimiter)

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

if __name__ == '__main__':
    Bible()