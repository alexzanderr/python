"""
    This file is used to store essential
        variables used in entire project.
"""
from bs4 import BeautifulSoup
from collections import OrderedDict
from string import Template
import re, os, requests
from BibleDatabase.functions import *
from core.path__ import *


numberRegex = re.compile(r'[0-9]+')
textRegex = re.compile(r'[a-zA-Z]+')

romanLiteral_I = re.compile(r'(I [a-zA-Z]+)')
romanLiteral_II = re.compile(r'(II [a-zA-Z]+)')
romanLiteral_III = re.compile(r'(III [a-zA-Z]+)')
romanLiteral_IV = re.compile(r'(IV [a-zA-Z]+)')

bibleSectionRegexStandard = re.compile(r'>[a-zA-Z]+ \([0-9]+\)<')
bibleSectionRegexRL_I = re.compile(r'>I [a-zA-Z]+ \([0-9]+\)<')
bibleSectionRegexRL_II = re.compile(r'>II [a-zA-Z]+ \([0-9]+\)<')
bibleSectionRegexRL_III = re.compile(r'>III [a-zA-Z]+ \([0-9]+\)<')
bibleSectionRegexRL_IV = re.compile(r'>IV [a-zA-Z]+ \([0-9]+\)<')

chapterRegex = re.compile(r'Cap\. [0-9]+')


biblePageURL = 'https://www.bibliaortodoxa.ro/cautare.php?text=&carte=25&volum='

userAgent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/79.0.3945.130 Safari/537.36"
}

# you have to replace $bookNumber with the corespondent bible section
bibleSectionURL = Template('https://www.bibliaortodoxa.ro/cautare.php?text=&carte=$bookNumber&volum=')

# database path
databasePath = r'BibleDatabase\database'


# files path
filesPath = r'BibleDatabase\files'

# this variable will be accessed in
# entire program during its existence
bibleSectionsStats = {
    "Facerea": {
        "id": 25,
        "versets": 1530,
    },
    "Iesirea": {
        "id": 32,
        "versets": 1211,
    },
    "Leviticul": {
        "id": 47,
        "versets": 857,
    },
    "Numerii": {
        "id": 59,
        "versets": 1286,
    },
    "Deuteronomul": {
        "id": 17,
        "versets": 951,
    },
    "Iosua Navi": {
        "id": 41,
        "versets": 654,
    },
    "Judecatori": {
        "id": 46,
        "versets": 586,
    },
    "Rut": {
        "id": 71,
        "versets": 85,
    },
    "I Regi": {
        "id": 66,
        "versets": 808,
    },
    "II Regi": {
        "id": 67,
        "versets": 691,
    },
    "III Regi": {
        "id": 68,
        "versets": 816,
    },
    "IV Regi": {
        "id": 69,
        "versets": 717,
    },
    "I Paralipomena": {
        "id": 14,
        "versets": 941,
    },
    "II Paralipomena": {
        "id": 15,
        "versets": 820,
    },
    "I Ezdra": {
        "id": 23,
        "versets": 280,
    },
    "Neemia": {
        "id": 58,
        "versets": 405,
    },
    "Esterei": {
        "id": 21,
        "versets": 168,
    },
    "Iov": {
        "id": 42,
        "versets": 1069,
    },
    "Psalmi": {
        "id": 65,
        "versets": 2552,
    },
    "Solomon": {
        "id": 74,
        "versets": 432,
    },
    "Ecclesiastul": {
        "id": 18,
        "versets": 221,
    },
    "Cantari": {
        "id": 9,
        "versets": 116,
    },
    "Isaia": {
        "id": 43,
        "versets": 1291,
    },
    "Ieremia": {
        "id": 20,
        "versets": 72,
    },
    "Plangeri": {
        "id": 64,
        "versets": 153,
    },
    "Iezechiel": {
        "id": 33,
        "versets": 1290,
    },
    "Daniel": {
        "id": 16,
        "versets": 357,
    },
    "Osea": {
        "id": 60,
        "versets": 195,
    },
    "Amos": {
        "id": 3,
        "versets": 146,
    },
    "Miheia": {
        "id": 56,
        "versets": 105,
    },
    "Ioil": {
        "id": 39,
        "versets": 73,
    },
    "Avdie": {
        "id": 6,
        "versets": 21,
    },
    "Iona": {
        "id": 40,
        "versets": 47,
    },
    "Naum": {
        "id": 57,
        "versets": 46,
    },
    "Avacum": {
        "id": 5,
        "versets": 56,
    },
    "Sofonie": {
        "id": 73,
        "versets": 53,
    },
    "Agheu": {
        "id": 2,
        "versets": 38,
    },
    "Zaharia": {
        "id": 82,
        "versets": 211,
    },
    "Maleahi": {
        "id": 52,
        "versets": 55,
    },
    "Tobit": {
        "id": 81,
        "versets": 247,
    },
    "Iudita": {
        "id": 45,
        "versets": 339,
    },
    "Baruh": {
        "id": 8,
        "versets": 140,
    },
    "3 tineri": {
        "id": 1,
        "versets": 67,
    },
    "III Ezdra": {
        "id": 24,
        "versets": 468,
    },
    "Ecclesiasticul": {
        "id": 72,
        "versets": 1532,
    },
    "Susanei": {
        "id": 75,
        "versets": 64,
    },
    "Istoria Balaurului": {
        "id": 7,
        "versets": 50,
    },
    "I Macabei": {
        "id": 49,
        "versets": 924,
    },
    "II Macabei": {
        "id": 50,
        "versets": 558,
    },
    "III Macabei": {
        "id": 51,
        "versets": 206,
    },
    "Manase": {
        "id": 54,
        "versets": 15,
    },
    "Matei": {
        "id": 55,
        "versets": 1071,
    },
    "Marcu": {
        "id": 53,
        "versets": 678,
    },
    "Luca": {
        "id": 48,
        "versets": 1151,
    },
    "Ioan": {
        "id": 35,
        "versets": 879,
    },
    "Faptele Apostolilor": {
        "id": 26,
        "versets": 1007,
    },
    "Romani": {
        "id": 70,
        "versets": 433,
    },
    "I Corinteni": {
        "id": 12,
        "versets": 437,
    },
    "II Corinteni": {
        "id": 13,
        "versets": 256,
    },
    "Galateni": {
        "id": 29,
        "versets": 148,
    },
    "Efeseni": {
        "id": 19,
        "versets": 155,
    },
    "Filipeni": {
        "id": 28,
        "versets": 104,
    },
    "Coloseni": {
        "id": 10,
        "versets": 95,
    },
    "I Tesaloniceni": {
        "id": 76,
        "versets": 89,
    },
    "II Tesaloniceni": {
        "id": 77,
        "versets": 47,
    },
    "I Timotei": {
        "id": 78,
        "versets": 113,
    },
    "II Timotei": {
        "id": 79,
        "versets": 83,
    },
    "Tit": {
        "id": 80,
        "versets": 46,
    },
    "Filimon": {
        "id": 27,
        "versets": 25,
    },
    "Evrei": {
        "id": 22,
        "versets": 303,
    },
    "Iacov": {
        "id": 30,
        "versets": 108,
    },
    "I Petru": {
        "id": 61,
        "versets": 105,
    },
    "II Petru": {
        "id": 62,
        "versets": 61,
    },
    "I Ioan": {
        "id": 36,
        "versets": 105,
    },
    "II Ioan": {
        "id": 37,
        "versets": 13,
    },
    "III Ioan": {
        "id": 38,
        "versets": 15,
    },
    "Iuda": {
        "id": 44,
        "versets": 25,
    },
    "Apocalipsa": {
        "id": 4,
        "versets": 405,
    },
}

