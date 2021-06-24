

# core
from core.path__ import *
from core.audio__ import *
from core.symbols import *
from core.system import *
from core.aesthetics import *
from core.sounds.system.system import *
from core.sounds.vox.vox import *
from core.sounds.cs16.cs16 import *


# project
from LinuxTerminal.AsciiART import *


def Cowsay(content):
    message = "\n  " + "_" * len(content) + "__\n"
    message += " < " + content + " >\n"
    message += "  " + "-" * len(content) + "--"
    from random import choice
    message += ConsoleColored(cowsay, choice(['red', 'yellow', 'blue', 'green', 'purple']))
    return message


def VerifyExistenceInPath(currentWorkingPath, file):
    for f in os.listdir(currentWorkingPath):
        if f == file:
            return True
    return False

def MathExpression__(command):
    if command == "":
        return False

    operators = "+-*\\&^%~><.()"
    digits = "0123456789"

    in_digits = False
    in_operators = False
    other_charactes = []
    for character in command:
        if character in digits:
            in_digits = True
        elif character in operators:
            in_operators = True
        elif character == ' ':
            pass
        else:
            other_charactes.append(character)

    if in_digits and \
        in_operators and \
        len(other_charactes) == 0 \
        or "log" in command:
        return True
    return False

def ComputeMathExpression__(command):
    try:
        __formated = eval(command)
    except NameError as error:
        if "log" in str(error):
            from math import log, log10, log2
            __formated = eval(command)
        else:
            print(ConsoleColored("\n\tIncorrect math expression given.\n", 'red', bold=1))

    __formated = ConsoleColored(str(__formated), 'orange', bold=1)
    equal = ConsoleColored("=", "yellow", bold=1)
    print("\n\t{} {} {}\n".format(command, equal, __formated))

def PrintColored(item, color):
    if color in ['red', 'green', 'blue', 'yellow', 'fade']:
        if color == 'red':
            print(ConsoleColored(item, 'red'), '\n')
        elif color == 'green':
            print(ConsoleColored(item, 'green'), '\n')
        elif color == 'blue':
            print(ConsoleColored(item, 'blue'), '\n')

        elif color == 'fade':
            lines = []
            line = ""
            for character in item:
                if character == "\n":
                    lines.append(line)
                    line = ""
                else:
                    line += character

            from random import choice
            decision = choice([0, 1])

            if decision == 1:
                len_lines = len(lines)
                one_third = len_lines // 3
                if len_lines % 3 != 0:
                    one_third += 1

                for i in range(0, one_third):
                    print(ConsoleColored(lines[i], "purple"))
                for i in range(one_third, one_third * 2):
                    print(ConsoleColored(lines[i], "red"))
                for i in range(one_third * 2, len_lines):
                    print(ConsoleColored(lines[i], "yellow"))
                print()

            else:
                for i in range(len(lines)):
                    if i % 2 == 0:
                        print(ConsoleColored(lines[i], "red"))
                    elif i % 3 == 0:
                        print(ConsoleColored(lines[i], "yellow"))
                    else:
                        print(ConsoleColored(lines[i], "purple"))
            print()

        else:
            print(ConsoleColored(item, 'yellow'), '\n')
    else:
        print(ConsoleColored('Incorrect color given', 'red'), '\n')


def SizeBuiltIn(command):
    if command == "":
        return False

    __items = command.split()
    if len(__items) == 2:
        if __items[0] == "size":
            if os.path.isfile(__items[1]) or os.path.isdir(__items[1]):
                return True
            print(ConsoleColored("\npath provided is not valid\n", "red"))
    return False

def CheckTree__(command: str):
    if command == "":
        return False

    __items = command.split()
    if __items[0] != "tree":
        return False

    path = __items[1]
    if not os.path.isdir(path):
        return False

    if not os.path.exists(path):
        return False

    return True

def PrintTree__(command: str):
    folder = command.split()[1]
    folder = folder.split("\\")
    folder = folder[len(folder) - 1]
    print(ConsoleColored("\n" + folder, "cyan", bold=1, underlined=1))
    print(tree_representation(folder))
    print()

def Datetime__():
    from datetime import datetime
    date_time = datetime.now().strftime("%H:%M:%S-%d.%m.%Y")
    __items = date_time.split("-")

    timestr = __items[0]
    meridian = timestr.split(":")[0]
    meridian = "AM" if int(meridian) < 12 else "PM"
    meridian = ConsoleColored(meridian, "green", bold=1)
    datestr = __items[1]

    __items = [ConsoleColored(item, "yellow", bold=1) for item in timestr.split(":")]
    timestr = ConsoleColored(":", "red", bold=1).join(__items)

    __items = [ConsoleColored(item, "yellow", bold=1) for item in datestr.split(".")]
    datestr = ConsoleColored(".", "red", bold=1).join(__items)

    return {
        "date": datestr,
        "time": timestr,
        "meridian": meridian
    }

