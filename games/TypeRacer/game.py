
from core.system import *

try:
    import pynput
except ImportError:
    print("pynput not installed\ninstalling...")
    os.system("pip install pynput")


from pynput.keyboard import Key, Listener, KeyCode

# core
from core.aesthetics import *
from core.numbers__ import *

# python
import sys
import time
import threading
from random import choice

"""
typeracer formula:
    gross live wpm: ((total_correct_chars / 5) * 60 ) / time took to write that correct characters
    net live wpm: gross wpm - (incorrect characters written / current time)
    accuracy: (correct characters written / total characters in the text) * 100
"""

class CharacterInfo:
    def __init__(self, char, index, written_correct):
        self.char = char
        self.index = index
        self.written_correct = written_correct

    def __str__(self):
        content = f'({self.char}, {self.index}, {self.written_correct})'
        return content



texts = [
    'sometimes is fun to code because the entire game starts within the thinking',
    'being such an uneducated existence makes you cry everyday if you realise what you are...',
    'the error is between darkness and light.',
    # bigtext
]

incorrect_index = 0
incorrect_index_limit = 15
text = list(choice(texts))
text_copy = text.copy()
index = 0
correct_characters = []

wpm = 0
accuracy = 0.0
start_time = time.time()
current_time = None

active_game = False

character_infos = []

correct_counter = 0
incorrect_counter = 0

def FormatedText(text: list):
    content = '\n\n\t' + ''.join(text) + '\t\n\n'
    return content

def DisplayContent(mode: str='playing'):
    global wpm, accuracy, current_time, correct_characters, \
        incorrect_index, index, character_infos, incorrect_counter, \
        correct_counter
    clearscreen()

    formated_text = FormatedText(text)
    """
    if len(formated_text) > 50:
        i = 0
        while i < len(formated_text):
            sys.stdout.write(formated_text[i])
            if i % 50 == 0:
                sys.stdout.write('\n')
            i += 1
    """
    print(formated_text)

    if mode == 'playing':
        printing_index = index
        if index > 0:
            printing_index -= 1

        print(f'\nIndex: {index} \t\t\t\t\t {ConsoleColored("WPM: " + str(wpm), "yellow")}')
        print(f'Incorrect index: {incorrect_index}')
        print(f'Current char: \'{delete_ansi_codes(text[printing_index])}\'')
        if index < len(text):
            print(f'Next char: \'{delete_ansi_codes(text[index])}\'\n')
        else:
            print(f'Next char: \'\'\n')
        print(f'Corect characters inputed: {correct_counter}')
        print(f'Incorect characters inputed: {incorrect_counter}')
        print(f'\nTotal characters: {len(text)}')
        print(f'Total words: {len("".join(text).split())}\n')
        print('<insert>')

        """
        if index > 0:
            print(f'\nIndex: {index} \t\t\t\t\t {ConsoleColor("WPM: " + str(wpm), "yellow")}')
            print(f'Incorrect index: {incorrect_index}')
            print(f'Current char: \'{delete_ansi_codes(text[index - 1])}\'')
            if index < len(text):
                print(f'Next char: \'{delete_ansi_codes(text[index])}\'\n')
            else:
                print(f'Next char: \'\'\n')
            print(f'Corect characters: {len(correct_characters)}')
            print('insert:')
        elif index == 0:
            print(f'\nIndex: {0} \t\t\t\t\t {ConsoleColor("WPM: " + str(wpm), "yellow")}')
            print(f'Incorrect index: {incorrect_index}')
            print(f'Current char: \'\'')
            print(f'Next char: \'{delete_ansi_codes(text[index])}\'\n')
            print(f'Corect characters: {len(correct_characters)}')
            print('insert:')
        """
    #print(text)
    #print(correct_characters)
    #PrintCharInfos(character_infos)

def ContainsANSISeq(text: list):
    for index in range(len(text)):
        # here we find that the text contains ansi
        if text[index] != text_copy[index]:
            return True
    return False

def AlreadyExists(chars_infos: list, at_index: int):
    for charinfo_object in chars_infos:
        if charinfo_object.index == at_index:
            return True
    return False

def PrintCharInfos(char_infos):
    for charinfo_object in char_infos:
        print(charinfo_object, end=', ')
    print()

