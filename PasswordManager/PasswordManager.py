
# python
import os
import sys
import json
import pprint
import getpass
import hashlib
import subprocess
import webbrowser
from datetime import datetime

# 3rd party modules
import pyperclip

# PasswordGenerator folder
from PasswordGenerator.PasswordGenerator import RandomPassword

# core
from core.winapi__ import windows_notification
from core.aesthetics import ConsoleColored

username = getpass.getuser()
mozila_firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"

date_format = "%d.%m.%Y"
time_format = "%H.%M.%S"
datetime_format = f"{date_format}_{time_format}"

return_green = ConsoleColored(
    "return",
    "yellow",
    1
)

def GetCurrentDatetime(datetime_format: str):
    return datetime.now().strftime(datetime_format)

appname = "password_manager"
password_manager_red = ConsoleColored(appname, "red", 1)

search_account_red = ConsoleColored(
    "search 4 account",
    "red",
    1
)

add_new_account_red = ConsoleColored(
    "add new account",
    "red",
    1
)

database_path = r"database.json"
# dict
database = json.loads(open(database_path).read())
# str
database_json = json.dumps(database, indent=2)
total_accounts = len(database)

fixed_email = json.loads(open("fixed_email.json").read())["email"]

def clearscreen():
    os.system("cls")

def pauseprogram():
    input("\n" + return_green)

def Prettify(__object, __indent=4):
    if type(__object) not in [list, dict]:
        raise TypeError
    return json.dumps(__object, indent=__indent)

def PrintPrettify(__object, __indent=4):
    print(Prettify(__object, __indent))

def UpdateDatabase():
    with open(database_path, "w+", encoding="utf-8") as file:
        file.truncate(0)
        file.write(json.dumps(database, indent=4))

def PrintList(array: list):
    for index, item in enumerate(array):
        print(f"[ {index + 1} ]. {item}")
    print()

def EditAccount(account):
    domain_name = list(account.keys())[0]
    total_items = len(account[domain_name])
    if total_items == 1:
        accounts_keys_list = list(account[domain_name][0].keys())
        while 1:
            print()
            PrintPrettify(account)
            PrintList(accounts_keys_list)

            choice = input("choose one to modify:\n>>> ")
            try:
                choice = int(choice)
                if 1 <= choice <= len(accounts_keys_list):
                    chosen_key = accounts_keys_list[choice - 1]
                    modified = input(f"{chosen_key}: ")
                    account[domain_name][0][chosen_key] = modified

                    choice = input("are you done? [y/n]:\n")
                    if choice == "y":
                        break

            except ValueError:
                pass

            print("~" * 50)

        print("this is your modified account:\n")
        print(account)

        choice = input("are you sure?")
        if choice == "y":
            database[domain_name][0] = account
            print(ConsoleColored("database updated!", "green", bold=1))
        else:
            print("nothing was saved!")

def DeleteAccount(account):
    domain_name = list(account.keys())[0]
    choice = input("are you sure?\n>>> ")
    if choice == "y":
        del database[domain_name]
        print(f"account with name {domain_name} was deleted from database!")

def Return(account):
    return

account_actions = [
    ["edit", EditAccount],
    ["delete", DeleteAccount],
    ["return", Return]
]

