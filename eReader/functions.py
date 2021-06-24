
"""
    Functions used in this entire project.
"""

from collections import OrderedDict
from eReader.essentials import *

def DisplayEBookStats(eBookStats: OrderedDict):
    """
        Just displaying the main dict in an aesthetic form
        :param eBookStats:
        :return:
    """
    for dictKey in eBookStats:
        if type(dictKey) == int:
            for specsKey in eBookStats[dictKey]:
                if specsKey == 'content':
                    print(f'eBookStats[{dictKey}][\'{specsKey}\'] is too big to display.')
                else:
                    print(f'{specsKey} => {eBookStats[dictKey][specsKey]}')
            print('-----')
        else:
            print(f'{dictKey} => {eBookStats[dictKey]}')

def GetAuthor(bookNameAndAuthor: str):
    """
        Example >
        bookNameAndAuthor: 'The Cosmic Computer by Some Author'
        :return 'Some Author'
    """
    index = bookNameAndAuthor.index('by') + 3
    return bookNameAndAuthor[index:]

def GetBookName(bookNameAndAuthor: str):
    """
        Example >
        :param bookNameAndAuthor: 'Hacker Crackdown by Bruce Sterling'
        :return: 'Hacker Crackdown'
    """
    return bookNameAndAuthor[:bookNameAndAuthor.index('by') - 1]

def GetBookNameAndAuthorNameFromTitle(title: str):
    """
        Example >
        :param title: 'The Project Gutenberg EBook of Hacker Crackdown, by Bruce Sterling'
        :return: 'Hacker Crackdown by Bruce Sterling' (the book bookNameAndAuthor and authorName)
    """
    if ',' in title:
        title = title.replace(',', '')
    if '.' in title:
        title = title.replace('.', '')
    if ':' in title:
        title = title.replace(':', ',')
    return title[title.index('of') + 3:]

def CreateLinesListAndFormatedText(soupText: str, copyingMode=False):
    """
        :param soupText: the entire page text returned by BeautifulSoup

        :param copyingMode: used for just copying
            the entire text file to the attributes
            instead of creating them for the first time

        :return
            - lines list => used to store every line
                of the book from beginning to end
            - formatedText => a huge string that contains
                the entire book with lines  formated with number row
    """
    lines = list()
    line = ''
    index = 1
    formatedText = ''
    for character in soupText:
        if character != '\n':
            line += character
        elif character == '\n':
            if '\r' in line:
                # because it has an '\r' at the final
                line = line[:len(line) - 1]
            lines.append(line)
            if copyingMode:
                formatedText += line + '\n'
            else:
                formatedText += f'[ {index} ] =>\t\t{line}\n'
            index += 1
            line = ''
    return lines, formatedText

def CreateLinesFormatedList(linesList: list, copyingMode=False):
    """
        After creating the lines list and text_formated (huge string) we do this:
            creating a formated version of lines list called linesFormated

        :param linesList: the lines list created recently

        :param copyingMode: used for just copying the entire text file to the attributes
            instead of creating them for the first time

        :return: linesFormated list with every line modified with number row positioned
            to left of the line text
    """
    linesFormated = list()
    for index, line in enumerate(linesList):
        if copyingMode:
            linesFormated.append(line)
        else:
            linesFormated.append(f'[ {index + 1} ] =>\t\t{line}')
    linesFormated.append('__END__')
    return linesFormated

def GetRowNumber(formatedLine: str):
    """
        :param formatedLine: an element from the lines_formated list
            looks like this:
                '[ 1 ] => some text from the specified line

        This function is using regex to extract the '[ 1 ] =>'
            from the formated_line

        :return: its returning just the integer from '[ 1 ] =>' ===> 1
    """
    match = rowNumberRegex.match(formatedLine)
    if match is None:
        return -1
    return int(numberRegex.findall(match[0])[0])

def CreatePagesList(formatedLines: list, copyingMode=False):
    """
        :param formatedLines: the list created from the function:
            self.CreateLinesFormatedList

        :param copyingMode: used for just copying the entire text file to the attributes
            instead of creating them for the first time

        :return: a pages list storing a nested lists
            Example:
                pages: [
                    page_list1: [
                        line_list1:[
                            line: [
                                line_number,
                                formatedLine
                            ]
                        ],
                        ...,
                        line_listN: [
                            ...
                        ]
                    ],
                    ...,
                    page_listN: [
                        ....
                    ]
                ]
    """
    pages = list()
    page = list()
    index = 1
    for formatedLine in formatedLines:
        if index == 16 or formatedLine == '__END__':
            pages.append(page)
            index = 1
            page = list()
        number_row = GetRowNumber(formatedLine)
        if number_row:
            page.append([number_row, formatedLine])
        else:
            page.append(formatedLine)
        index += 1
    return pages

def CreateAttributes(soupText: str, copyingMode=False):
    """
        :param soupText: the page text returned from BeautifulSoup

        :param copyingMode: used for just copying the entire text file to the attributes
                instead of creating them for the first time

        :return: a tuple representing (
                lines,
                formatedText,
                formatedLines,
                pages
            )
    """
    lines, formatedText = CreateLinesListAndFormatedText(soupText, copyingMode)
    formatedLines = CreateLinesFormatedList(lines, copyingMode)
    pages = CreatePagesList(formatedLines)
    return lines, formatedText, formatedLines, pages