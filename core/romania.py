
"""
    core/romania.py

    helpful with extracting
    birth date from
    social security numbers

    also contains every district
    from this country

    good for romanian developers or
    people who live in romania

    author: @alexzander
"""


letters_to_diacritics = {
    "a": ["ă", "â"],
    "A": ["Ă", "Â"],
    "i": "î",
    "I": "Î",
    "s": "ş",
    "S": "Ş",
    "t": "ţ",
    "T": "Ţ"
}


diacritics_to_letters = {
    "ă": "a",
    "â": "a",
    "Ă": "A",
    "Â": "A",
    "î": "i",
    "Î": "I",
    "ş": "s",
    "ș": "s",
    "ț": "t",
    "ţ": "t",
    "Ț": "T",
    "Ş": "S",
    "Ţ": "T"
}


romanian_districts = [
    {
        "name": "Alba",
        "code": "01",
    },
    {
        "name": "Arad",
        "code": "02"
    },
    {
        "name": "Arge\u0219",
        "code": "03"
    },
    {
        "name": "Bac\u0103u",
        "code": "04"
    },
    {
        "name": "Bihor",
        "code": "05"
    },
    {
        "name": "Bistri\u021ba-N\u0103s\u0103ud",
        "code": "06"
    },
    {
        "name": "Boto\u0219ani",
        "code": "07"
    },
    {
        "name": "Bra\u0219ov",
        "code": "08"
    },
    {
        "name": "Br\u0103ila",
        "code": "09"
    },
    {
        "name": "Buz\u0103u",
        "code": "10"
    },
    {
        "name": "Cara\u0219-Severin",
        "code": "11"
    },
    {
        "name": "Cluj",
        "code": "12"
    },
    {
        "name": "Constan\u021ba",
        "code": "13"
    },
    {
        "name": "Covasna",
        "code": "14"
    },
    {
        "name": "D\u00e2mbovi\u021ba",
        "code": "15"
    },
    {
        "name": "Dolj",
        "code": "16"
    },
    {
        "name": "Gala\u021bi",
        "code": "17"
    },
    {
        "name": "Gorj",
        "code": "18"
    },
    {
        "name": "Harghita",
        "code": "19"
    },
    {
        "name": "Hunedoara",
        "code": "20"
    },
    {
        "name": "Ialomi\u021ba",
        "code": "21"
    },
    {
        "name": "Ia\u0219i",
        "code": "22"
    },
    {
        "name": "Ilfov",
        "code": "23"
    },
    {
        "name": "Maramure\u0219",
        "code": "24"
    },
    {
        "name": "Mehedin\u021bi",
        "code": "25"
    },
    {
        "name": "Mure\u0219",
        "code": "26"
    },
    {
        "name": "Neam\u021b",
        "code": "27"
    },
    {
        "name": "Olt",
        "code": "28"
    },
    {
        "name": "Prahova",
        "code": "29"
    },
    {
        "name": "Satu Mare",
        "code": "30"
    },
    {
        "name": "S\u0103laj",
        "code": "31"
    },
    {
        "name": "Sibiu",
        "code": "32"
    },
    {
        "name": "Suceava",
        "code": "33"
    },
    {
        "name": "Teleorman",
        "code": "34"
    },
    {
        "name": "Timi\u0219",
        "code": "35"
    },
    {
        "name": "Tulcea",
        "code": "36"
    },
    {
        "name": "Vaslui",
        "code": "37"
    },
    {
        "name": "V\u00e2lcea",
        "code": "38"
    },
    {
        "name": "Vrancea",
        "code": "39"
    },
    {
        "name": "Bucure\u0219ti",
        "code": "40"
    },
    {
        "name": "Bucure\u0219ti - Sector 1",
        "code": "41"
    },
    {
        "name": "Bucure\u0219ti - Sector 2",
        "code": "42"
    },
    {
        "name": "Bucure\u0219ti - Sector 3",
        "code": "43"
    },
    {
        "name": "Bucure\u0219ti - Sector 4",
        "code": "44"
    },
    {
        "name": "Bucure\u0219ti - Sector 5",
        "code": "45"
    },
    {
        "name": "Bucure\u0219ti - Sector 6",
        "code": "46"
    },
    {
        "name": "C\u0103l\u0103ra\u0219i",
        "code": "51"
    },
    {
        "name": "Giurgiu",
        "code": "52"
    }
]


def birth_date_from_cnp(code):
    # 1800 -> 1899
    if code[0] == "3" or code[0] == "4":
        an = 1800
        if int(code[1]) == 0 and int(code[2]) != 0:
            an += int(code[2])
        elif int(code[1]) != 0 and int(code[2]) != 0:
            an += int(code[1:3])
        luna = int(code[3:5]) if int(code[3]) != 0 else int(code[4])
        zi = int(code[5:7]) if int(code[5]) != 0 else int(code[6])
        return an, luna, zi

    # 1900 -> 1999
    elif code[0] == "1" or code[0] == "2":
        an = 1900
        if int(code[1]) == 0 and int(code[2]) != 0:
            an += int(code[2])
        elif int(code[1]) != 0 and int(code[2]) != 0:
            an += int(code[1:3])
        luna = int(code[3:5]) if int(code[3]) != 0 else int(code[4])
        zi = int(code[5:7]) if int(code[5]) != 0 else int(code[6])
        return an, luna, zi
    # 2000 -> 2099
    elif code[0] == "5" or code[0] == "6":
        an = 2000
        if int(code[1]) == 0 and int(code[2]) != 0:
            an += int(code[2])
        elif int(code[1]) != 0 and int(code[2]) != 0:
            an += int(code[1:3])
        luna = int(code[3:5]) if int(code[3]) != 0 else int(code[4])
        zi = int(code[5:7]) if int(code[5]) != 0 else int(code[6])
        return an, luna, zi
    return None


def remove_diacritics(string: str):
    return string. \
        replace("ă", "a"). \
        replace("ș", "s"). \
        replace("î", "i"). \
        replace("ț", "t"). \
        replace("Ț", "T"). \
        replace("â", "a"). \
        replace("ş", "s"). \
        replace("Î", "I"). \
        replace("ţ", "t")


# TESTING
if __name__ == '__main__':
    pass