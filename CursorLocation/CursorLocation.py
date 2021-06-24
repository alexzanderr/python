
import os
import pyautogui
from time import sleep
from core.aesthetics import *

def CursorLocation():
    os.system("cls")
    print("Current cursor coordinates:")
    while True:
        try:
            pos = pyautogui.position()
            x = lime_green(pos.x)
            y = lime_green(pos.y)
            print("(X={}, Y={})".format(x, y), end="\r")
            print(len(repr(x)))
            sleep(.01)

        except KeyboardInterrupt:
            print("\napp closed from keyboard interrupt")
            break

if __name__ == '__main__':
    CursorLocation()