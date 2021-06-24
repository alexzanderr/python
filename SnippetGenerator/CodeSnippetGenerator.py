
""" 
    python script made by Andrew Alexzander (dragonfire for nickname)
    
    this module auto generates a code snippet for vs code
        you enter the code in any language manually into a text file 
        and the program outputs & auto copies to clipboard the code 
        snippet json format for vs code 

    there are 2 dependecies import from andrew packages

    andrew_packages is a folder where its path is located to PYTHONPATH
    in your environment variables, if you dont have it there, put it there!

    RELEASE DATE: 20.05.2020
"""

import os

# pip install pyperclip
# or
# pip3 install pyperclip
# or
# python3 -m pip install pyperclip
import pyperclip, time
from core.system import *
from core.aesthetix import *

appname = \
"""
   _____       _                  _      _____                           _
  / ____|     (_)                | |    / ____|                         | |
 | (___  _ __  _ _ __  _ __   ___| |_  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __
  \___ \| '_ \| | '_ \| '_ \ / _ \ __| | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
  ____) | | | | | |_) | |_) |  __/ |_  | |__| |  __/ | | |  __/ | | (_| | |_ (_) | |
 |_____/|_| |_|_| .__/| .__/ \___|\__|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|
                | |   | |
                |_|   |_|
"""

source_code_format = \
"""INSERT SOURCE CODE BELOW
=====================================

=====================================
__EOF__"""

items_to_ignore = [
    "INSERT SOURCE CODE BELOW",
    "=====================================",
    "__EOF__"
]

def ContainsOnylWhites(line: str):
    for char in line:
        if char != " " or char != "\n" or char != "\t":
            return False
    return True

def PrintCodes(code_lines: list):
    for line in code_lines:
        print(line)
    print()

def ConvertToString(snippet: list):
    snippet_string = ""
    for i in range(len(snippet)):
        if isinstance(snippet[i], list):
            if i == len(snippet) - 1:
                snippet_string += ConvertToString(snippet[i])
            else:
                snippet_string += ConvertToString(snippet[i]) + "\n"
        else:
            if i == len(snippet) - 1:
                snippet_string += snippet[i]
            else:
                snippet_string += snippet[i] + "\n"
    return snippet_string
    
def ReplaceSpacesWithTabs(code_lines: list):
    """
        this function replaces every beginning
        spaces with tabs
        this action is repeated for every line
        in the source code
        
        Example: "        x = 3" 
        Returns => "\t\tx = 3"
    """
    replaced_version = code_lines.copy()
    for i in range(len(replaced_version)):
        if ContainsOnylWhites(replaced_version[i]):
            continue
        if replaced_version[i][0] == " ":
            index = 0
            total_tabs = 0
            while index < len(replaced_version[i]):
                index += 1
                if index % 4 == 0:
                    total_tabs += 1
                
                if index < len(replaced_version[i]) and replaced_version[i][index] != ' ':
                    break
            replaced_version[i] = replaced_version[i].strip()
            replaced_version[i] = ("\t" * total_tabs) + replaced_version[i]
    return replaced_version


def InsertQuotesFrontEnd(code_lines: list):
    """
        this function inserts quotes("") at
        beginning and end of a text
        
        we need these quotes in the source code
        lines to paste easily the snippet into
        JSON format
        
        this procedure is repeat for every source
        code line in the array
        
        Example: "\t\tx = 3"
        Return: "\"\t\tx=3\""
    """
    replaced_version = code_lines.copy()
    for i in range(len(replaced_version)):
        if i == len(replaced_version) - 1:
            replaced_version[i] = replaced_version[i][1: len(replaced_version[i]) - 1]
            replaced_version[i] = f"\"{replaced_version[i]}\""
        else:
            replaced_version[i] = replaced_version[i][1: len(replaced_version[i]) - 1]
            replaced_version[i] = f"\"{replaced_version[i]}\","
    return replaced_version

def ReadFromFile(path):
    code_lines = []
    with open(path, 'r+', encoding='utf-8') as file:
        line = file.readline()
        while line != '__EOF__':
            line = line[:len(line) - 1]
            if line not in items_to_ignore:
                code_lines.append(line)
            line = file.readline()
    return code_lines

def EscapeAllQuotes(text: str):
    items = list(text)
    index = 0
    while index < len(items):
        if items[index] == '"':
            items.insert(index, '\\')
            index += 1
        index += 1
    return "".join(items)

def CreateSnippet(source_code_path: str):
    """
        returns a string version of the code snippet
    """
    with open(source_code_path, 'w+', encoding='utf-8') as file:
        file.truncate(0)
        file.write(source_code_format)

    clearscreen()
    print(ConsoleColored(appname, "green"), '\n')

    while True:
        snippet_key_name = input("Enter code snippet key name:\n")
        prefix_name = input("Enter code snippet PREFIX name:\n")
        description = input("Enter description for snippet: (you can skip with enter):\n")
        decision = input("are you sure about these names? [y/n]:")

        if decision == 'y':
            break
        
    clearscreen()


    snippet = [
        f'"{snippet_key_name}": {{',
        f'\t"prefix": "{prefix_name}",',

    ]

    print("\nPlease insert your source code in this file!")
    os.system(f"{source_code_path}")

    print("\nProcessing code in 2 seconds...\n\n")
    time.sleep(2)

    # reading the codes
    body = ReadFromFile(source_code_path)

    # replacing the spaces with tabs
    body = ReplaceSpacesWithTabs(body)

    # replacing with representation
    for i in range(len(body)):
        if ContainsOnylWhites(body[i]):
            continue
        body[i] = body[i].__repr__()

    # escaping all quotes
    for i in range(len(body)):
        if '"' in body[i]:
            body[i] = EscapeAllQuotes(body[i])
    
    # inserting quotes at beginning and end 
    # to became in string form
    body = InsertQuotesFrontEnd(body)
    
    # adding tabs to correctly indent
    for i in range(len(body)):
        body[i] = "\t\t" + body[i]
    
    # insert essentials in body
    body.insert(0, "\t\"body\": [")
    body.append("\t],")
    
    # adding body to snipet
    snippet.append(body)
    
    # adding description
    if description != "":
        snippet.append(f'\t"description": "{description}"')
    else:
        snippet.append(f'\t"description": "None"')
    
    # adding curly bracket to the end
    snippet.append("},")
    
    # converting the snippet list type to string
    snippet_string = ConvertToString(snippet)
    return snippet_string

if __name__ == '__main__':
    source_code_path = '/SourceCode.txt'
    code_snippet = CreateSnippet(source_code_path)

    print("Here is your code snippet:\n")
    print(code_snippet, '\n')

    print(ConsoleColored("This code snippet has been copied to clipboard! :)", "green"))
    print(ConsoleColored("Dont worry copying this big text, you just have to paste it! :)", "green"))
    print(ConsoleColored("Enjoy!\n", "green"))

    pyperclip.copy(code_snippet)

    input("press <enter> to exit")
