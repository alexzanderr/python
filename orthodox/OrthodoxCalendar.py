
from datetime import datetime
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from time import sleep
import sys, json, os
from core.system import *

program_arguments = sys.argv
year_from_args = False
if len(program_arguments) == 2:
    date = program_arguments[1].split("=")[1]
    try:
        struct_date = datetime.strptime(date, "%d.%m.%Y")
        items = date.split(".")
        year = int(items[2])
        year_from_args = True
    except:
        print("incorrect year.")
elif len(program_arguments) == 1:
    year = input("enter year you want to scrap:\n")
    try:
        year = int(year)
    except ValueError:
        print("invalid year.")
    
# year = 2021
calendar_path = r"orthodox\OrthodoxCalendar{year}.json".format(year=year)

if 2020 <= year:
    url = "https://noutati-ortodoxe.ro/calendar-ortodox/?year={}".format(year)
    print("get http request to: {url}...".format(url=url))
    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep=1)
    
    sp = BeautifulSoup(response.html.html, "html.parser")
    
    print("extracting information...")
    months = [
        sp.find("div", attrs={
            "class": "calendar",
            "id": "month{}".format(month)
        }) for month in range(1, 13)
    ]
    
    calendar = []
    for index in range(1, 13):
        trs = months[index - 1].findAll("tr")
        
        month_name = trs[0].text.strip()
        start = 4
        dim = len(month_name)
        m = ""
        while start < dim:
            if month_name[start] == "\t":
                break
            m += month_name[start]
            start += 1
        month_name = m.lower().title()
        del m, start, dim
        
        month_days = [trs[i].text.strip()[0:2] for i in range(1, len(trs))]
        for i in range(len(month_days)):
            if month_days[i] != "Du" and month_days[i] != "(†":
                if month_days[i][1] == "\t":
                    month_days[i] = (int(month_days[i][0]), "<")
                elif month_days[i][1] != "\t":
                    month_days[i] = (int(month_days[i][:2]), ">")
            else:
                month_days[i] = (month_days[i], None)
        
        events = []
        length = 0
        for i in range(1, len(trs)):
            if month_days[i - 1][1] == "<":
                day = month_days[i - 1][0]
                event = trs[i].text.strip()[1:]
                length += 1
            elif month_days[i - 1][1] == ">":
                day = month_days[i - 1][0]
                event = trs[i].text.strip()[2:]
                length += 1
            else:
                events[length - 1]["event"] += "\n" + trs[i].text.strip()
            
            if event.startswith("\t\t\t"):
                event = event[3:]
                
            events.append({
                "day": day,
                "event": event
            })
        
        calendar.append({
            "month_name": month_name,
            "month_index": index,
            "events": events
        })
    
    print("writing information to json file...")
    
    # if not os.path.exists(project_path):
    with open(calendar_path, "w+", encoding="utf-8") as file:
        file.truncate(0)
        file.write(json.dumps(calendar, indent=4))
            
    if year_from_args:
        d = int(items[0])
        m = int(items[1])
        for month in calendar:
            if m == month["month_index"]:
                for event in month["events"]:
                    if event["day"] == d:
                        print("\nwanted event:\n" + event["event"] + "\n")
                        break
    else:
        print("done.")
    
    del events, length, month_days
else:
    print("incorrect year.")