def PrintTime__(date_dict: dict, loop=0):
    _time = left_bracket_cyan + " " + date_dict["time"] + " " + date_dict["meridian"] + " " + right_bracket_cyan
    if loop:
        print("\t" + _time, end="\r")
    else:
        print("\n\t" + _time + "\n")

def PrintDate__(date_dict: dict):
    _date = "{} {} {}".format(left_bracket_cyan, date_dict["date"], right_bracket_cyan)
    print("\n\t{}\n".format(_date))

def PrintDatetime__(_datedict: dict):
    _time = _datedict["date"]
    _date = _datedict["time"]
    meridian = _datedict["meridian"]

    _datetime = f"{left_bracket_cyan} {_time} {right_bracket_cyan} {dash_orange} {left_bracket_cyan} {_time} {meridian} {right_bracket_cyan}"

    print("\n\t{}\n".format(_datetime))

def CDMinusMinus__(cwd):
    # root\\folder1\\folder2\\folder3
    cwd = cwd.split("\\")
    # because it ends with "\\" and split puts '' at final
    if len(cwd) > 2:
        cwd = "\\".join(cwd[:len(cwd) - 2]) + "\\"
    else:
        cwd = cwd[0] + "\\"
    return cwd

def PlayWindows98ErrorRemix__():
    playaudio(windows98_error())
    for _ in range(2):
        sleep(.2)
        playaudio(windows98_error())

    windows98_remix()
    print("\tcurrently playing - windows98-remix")

def FormatedListing__(commands: list):
    __formated = "\t"
    length = 0
    for command in commands:
        __formated += command + " | "
        length += len(command + " | ")
        if length > 70:
            __formated += "\n\t"
            length = 0
    return __formated[:len(__formated) - 3]

def ListDirectory__(__cwd):
    __contents = os.listdir(__cwd)
    # longest = max(map(len, __contents))
    if len(__contents) > 0:
        for __cont in __contents:
            __path = __cwd + __cont

            # is file
            if os.path.isfile(__path):
                __type = ConsoleColored("[__File__]", "cyan", bold=1)
                _type = "file"
                __ext = __path
                if __ext is None:
                    __ext = ""

            # is folder
            elif os.path.isdir(__path):
                __type = ConsoleColored("[__Folder__]", "yellow", bold=1)
                _type = "folder"
                __ext = ""

            # print[__Folder__]
            dim = 35
            if _type == "folder":
                __line = __type.ljust(dim - 5)
            else:
                __line = __type.ljust(dim)

            __line += __cont + " " + __ext
            print(__line)

    else:
        print("\t" + ConsoleColored("folder is empty.", "cyan", bold=1))

def DeleteFunction__(command: str, __cwd):
    __items = command.split()
    if len(__items) == 2:
        # deleting a full path file
        if os.path.isfile(__items[1]):
            print("\file {}".format(ConsoleColored(__items[1], "cyan", bold=1)))
            print(ConsoleColored("\tdeleted successfully.", "red", bold=1))
            os.remove(__items[1])

        # deleting a full path directory
        elif os.path.isabs(__items[1]):
            # directory has files or other dirs
            message = "\tAre you sure you want to delete this folder?\n"
            message += "\tthis folder {}\n".format(ConsoleColored(__items[1], "cyan", bold=1, underlined=1))
            message += "\t({}) or ({}) ?\n".format(ConsoleColored("(y)es", "red", bold=1), ConsoleColored("(n)o", "green", bold=1))

            decision = input(message)
            if decision == "y":
                os.system("rmdir /S /Q {}".format(__items[1]))
                print("\tfolder {}".format(ConsoleColored(__items[1], "cyan", bold=1)))
                print(ConsoleColored("\tdeleted successfully.", "red", bold=1))

        # deleting a folder or a file from current working dir
        else:
            found = 0
            contents = os.listdir(__cwd)
            if len(contents) > 0:
                for content in contents:
                    if __items[1] == content:
                        found = 1
                        break

                if found:
                    path = __cwd + __items[1]
                    message = "\tAre you sure you want to delete this item?\n"
                    message += "\tthis item {}\n".format(ConsoleColored(path, "cyan", bold=1, underlined=1))
                    message += "\t({}) or ({}) ?\n\t".format(ConsoleColored("(y)es", "red", bold=1), ConsoleColored("(n)o", "green", bold=1))

                    decision = input(message)
                    if decision == "y":
                        if os.path.isfile(path):
                            os.remove(path)
                        elif os.path.isdir(path):
                            os.rmdir(path)
                        print("\titem {}".format(ConsoleColored(path, "cyan", bold=1, underlined=1)))
                        print(ConsoleColored("\tdeleted successfully.", "red", bold=1))
                else:
                    print("\tyour requested item was not found.\n")
            else:
                print("\tyou folder is empty.\n")