def VerifiyCorrectitude(keyboard_key):
    global index, text, incorrect_index, wpm, accuracy, \
        correct_characters, current_time, character_infos, \
        correct_counter, incorrect_counter
    if index <= len(text) - 1:
        # we have limit here, you can't type anymore if you typed 15 wrong chars
        if incorrect_index < incorrect_index_limit:
            if incorrect_index == 0:
                # if is space
                if text[index] == ' ':
                    # if yours is space (correct)
                    if keyboard_key == ' ':
                        if character_infos == []:
                            character_infos.append(CharacterInfo(text[index], index, True))
                        elif not AlreadyExists(character_infos, index):
                            character_infos.append(CharacterInfo(text[index], index, True))

                        correct_characters.append(text[index])
                        text[index] = ConsoleColored(' ', 'green', underlined=True)
                        correct_counter += 1
                    # (incorrect)
                    else:
                        if character_infos == []:
                            character_infos.append(CharacterInfo(text[index], index, False))
                        elif not AlreadyExists(character_infos, index):
                            character_infos.append(CharacterInfo(text[index], index, False))

                        text[index] = ansi_colored(0, 30, 41, " ")
                    incorrect_counter += 1
                    index += 1
                else:
                    # (correct)
                    if keyboard_key == text[index]:
                        if character_infos == []:
                            character_infos.append(CharacterInfo(text[index], index, True))
                        elif not AlreadyExists(character_infos, index):
                            character_infos.append(CharacterInfo(text[index], index, True))

                        correct_characters.append(text[index])
                        text[index] = ConsoleColored(text[index], 'green', underlined=True)
                        correct_counter += 1

                    # (incorrect)
                    elif keyboard_key != text[index]:
                        if character_infos == []:
                            character_infos.append(CharacterInfo(text[index], index, False))
                        elif not AlreadyExists(character_infos, index):
                            character_infos.append(CharacterInfo(text[index], index, False))

                        text[index] = ConsoleColored(text[index], 'red', underlined=True)
                        incorrect_index += 1
                        incorrect_counter += 1
                    index += 1

            # (incorrect)
            else:
                if character_infos == []:
                    character_infos.append(CharacterInfo(text[index], index, False))
                elif not AlreadyExists(character_infos, index):
                    character_infos.append(CharacterInfo(text[index], index, False))

                if text[index] == ' ':
                    text[index] = ansi_colored(0, 30, 41, " ")
                else:
                    text[index] = ConsoleColored(text[index], 'red', underlined=True)

                incorrect_counter += 1
                incorrect_index += 1
                index += 1

        now = time.time()
        current_time = now - start_time
        wpm = int(len(correct_characters) * 60 / 5 / current_time)
        DisplayContent()

        if index == len(text):
            # we have incorrect typed characters at the end
            if incorrect_index == 0:
                index -= 1
                return False

def KeyComparison(key: KeyCode):
    global text, index, incorrect_index, incorrect_index_limit, correct_characters
    if key == Key.up or key == Key.down or key == Key.right or key == Key.left:
        pass
    elif key == Key.ctrl or key == Key.ctrl_l or key == Key.ctrl_r:
        pass
    elif key == Key.shift:
        pass
    elif key == Key.esc:
        pass
    elif key == Key.enter:
        pass
    elif key == Key.backspace:
        if ContainsANSISeq(text):
            if index > 0:
                if text[index - 1].startswith(ansi_codes['red']) or \
                        text[index - 1].startswith('\x1b[0;30;41m'):
                    incorrect_index -= 1
                    if incorrect_index < 0:
                        incorrect_index = 0
                elif text[index - 1].startswith(ansi_codes['green']) or \
                        text[index - 1].startswith('\x1b[92m\x1b[4m'):
                    if correct_characters:
                        correct_characters.pop()
                text[index - 1] = delete_ansi_codes(text[index - 1])
                index -= 1
                DisplayContent()
            elif index == 0:
                if text[0].startswith(ansi_codes['red']) or \
                        text[0].startswith('\x1b[0;30;41m'):
                    incorrect_index = 0
                elif text[index - 1].startswith(ansi_codes['green']) or \
                        text[index - 1].startswith('\x1b[92m\x1b[4m'):
                    if correct_characters:
                        correct_characters.pop()
                text[0] = delete_ansi_codes(text[0])
                DisplayContent()

    elif key == Key.space:
        if incorrect_index < incorrect_index_limit:
            results = VerifiyCorrectitude(' ')
            if results == False:
                return False

    else:
        if incorrect_index < incorrect_index_limit:
            results = VerifiyCorrectitude(key.char)
            if results == False:
                return False

def ClearText(text: list):
    for i in range(len(text)):
        text[i] = delete_ansi_codes(text[i])

def ResetStats():
    global index, incorrect_index, wpm, accuracy, current_time, text, character_infos, correct_characters
    ClearText(text)
    index = 0
    incorrect_index = 0
    wpm = 0
    accuracy = 0.0
    current_time = None
    text = list(choice(texts))
    character_infos = []
    correct_characters = []
    active_game = False
    correct_counter = 0
    incorrect_counter = 0

def ComputeAccuracy(char_infos: list):
    correct_chars = 0
    for charinfo_object in char_infos:
        if charinfo_object.written_correct:
            correct_chars += 1
    return (correct_chars / len(text)) * 100.0

def PracticeTyperacing():
    global accuracy, correct_characters, text, start_time, character_infos, wpm, correct_counter, incorrect_counter, current_time
    clearscreen()
    ResetStats()
    start_time = time.time()
    active_game = True
    DisplayContent()

    game = Listener(on_press=KeyComparison)
    game.start()
    game.join()

    #accuracy = (len(correct_characters) / len(text)) * 100.0
    accuracy = ComputeAccuracy(character_infos)

    DisplayContent(mode='gameover')
    print('game over\n')
    print(f'WPM: {wpm}')
    print(f'Accuracy: {fixed_set_precision_str(accuracy, 2)}%\n')
    ResetStats()

    pauseprogram()