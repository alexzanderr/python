
import json
import time
import asyncio
import itertools
import pyperclip
from time import sleep
from datetime import datetime

from TinderAPIX.session import Session
from core.aesthetics import *
import threading
from core.winapi__ import windows_notification

""" USAGE
for match in sess.yield_matches():
    print([x.body for x in match.get_messages()]) # gets the body of messages]
    match.get_messages()
"""

def GetTinderUsersList():
    """ returns a list with tinder collected users over time """
    return json.loads(open("TinderUsers.json").read())

def OverwriteTinderUsersList(updated_list: list):
    with open("TinderUsers.json", "w+", encoding="utf-8") as file:
        file.truncate(0)
        file.write(json.dumps(updated_list, indent=4))

def UpdateTinderUsersList(original_list: list, data_json: dict):
    for user in original_list:
        if user["id"] == data_json["id"]:
            print("user already exists.")
            return

    original_list.append(data_json)
    # print("users lists updated with: {}\n".format(data_json["id"]))

def GetTotalCollectedUsers():
    """ returns the total number of users in my database """
    return len(json.loads(open("TinderUsers.json").read()))

class TinderBot:
    """ this class implements TindeAPIX """

    def __init__(self, xauth_token: str):
        """ you can find the token by searching for it in network in browser while staying on tinder"""
        self.xauth_token = xauth_token

        try:
            self.tinder_session = Session(xauth_token)
        except Exception as exception:
            print(exception)
            while True:
                try:
                    self.xauth_token = input("your token is expired or invalid. enter here brand new one:\n>>> ")
                    self.tinder_session = Session(xauth_token)
                    break
                except:
                    pass

        print("Tinder session established successfully!")

    def LikeAllNearbyGirls(self, iterations=1):
        """
            aparent pot sa dau like cat vreau
            chiar daca pe tinder.com nu mai am likeuri
            aici pot sa vad useri si sa le dau like la infinit
            asta practic sfideaza legile tinderului which is cool

            this function is listing nearby girls, likes them',
            tells me if i have a match with them and appends the users
            into the TinderUsers list
        """
        tinder_users_list = GetTinderUsersList()

        for user in itertools.islice(self.tinder_session.yield_users(), iterations):
            print("~" * 70)
            user_metadata = {
                "name": user.name,
                "id": user.id,
                "age": user.age,
                "bio": user.bio,
                "gender": user.gender,
                "photos_url_list": user.photos,
                "liked": True
            }
            matched = user.like()

            if matched:
                user_metadata["matched"] = True
                print(ConsoleColored("MATCHED!!!", "green", bold=1))
                windows_notification("Tinder MATCH", "you got a match with {}".format(user.name), 2, "icons/tinder_logo.ico")
            else:
                user_metadata["macthed"] = False
                print(ConsoleColored("no match.", "red", bold=1))

            print(json.dumps(user_metadata, indent=8))
            print("{} liked successfully!".format(user.name))

            UpdateTinderUsersList(tinder_users_list, user_metadata)
            OverwriteTinderUsersList(tinder_users_list)

            print("{} added to database successfully!".format(user.name))
            print("~" * 70)
            print("=" * 80)

    def MessageAllMathces(self, message: str):
        print("the message:")
        print("~" * 50)
        print(message)
        print("~" * 50)

        decision = input("are you sure? [y/n]:\n")
        if decision == "y":
            start_time = time.time()

            counter = 0
            for m in self.tinder_session.yield_matches():
                if type(message) == list:
                    for line in message:
                        m.message(line)
                else:
                    m.message(message)

                match_name = ConsoleColored(m.name, "green", bold=1, underlined=1)
                print("Message sent to {} successfully!".format(match_name))
                counter += 1

            stop_time = time.time()
            execution_time = (stop_time - start_time)

            print("~" * 50)
            print("Message sent to all matches successfully!")
            print("Execution for this function: {} seconds.".format(fixed_set_precision_str(execution_time, 2)))
            print("Total matches: {}".format(counter))
        else:
            print("another time!")

    def GetMatchesList(self):
        return list(self.tinder_session.yield_matches())

    def PrintMatchesData(self):
        for match in self.tinder_session.yield_matches():
            print(match.id)
            print(match.name)
            print("~" * 50)

    def FindIDSbyName(self, name):
        for m in self.tinder_session.yield_matches():
            if m.name == name:
                print(m.id)

    def SpamUser(self, user_id, iterations):
        for m in self.tinder_session.yield_matches():
            if m.id == user_id:
                print('user found!')
                for _ in range(iterations):
                    message = "ti-am zis ca-ti fac spam cu botul!!!"
                    print(message)
                    m.message(message)
            else:
                print("still searching...")



if __name__ == '__main__':
    tinderbot = TinderBot("0314982b-a879-4b7a-92ac-b0f0661413f8")
    x = tinderbot.PrintMatchesData()
    print(x)
    # tinderbot.LikeAllNearbyGirls(20)
    # tinderbot.SpamUser("5cb8d0ab66a40f15001e8e0d")
    # tinderbot.FindIDSbyName("Andreea")
