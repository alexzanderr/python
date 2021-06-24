
import json
from core.random_library import *
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from random import choice

path = r"ITPCars\RomanianDistricts.json"
database_path = r"ITPCars\CarsDatabase.json"

def generate_romanian_districts():
    url = r"https://en.wikipedia.org/wiki/Counties_of_Romania"
    session = HTMLSession()
    response = session.get(url)
    response.html.render(sleep=1)


    sp = BeautifulSoup(response.html.html, "html.parser")
    table = sp.find("table", attrs={
        "class": "wikitable sortable jquery-tablesorter"
    })
    tbody = table.find("tbody")
    trs = tbody.findAll("tr")
    counter = 0
    romanian_districts = []
    for tr in trs:
        tds = tr.findAll("td")
        name = tds[1].text
        iso_code = tds[3].text
        district = {
            "name": name[:len(name) - 1],
            "ISOCode": iso_code[:len(iso_code) - 1]
        }
        romanian_districts.append(district)
        counter += 1

    with open(path, "w+", encoding="utf-8") as file:
        file.truncate(0)
        file.write(json.dumps(romanian_districts, indent=4))
        
districts = json.loads(open(path).read())
ISOCodes = [district["ISOCode"] for district in districts]


CarsDatabase = []
for i in range(1000):
    car_number = "{} {} {}".format(choice(ISOCodes), RandomNumber(choice([2,])), RandomUpperString(3))
    phone_number = "07{}.{}.{}".format(RandomDigits(2), RandomDigits(3), RandomDigits(3))
    itp_date = RandomDateString("16.04.2020", "30.04.2020")
    car_specs = {
        "numar_masina": car_number,
        "telefon_detinator": phone_number,
        "data_ITP": itp_date,
        "durata_ITP": 6
    }
    CarsDatabase.append(car_specs)


with open(database_path, "w+", encoding="utf-8") as file:
    file.truncate(0)
    file.write(json.dumps(CarsDatabase, indent=4))