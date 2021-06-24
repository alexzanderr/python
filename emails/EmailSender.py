
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import webbrowser, sys, smtplib, json
from datetime import datetime
from collections import OrderedDict
from core.aesthetics import *
from emails.functionality import *
from core.system import *

appname = \
"""
  ______                 _ _  _____                _
 |  ____|               (_) |/ ____|              | |
 | |__   _ __ ___   __ _ _| | (___   ___ _ __   __| | ___ _ __
 |  __| | '_ ` _ \ / _` | | |\___ \ / _ \ '_ \ / _` |/ _ \ '__|
 | |____| | | | | | (_| | | |____) |  __/ | | | (_| |  __/ |
 |______|_| |_| |_|\__,_|_|_|_____/ \___|_| |_|\__,_|\___|_|
"""

class EmailSender:
    def __init__(self):
        self.LIMIT = 50
        self.lessecure_app_url = "https://myaccount.google.com/u/4/lesssecureapps?pli=1"
        self.general_message = \
        """
            Type of encryption used: TLS(Transport layer security) - standard encryption
            This __message was sent with python programming language using simple mail transfer protocol library (smtplib).
            Thank you for your attention!
            Have a great day!
            Bye.
        """

        # list
        self.ContactsDatabase = json.loads(open(r"emails\ContactsDatabase.json").read())
        self.contacts_dimension = len(self.ContactsDatabase)

        # list
        self.automation_account = json.loads(open(r"emails\AutomationAccount.json").read())

        self.menu_options = [
            "send email to someone",
            "__EXIT__"
        ]

    def run(self):
        clearscreen()
        print(ConsoleColored(appname, "yellow"))
        print(datetime.now().strftime("current datetime: %H:%M:%S - %d.%m.%Y\n"))

        user_input = input("open less secure apps settings for your google account'? [(y) or (any key)]:")
        if user_input == 'y':
            webbrowser.open(self.lessecure_app_url)

        self.MenuFunction()

    def DisplayOptions(self):
        for index, option in enumerate(self.menu_options):
            print(f"[ {index + 1} ]. {option}")
        print()

    def DisplayStats(self):
        print(ConsoleColored(appname, "yellow"))
        print(datetime.now().strftime("current datetime: %H:%M:%S - %d.%m.%Y\n"))

    def MenuFunction(self):
        clearscreen()
        self.DisplayStats()
        self.DisplayOptions()
        user_input = input("choose your action:\n")
        try:
            user_input = int(user_input)
            if user_input == 1:
                self.SelectContact()
            elif user_input == 2:
                sys.exit(0)
            self.MenuFunction()
        except ValueError:
            self.MenuFunction()

    def send(self, contact, subject, message):
        clearscreen()
        self.DisplayStats()

        print(f"selected contact:")
        print(f"\t{contact}")

        print(f"selected subject:")
        print(f"\t{subject}")

        print(f"selected message:")
        print(f"\t{message}")

        user_input = input("\nare you sure you want to perform this action? [y/n]:\n")
        if user_input == "y":
            SendEmail(self.automation_account["email"], self.automation_account["password"], contact, subject, message)
            input("\npress [enter] to contiune")
        elif user_input == "n":
            self.MenuFunction()
        else:
            # reload with the same data
            self.send()

    def SelectContact(self):
        clearscreen()
        self.DisplayStats()

        # printing the contacts list
        for index, contactDICT in enumerate(self.ContactsDatabase):
            print(f"[ {index + 1} ]. [ {contactDICT['name']} ] => [ {contactDICT['email']} ]")
        print(ConsoleColored(f"[ {self.contacts_dimension + 1} ]. __RETURN__", "yellow"))
        print(ConsoleColored(f"[ {self.contacts_dimension + 2} ]. __EXIT__\n", "red"))

        # saving user input
        user_input = input("choose your action:\n")
        try:
            user_input = int(user_input)

            # validating user input
            if 1 <= user_input <= self.contacts_dimension:
                clearscreen()
                self.DisplayStats()
                # selecting user input
                selected_contact = self.ContactsDatabase[user_input - 1]["email"]
                print("you selected contact: {} .\n".format(selected_contact))

                subject = input("paste subject or write subject:\n")
                message = input("paste message or write message:\n")

                input("press [enter] to continue")

                self.send(selected_contact, subject, message)
            elif user_input == self.contacts_dimension + 1:
                self.MenuFunction()
            elif user_input == self.contacts_dimension + 2:
                sys.exit(0)

        except ValueError:
            # reload
            if user_input == "":
                self.SelectContact()
            # cancel
            if user_input == "abort":
                self.MenuFunction()
            # exit
            elif user_input == "exit" or user_input == "EXIT":
                sys.exit(0)
        self.MenuFunction()

if __name__ == "__main__":
    app = EmailSender()
    app.run()