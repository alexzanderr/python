

import string

def change_char(string, position, character):
    new_string = string[ :position] + character + string[position + 1: ]
    return new_string