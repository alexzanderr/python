
import curses
from string import ascii_lowercase


class Keyboard:
    arrow_up    = 450
    arrow_down  = 456
    arrow_right = 454
    arrow_left  = 452

    backspace = 8
    esc = 27
    tab = 9
    enter = 10

    # keyboard interrupt
    ctrl_c = 3

    class Letter:
        a = 97
        b = 98
        c = 99
        # ...
        z = 122

    class Digit:
        zero = 48
        # ...
        nine = 57
