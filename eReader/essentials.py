
"""
    Variables used in this entire project.
    Contains:
    - eBookStats => OrderedDict(), used for saving stats about every ebook
        - contains keys that represent every book bookNameAndAuthor
            at every key we have another OrderedDict() which contains
                stats about every book
                for example:
                    - an eBookIndex value
                    - an absolute path to the text
                        file that contains the book
                    - an absolute path to the text
                        file that conaints the last line where user left of
                    - a book id, which is used to identify the
                        books from the site: dev.gutenberg.org

    - a lot of paths for the specified specs

    - regexs for extracting the number row
"""

import re, os
from string import Template
from collections import OrderedDict
from core.system import *
from core.pathx import *

def GetNumberFromFile(absolute_path):
    return int(open(absolute_path, "r", encoding="utf-8").readline())
    
# this is the line formatter for my ebook
rowNumberRegex = re.compile('\[ [0-9]+ \] \=\>')

# just a simple regex for getting a number
numberRegex = re.compile('[0-9]+')


# we will replace $id with some integer number and we will get the html for that ebook
from eReader.project_imports import *
urlFilesFormat = Template(files_url)
urlCacheFormat = Template(cache_url)

# some paths to my specs
projectPath = 'eReader'
eBooksPath = projectPath + r'\ebooks'
totalEBooksAbsolutePath = eBooksPath + r'\total.txt'

# used for separating text in console
delimiter = '=' * 100


totalEBooks = GetNumberFromFile(totalEBooksAbsolutePath)

def GetEBookContentFromFile(eBookAbsolutePath: str):
    formatedText = ''
    with open(eBookAbsolutePath, 'r', encoding='utf-8') as eBookFile:
        line = eBookFile.readline()
        while line:
            if line != '__EOF__':
                formatedText += line
            line = eBookFile.readline()
    return formatedText


# a dictionary that contains book names as key and a dictionary at every book bookNameAndAuthor
# which contains its eBookIndex: [0, 1, 2, ...], book_abs_path, last_line_abs_path to the text file
# which contains the last line where the user left of and book id from the website
eBookStats = OrderedDict()
for eBookIndex in range(totalEBooks):
    eBookStats[eBookIndex] = OrderedDict()
    path = eBooksPath + f'\\{eBookIndex}'
    files = os.listdir(path)
    for file in files:
        absolutePath = path + '\\' + file
        if 'id' in file:
            eBookStats[eBookIndex]['id'] = GetNumberFromFile(absolutePath)
            eBookStats[eBookIndex]['idAbsPath'] = absolutePath
        elif 'lastLine' in file:
            eBookStats[eBookIndex]['lastLine'] = GetNumberFromFile(absolutePath)
            eBookStats[eBookIndex]['lastLineAbsPath'] = absolutePath
        else:
            eBookStats[eBookIndex]['bookNameAndAuthor'] = get_file_name(file)
            eBookStats[eBookIndex]['contentAbsPath'] = absolutePath
            eBookStats[eBookIndex]['content'] = GetEBookContentFromFile(absolutePath)

eBookStats['total'] = totalEBooks
del totalEBooks