def SearchAccount():
    clearscreen()
    print(search_account_red + "\n")
    tosearch = input("enter account domain name:\n>>> ")

    if tosearch == "":
        return

    tosearch = tosearch.strip().lower()

    found_accounts = []
    occurences = 0
    for domain_name in database.keys():
        if tosearch in domain_name:
            print("~" * 40)
            print("account found!\n")
            print(json.dumps({
                domain_name: database[domain_name].copy()
            }, indent=4))
            print("total accounts on this domain: {}".format(len(database[domain_name])))
            print("~" * 40 + "\n")

            occurences += 1
            found_accounts.append({
                domain_name: database[domain_name].copy()
            })

    print(f"total accounts with \"{tosearch}\" keyword: {len(found_accounts)}")
    for index, found_acc in enumerate(found_accounts):
        print(f"[ {index + 1} ]. {list(found_acc.keys())[0]}")
    print()

    choice = input("choose one from this accounts:\n")
    try:
        choice = int(choice)
        chosen_account = found_accounts[choice - 1]

        print("\nwhat do you want to do with this account?")

        for index, account_action in enumerate(account_actions):
            print(f"[ {index + 1} ]. {account_action[0]}")
        print()

        choice = input("choose what happens:\n>>> ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(account_actions):
                account_actions[choice - 1][1](chosen_account)

        except ValueError:
            return
    except ValueError:
        return

    if occurences == 0:
        print("nothing to be found!")


    pauseprogram()

def AddAccount():
    """ adds new account to database.

        if the domain name is already existent
        then the user should enter a sub account and
        add it to the domain name in database.

        else
        creates a new domain name and adds a sub account to it.
    """

    clearscreen()
    print(add_new_account_red + "\n")
    print("enter credentials for your new account:\n")

    domain_name = input("domain name:\n>>> ")
    if domain_name == "":
        return

    domain_name = domain_name.strip().lower()

    already_existent = 0
    for dom in database.keys():
        if domain_name == dom:
            print(ConsoleColored("warning", "red", bold=1))
            print("this domain name already exists!!!\n")
            already_existent = 1
            break

    if already_existent:
        sub_account = {
            "email": fixed_email,
            "password": RandomPassword()
        }

        print("this is your new account that will be added to {}.\n".format(domain_name))
        PrintPrettify(sub_account)

        print("your domain name will look like this:\n")
        domain_copy = database[domain_name].copy()
        domain_copy.append(sub_account)
        domain_copy = {domain_name : domain_copy}
        PrintPrettify(domain_copy)

        decision = input("\nare you sure about this? [y/n]:\n")
        if decision == "y":
            database[domain_name].append(sub_account)
            print("\n" + ConsoleColored("database updated successfully!", "green", bold=1))

            windows_notification(
                "Password Manager",
                "password copied to clipboard!",
                2,
                "icons\exec.ico",
                1)
            pyperclip.copy(sub_account["password"])

    else:
        domain_account = {
            domain_name: [
                {
                    "email": fixed_email,
                    "password": RandomPassword()
                }
            ]
        }

        while 1:
            PrintPrettify(domain_account)
            print()

            credentials_key = input("add key type:\n>>> ")
            if credentials_key == "":
                break

            if credentials_key == "email" or credentials_key == "password":
                print("those already exist!")
                continue


            credentials_value = input(f"{credentials_key}: ")
            domain_account[domain_name][0].update({credentials_key : credentials_value})

            decision = input("\nare you done? [y/n]:\n")
            if decision == "y":
                break

        print("your new account looks like this:\n")
        PrintPrettify(domain_account)

        decision = input("are you sure you want to add this to database? [y/n]:\n")
        if decision == "y":
            database.update(domain_account)
            print("\n" + ConsoleColored("database updated successfully!", "green", bold=1))

            windows_notification("Password Manager", "password copied to clipboard!", 2, "icons\exec.ico", 1)
            pyperclip.copy(domain_account[domain_name][0]["password"])

    pauseprogram()

def ShowDatabase():
    database_url = f"file:///{os.getcwd()}/database.json"
    subprocess.Popen([mozila_firefox_path, r"PasswordManager\database.json"])

    print(json.dumps(database, indent=4))
    print(f"total accounts: {total_accounts}")
    print("~" * 50)
    pauseprogram()

def GenerateRandomPassword():
    clearscreen()
    random_password = RandomPassword()
    random_password_green = ConsoleColored(
        random_password,
        "green",
        1
    )
    print(f"your random password: {random_password_green}")

    pyperclip.copy(random_password)
    print("was copied to clipboard")

    windows_notification(
        "PasswordManager",
        random_password,
        2,
        "icons\\exec.ico",

    )

    current_datetime = GetCurrentDatetime(datetime_format)
    with open(f"logs\\password_generator\\log_{current_datetime}.txt", "w+", encoding="utf-8") as file:
        date, time = current_datetime.split("_")
        file.write(f"random password {random_password} was generated at\ndate: {date} \ntime: {time}.")

    pauseprogram()

def Exit():
    """ updating database. writing exit log. printing shut down. exiting. """
    UpdateDatabase()
    current_datetime = GetCurrentDatetime(datetime_format)
    with open(f"logs\\exit\\log_{current_datetime}.txt", "w", encoding="utf-8") as file:
        date, time = current_datetime.split("_")
        file.write(f"exit occured at\ndate: {date}\ntime: {time}\nusername: {username}")

    print(f"{appname} app was shut down.")
    sys.exit(0)

menu = [
    ["search account", SearchAccount],
    ["add new account", AddAccount],
    ["show database", ShowDatabase],
    ["genereate random password", GenerateRandomPassword],
    ["exit", Exit]
]

def PrintMenu():
    for index, action in enumerate(menu):
        print(f"[ {index + 1} ]. {action[0]}")
    print()

def Menu():
    clearscreen()
    print(password_manager_red + "\n")
    PrintMenu()
    action = input("choose your action:\n>>> ")
    action = action.strip()
    try:
        index = int(action)
        del action

        if 1 <= index <= len(menu):
            menu[index - 1][1]()
    except ValueError:
        pass

def PasswordManager():
    # load time
    current_datetime = GetCurrentDatetime(datetime_format)
    with open(f"logs\\login\\log_{current_datetime}.txt", "w+", encoding="utf-8") as file:
        date, time = current_datetime.split("_")
        file.write(f"login occured at\ndate: {date}\ntime: {time}\nusername: {username}")

    while 1:
        Menu()

if __name__ == '__main__':
    try:
        PasswordManager()
    except Exception as error:
        print("error found. error forced app shut down.")
        print(error)
        pauseprogram()

        # if we got some error we must update database if
        # changes were made by user
        Exit()