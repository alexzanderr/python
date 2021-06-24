
import time
import curses
from core.curses__ import Keyboard

def app(screen):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW)


    text = "salutare si bine te am gasit la un nou episod\nsalutare\nsalutare\nmy name is andrew"

    h, w = screen.getmaxyx()
    x = w // 2 - len(text) // 2
    y = h // 2

    screen.attron(curses.color_pair(1))

    screen.addstr(y, x, text)

    screen.attroff(curses.color_pair(1))

    screen.refresh()

    time.sleep(3)
    # after this the program will close


"""
https://www.youtube.com/watch?v=2em6MiOpHWk

for inserting text and deleting char by char with backspace
"""

def detect_keys(screen: 'curses._CursesWindow'):

    # curses.curs_set(0)


    # h, w = screen.getmaxyx()
    # x = w // 2
    # y = h // 2
    # # print(x, y)

    x = 10

    pressed = False
    while True:
        if not pressed:
            screen.addstr(x, 0, "press something\n")
        k = screen.getch()
        pressed = True
        # char = screen.get_wch()
        screen.clear()


        if k == Keyboard.ctrl_c:
            screen.addstr(x, 0, "you want to exit")
            break
        elif k == Keyboard.arrow_up:
            screen.addstr(x, 0, "you pressed arrow UP")
        elif k == Keyboard.arrow_down:
            screen.addstr(x, 0, "you pressed arrow DOWN")
        elif k == Keyboard.enter:
            screen.addstr(x, 0, "you pressed enter")
        elif k == Keyboard.backspace:
            screen.addstr(x, 0, "you pressed BACKSPACE")
        else:
            screen.addstr(x, 0, "this is my random message: {}".format(k))


        screen.refresh()

    return 0


curses.wrapper(detect_keys)