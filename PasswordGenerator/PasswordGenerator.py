
import os
os.system("cls")

import pyperclip
from random import choice
from core.aesthetics import ConsoleColored
from string import punctuation, ascii_letters, digits
from core.winapi__ import windows_notification

# andrew style
def RandomPassword(length=20):
    password = "".join([choice(ascii_letters) + choice(digits) + choice(punctuation) for _ in range(0, 20, 2)])
    if "\\" in password:
        password = "".join([char for char in password if char != "\\"])
    return password

def PasswordGenerator():
    random_password = RandomPassword()
    pyperclip.copy(random_password)
    password_colored = ConsoleColored(random_password, "green", bold=1)
    print(f"\nPassword [ {password_colored} ] was copied to clipboard successfully!\n")

    windows_notification(
        "PasswordGenerator",
        random_password,
        10,
        "icons\\1.ico",
        True
    )

if __name__ == '__main__':
    PasswordGenerator()
