
from eReader.functions import *
from eReader.essentials import *
from core.aesthetix import *

class CreateEBook:
    def __init__(self, identifier: int):
        """
            :param identifier: book id from gutenberg book webpage
            This __init__ is creating an http request to the page 'dev.gutenberg.org'
            and returning the entire page text into this code, using BeautifulSoup class
            Unfortunately we have multiple types of
                url format on which we can get a request
        """
        import requests
        from bs4 import BeautifulSoup
        self.identifier = identifier
        self.page = requests.get(urlFilesFormat.safe_substitute(id=self.identifier),
                                 headers=userAgent)

        #if self.page.status_code != 200:
        #    self.page = requests.get(urlCacheFormat.safe_substitute(id=identifier),
        #                             headers=userAgent)

        self.soup = BeautifulSoup(self.page.text, 'html.parser')

        self.bookNameAndAuthor = GetBookNameAndAuthorNameFromTitle(
            str(self.soup.find('title').next).strip()
        )

        self.lines, self.formatedText, self.formatedLines, self.pages = \
            CreateAttributes(self.soup.text)

        self.SaveEBookToFile()
        self.SaveBookNameAndAuthorToPythonFile()
        self.UpdateTotalEBooksLength()
        self.UpdateEBookStats()

    def SaveEBookToFile(self):
        """
            Just saving the txt file with the entire book scrapped from
                the dev.gutenberg.org, by opening a new file and writing line
                by line to the file.
            :return: nothing
        """
        path = eBooksPath + f"\\{eBookStats['total']}"
        os.mkdir(path)

        with open(path + '\\' + 'id.txt', 'w', encoding='utf-8') as idFile:
            idFile.truncate(0)
            idFile.write(str(self.identifier))

        with open(path + '\\' + 'lastLine.txt', 'w', encoding='utf-8') as lastLineFile:
            lastLineFile.truncate(0)
            lastLineFile.write('1')

        with open(path + '\\' + self.bookNameAndAuthor + '.txt', 'w', encoding='utf-8') as eBookFile:
            eBookFile.truncate(0)
            for formatedLine in self.formatedLines:
                if formatedLine != '__END__':
                    eBookFile.write(formatedLine + '\n')
            eBookFile.write('__EOF__')

    def SaveBookNameAndAuthorToPythonFile(self):
        """
            The function opens an existent python script which
                is used to store asciify versions of the book names.
            Also creates a asciify version of the new book and adds it
                to the python script.
            :param self.bookNameAndAuthor: 'The Cosmic Computer'
            :return: nothing, writes in the python script: Asciify('The Cosmic Computer')
        """

        with open(projectPath + '\\bookNames.py', 'a', encoding='utf-8') as bookNamesFile:
            print(self.bookNameAndAuthor)
            bookNameAndAuthorBigger = asciify(GetBookName(self.bookNameAndAuthor))
            bookNamesFile.write('\n')
            bookNamesFile.write(f'book_{eBookStats["total"]}_name = \\\n')
            bookNamesFile.write('"""\n')
            bookNamesFile.write(bookNameAndAuthorBigger + '\n')
            bookNamesFile.write('"""\n')

    def UpdateTotalEBooksLength(self):
        eBookStats['total'] += 1
        with open(totalEBooksAbsolutePath, 'w', encoding='utf-8') as totalEBooksFile:
            totalEBooksFile.truncate(0)
            totalEBooksFile.write(str(eBookStats['total']))

    def UpdateEBookStats(self):
        index = eBookStats['total'] - 1
        path = eBooksPath + f'\\{index}'
        eBookStats[index] = OrderedDict()
        eBookStats[index]['id'] = self.identifier
        eBookStats[index]['idAbsPath'] = path + r'\id.txt'
        eBookStats[index]['lastLine'] = 1
        eBookStats[index]['lastLineAbsPath'] = path + r'\lastLine.txt'
        eBookStats[index]['bookNameAndAuthor'] = self.bookNameAndAuthor
        eBookStats[index]['contentAbsPath'] =  path + '\\' + self.bookNameAndAuthor + '.txt'
        eBookStats[index]['content'] = GetEBookContentFromFile(path + '\\' + self.bookNameAndAuthor + '.txt')

# usage
if __name__ == '__main__':
    newbook = CreateEBook(27468)