def MakeFile__(__cwd="", __items=[], __help=0):
    if __help:
        message = \
        """
            built-in function mkfile

            usage:
                1. mkfile file_name.extension --content=test
                    or
                2. mkfile file_name --content=test
                    or
                3. mkfile root\\folder1\\folder2\\...\\file.extension --content=test
                    or
                4. mkfile root\\folder1\\folder2\\...\\file --content=test

            1. creates a file in current working directory
            2. same as 1, it is not a must to specify extension
            3. creates a file at specified folder path
            4. same as 2, it is not a must to specify extension

            --content is an optional parameter, it tells to the terminal
                to add this text to the file after creation
        """
        print(ConsoleColored(message, "yellow", bold=1))
    else:
        if os.path.isabs(__items[1]):
            with open(__items[1], "w+", encoding="utf-8") as file:
                file.truncate(0)
                print("\tfile with name: {} created successfully.\n".format(ConsoleColored(__items[1], "green", bold=1)))

                if len(__items) == 3:
                    __content = __items[2]
                    ___items = __content.split("=")
                    if ___items[0] == "--content":
                        file.write(___items[1])
                        print("\tand added text: {} to it.\n".format(ConsoleColored(___items[1], "green", bold=1)))
        else:
            found = 0
            __contents = os.listdir(__cwd)
            for _cont in __contents:
                if _cont == __items[1]:
                    found = 1
                    break

            if not found:
                path = __cwd + __items[1]
                with open(path, "w+", encoding="utf-8") as file:
                    file.truncate(0)
                    print("\tfile with name {} created successfully.\n".format(ConsoleColored(__items[1], "green", bold=1)))

                    if len(__items) == 3:
                        __content = __items[2]
                        ___items = __content.split("=")
                        if ___items[0] == "--content":
                            file.write(___items[1])
                            print("\tand added text: {} to it.\n".format(ConsoleColored(___items[1], "green", bold=1)))
            else:
                print("\tfile already exists!!\n")

def PythonInteractive__():
    print(ConsoleColored("\nPython {} {}".format(get_python_version(), "(tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32"), "yellow", bold=1))
    print(ConsoleColored('Type "help", "copyright", "credits" or "license" for more information.', "yellow", bold=1))

    while 1:
        inputprint = right_arrow_blue + right_arrow_yellow + right_arrow_blue + right_arrow_yellow + " "
        python_command = input(inputprint)

        if python_command == "":
            continue
        elif python_command == "exit":
            break
        else:
            try:
                exec(python_command)
                result = eval(python_command)
                if result != None:
                    print(result)
            except Exception as error:
                message = ConsoleColored("Traceback", "red", bold=1)
                message += ConsoleColored(" (most recent call last):\n", "yellow", bold=1)
                message += ConsoleColored("File \"", "yellow", bold=1) + ConsoleColored("<stdin>", "green", bold=1)
                message += ConsoleColored("\", line 1, in ", "yellow", bold=1) + ConsoleColored("<module>\n", "green", bold=1)

                error_name = str(type(error))
                index1 = error_name.find("'")
                index2 = error_name.find("'", index1 + 1)
                error_name = error_name[index1 + 1: index2]

                message += ConsoleColored(error_name, "blue", bold=1) + ConsoleColored(": ", "yellow", bold=1)
                message += ConsoleColored(str(error), "cyan", bold=1, underlined=1)
                print(message)

def MakeDir__(__cwd="", __items=[], __help=0):
    if __help:
        message = \
        """
            built-in function mkdir

            usage:
                1. mkdir folder_name
                    or
                2. mkdir root\\folder1\\folder2\\...\\folderN

            1. creates a folder in current working directory
            2. creates a folder at specified folder path
        """
        print(ConsoleColored(message, "yellow", bold=1))
    else:
        if os.path.isabs(__items[1]):
            os.mkdir(__items[1])
            print("directory at path: {}".format(ConsoleColored(__items[1], "cyan", bold=1, underlined=1)))
            print(ConsoleColored("\tcreated successfully.", "green", bold=1, underlined=1))
        else:
            exists = 0
            for content in os.listdir(__cwd):
                if __items[1] == content:
                    exists = 1
                    break

            if not exists:
                if " " not in __items[1]:
                    os.mkdir(__cwd + __items[1])
                    print("\tdirectory with name {} created successfully.\n".format(__items[1]))
                else:
                    print("\tinvalid name for dir")
            else:
                print("\tdirectory already exists.\n")

def ChangeDirectory__(__cwd, __items, __command):
    # case 1: cd and ..
    if __command == "cd.." or __items[1] == "..":
        return CDMinusMinus__(__cwd)

    # case 2: cd and absolute_folder
    elif os.path.isabs(__items[1]):
        if __items[1].lower() == "d:":
            __items[1] = "D:\\"
        elif __items[1].lower() == "c:":
            __items[1] = "C:\\"
        elif __items[1].lower() == "i:":
            __items[1] = "I:\\"

        dirs = __items[1].split("\\")
        dirs = list(filter(lambda x: x != "", dirs))
        return "\\".join(dirs) + "\\"

    # case 3: cd and folder in current working folder
    else:
        for content in os.listdir(__cwd):
            if os.path.isdir(__cwd + content) and \
                __items[1].lower() == content.lower():
                return __cwd + content + "\\"

        windows98_error()
        print(ConsoleColored("\tdirectory is invalid", "red", bold=1))