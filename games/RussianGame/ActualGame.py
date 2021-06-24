
from collections import OrderedDict
from core.system import *
from random import choice
from core.aesthetics import *
from time import sleep

def DisplayDictionary(russianAlphabetDict: OrderedDict):
    print('russianAlphabetDict = {')
    for key in russianAlphabetDict:
        print(f"\t'{key}': '{russianAlphabetDict[key]}',")
    print('}')

russianSymbolsPronounciation = {
	'я': 'ia',
	'ш': 'şâi',
	'е': 'e',
	'р': 'r',
	'т': 't',
	'ы': 'â',
	'у': 'u',
	'и': 'i',
	'о': 'o',
	'п': 'p',
	'а': 'a',
	'с': 's',
	'д': 'd',
	'ф': 'f',
	'г': 'g',
	'ч': 'ce',
	'й': 'i',
	'к': 'k',
	'л': 'l',
	'э': 'ă',
	'х': 'h',
	'ц': 'ţ',
	'в': 'v',
	'б': 'b',
	'н': 'n',
	'м': 'm',
    'щ': 'sh',
    'ю': 'iu',
    'ж': 'j',
    'ь': '',
    'з': 'z',
    'ъ': '',
    'ё': 'io'
}

flagLine = '=' * 100
pronounciationLetters = list(russianSymbolsPronounciation.values())

def ArrangeRandomly(pronounciationLetters: list):
	randomly = []
	while pronounciationLetters:
		randomLetter = choice(pronounciationLetters)
		randomly.append(randomLetter)
		pronounciationLetters.remove(randomLetter)
	return randomly

def PlayGame():
	global pronounciationLetters
	clearscreen()
	print(flagLine)
	print(ConsoleColored(flagLine, 'blue'))
	print(ConsoleColored(flagLine, 'red'))
	print()
	russianCharacter = choice(list(russianSymbolsPronounciation.keys()))
	russianCharacterColored = ConsoleColored(f"'{russianCharacter}'", 'yellow')
	print(f'The russian blyat character: {russianCharacterColored}\n')

	pronounciationLetters = ArrangeRandomly(pronounciationLetters)
	counter = 1
	for index, letter in enumerate(pronounciationLetters, start=1):
		print(f'[ {index} ]. \'{letter}\'', end=' ')
		if counter % 7 == 0:
			print()
		counter += 1

	userInput = input('\n\nchoose the pronounciation of this russian blyat character:\n')
	try:
		userInput = int(userInput)
		chosenCharacter = pronounciationLetters[userInput - 1]
		if russianSymbolsPronounciation[russianCharacter] == chosenCharacter:
			print(ConsoleColored('Correct answer!!!', 'green'))
		else:
			print(ConsoleColored('Incorrect блять!!!', 'red'))
		sleep(1)
		PlayGame()
	except ValueError:
		if userInput == 'stop':
			return
		print(ConsoleColored('Incorrect input блять!!!', 'red'))
		sleep(0.5)

	PlayGame()