
# python
from time import sleep
from sys import exit

from core.aesthetics import *

# core
from core.system import *

# project
from LinuxTerminal.functions import *

# dragonfire
from getpass import getuser
username = ConsoleColored(getuser(), "green", bold=1)

# ASUSROGGL553VD
computer_name = ConsoleColored("ASUSROGGL553VD", "red", bold=1)

commands_json_path = "commands.json"

# ~
tilda = ConsoleColored('~', "blue", bold=1)

greenQuotationMark = ConsoleColored('"', 'green', bold=1)
ATSIGN = ConsoleColored('@', 'blue', bold=1)
blue_dollar_sign = ConsoleColored('$', 'blue', bold=1)

left_bracket_blue = ConsoleColored("[", "blue", bold=1)
right_bracket_blue = ConsoleColored("]", "blue", bold=1)
right_bracket_green = ConsoleColored("]", "green", bold=1)
arrows = ConsoleColored(">>>", "green", bold=1)

clear_screen()
print(ConsoleColored(alexzander, "green"))
print(ConsoleColored(terminal, "green"), '\n')

CommandsHistoryJSON = read_json_from_file(commands_json_path)

def UpdateCommandsHistory(command):
    global CommandsHistoryJSON
    if command not in CommandsHistoryJSON:
        CommandsHistoryJSON.append(command)
        write_json_to_file(CommandsHistoryJSON, commands_json_path)