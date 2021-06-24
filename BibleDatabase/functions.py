
from bs4 import BeautifulSoup
import requests, re
from collections import OrderedDict
from string import Template, ascii_lowercase, ascii_uppercase
from BibleDatabase.essentials import *
from core.aesthetics import *
from core.romania import *

numberRegex = re.compile(r'[0-9]+')
textRegex = re.compile(r'[a-zA-Z]+')

def TransformFromRomanianToEnglish(word: str):
    return ''.join([char if char not in letters_to_diacritics else letters_to_diacritics[char] for char in word])

def CreateBibleSectionsStatsDict(biblePageURL):
    """
        This function is accesing the web page and is
            extracting all the bible sections and total
            number of lines per sections at the same
            time with the id for that section.

        :param biblePageURL: url of the web page source
            from which we are extracting info

        :return: and OrderedDict containing every section
            with lines and ids
    """
    page = requests.get(biblePageURL)
    soup = BeautifulSoup(page.text, 'html.parser')

    bibleSections = soup.find('div', {'class': 'css_cautare_filtre'})
    bibleSections = [str(bibleSection) for bibleSection in list(bibleSections)[1:]]

    bibleSectionsStats = OrderedDict()
    for bibleSection in bibleSections:
        extractedSection = ''
        sectionIndex = bibleSection.index('volum=">') + len('volum=">')
        while sectionIndex < len(bibleSection):
            if bibleSection[sectionIndex] == '<':
                break
            extractedSection += bibleSection[sectionIndex]
            sectionIndex += 1

        sectionName = ''
        index = 0
        while index < len(extractedSection):
            if extractedSection[index] == '(':
                index += 1
                break
            sectionName += extractedSection[index]
            index += 1

        versetsNumber = ''
        while index < len(extractedSection):
            if extractedSection[index] == ')':
                break
            versetsNumber += extractedSection[index]
            index += 1

        sectionName = sectionName[:len(sectionName) - 1]
        sectionID = numberRegex.findall(bibleSection)[0]
        bibleSectionsStats[sectionName] = OrderedDict()
        bibleSectionsStats[sectionName]['id'] = sectionID
        bibleSectionsStats[sectionName]['versets'] = versetsNumber
    return bibleSectionsStats

def DisplayBibleSectionsStats(bibleSectionsStats: OrderedDict):
    """
        Just a sexy printing for the python
            dictionary variable format

        :param bibleSectionsStats: OrderedDict created
            in 'CreateBibleSectionsStatsDict' function

        :return: nothing
    """
    print('bibleSectionsStats = {')
    for bibleSectionKey in bibleSectionsStats:
        print(f'\t"{bibleSectionKey}": {{')
        print(f'\t\t"id": {bibleSectionsStats[bibleSectionKey]["id"]},')
        print(f'\t\t"versets": {bibleSectionsStats[bibleSectionKey]["versets"]},')
        print(f'\t}},')
    print('}')

def CreateLinesList(bibleText: str) -> list:
    lines = bibleText.split('\n')
    return lines[:len(lines) - 1]

def CreateDatabase():
    sectionCounter = 0
    totalLinesNumber = 1

    for sectionName in bibleSectionsStats:
        IDValue = bibleSectionsStats[sectionName]['id']

        page = requests.get(bibleSectionURL.safe_substitute(bookNumber=IDValue), headers=userAgent)
        soup = BeautifulSoup(page.text, 'html.parser')

        firstIndex = soup.text.index('Cap. 1')
        lastIndex = soup.text.index('Donatii BTC:')
        bibleText = soup.text[firstIndex : lastIndex].strip() + '\n'

        bibleSectionLines = CreateLinesList(bibleText)

        formatedBibleSectionLines = list()
        for lineNumber, line in enumerate(bibleSectionLines, start=1):
            formatedBibleSectionLines.append(f'[ {totalLinesNumber} ][ {lineNumber} ] =>\t\t' + line)
            totalLinesNumber += 1

        # creating the files
        path = databasePath + f'\\{sectionCounter}'
        os.mkdir(path)
        with open(path + f'\\{sectionName}.txt', 'w', encoding='utf-8') as bibleSectionFile:
            for formatedLine in formatedBibleSectionLines:
                bibleSectionFile.write(formatedLine + '\n')
            bibleSectionFile.write('__EOF__')

        with open(path + f'\\id.txt', 'w+', encoding='utf-8') as IDFile:
            IDFile.write(str(IDValue))

        with open(path + f'\\versets.txt', 'w+', encoding='utf-8') as versetsFile:
            versetsFile.write(str(bibleSectionsStats[sectionName]['versets']))

        sectionCounter += 1

def CreateBiblePagesList(bibleSectionsCollection: OrderedDict):
    pages = []
    page = []
    counter = 1
    linesCounter = 1
    for sectionName in bibleSectionsCollection:
        for line in bibleSectionsCollection[sectionName]['linesList']:
            if line != '':
                if '\t\t' in line:
                    lineNumber = int(numberRegex.findall(line.split('\t\t')[0])[1])
                    page.append([linesCounter, lineNumber, line])
                    counter += 1
                    if counter == 12:
                        pages.append(page)
                        page = []
                        counter = 1
                    linesCounter += 1
                else:
                    page.append(line)
    pages.append(page)
    return pages