def DisplayBibleSectionsCollection(bibleSectionsCollection: OrderedDict):
	for sectionName in bibleSectionsCollection:
		print(sectionName)
		for sectionKey in bibleSectionsCollection[sectionName]:
			print('\t' + sectionKey)
			if sectionKey == 'linesList':
				print(bibleSectionsCollection[sectionName]['linesList'])
			else:
				for contentTuple in bibleSectionsCollection[sectionName][sectionKey]:
					print('\t', contentTuple)
		print()

# the main collection where all its stored
bibleSectionsCollection = OrderedDict()

for index in range(len(bibleSectionsStats.keys())):
    files = os.listdir(databasePath + f'\\{index}')
    for file in files:
        if file != 'id.txt' and file != 'versets.txt':
            fileName = file
            break
    sectionName = get_file_name(fileName)
    bibleSectionsCollection[sectionName] = OrderedDict()
    bibleSectionsCollection[sectionName]['linesList'] = [sectionName]

    with open(databasePath + f'\\{index}\\{fileName}', 'r', encoding='utf-8') as bibleSectionFile:
        line = bibleSectionFile.readline()
        while line:
            if line != '__EOF__':
                line = line[:len(line) - 1]
                bibleSectionsCollection[sectionName]['linesList'].append(line)
            line = bibleSectionFile.readline()

    for formatedLine in bibleSectionsCollection[sectionName]['linesList']:
        if formatedLine != '':
            try:
                rowNumbers, lineContent = formatedLine.split('\t\t')
            except ValueError:
                pass
            else:
                if chapterRegex.match(lineContent):
                    lastChapter = lineContent
                    bibleSectionsCollection[sectionName][lastChapter] = list()
                else:
                    bibleLineNumber, bibleSectionLineNumber = numberRegex.findall(rowNumbers)
                    bibleSectionsCollection[sectionName][lastChapter].append(
                        (bibleLineNumber, bibleSectionLineNumber, lineContent))