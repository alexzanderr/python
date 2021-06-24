
from json import JSONEncoder
from core.json__ import *
from core.aesthetics import *

def is_valid(payment: dict):
    for value in payment.values():
        if value != "":
            return True
    return False

class Payment(JSONEncoder):
    def __init__(self, date, name, url, price, currency):
        self.date = date
        self.name = name
        self.url = url
        self.price = price
        self.currency = currency


    def string(self, indent=4):
        content = "{__indent}date: {date}\n"
        content += "{__indent}name: {name}\n"
        content += "{__indent}url: {url}\n"
        content += "{__indent}price: {price}\n"
        content += "{__indent}currency: {currency}"
        content = content.format(__indent=" " * indent, date=self.date, name=self.name, url=self.url, price=self.price, currency=self.currency)
        return content

    def print__(self, indent=4):
        print(self.string(indent))


payments_database_json_path = "payments.json"
payments_database_json = read_json_from_file(payments_database_json_path)

payments_database_list = [Payment(*payment.values()) for payment in payments_database_json]
del payments_database_json

def PrintDatabase():
    dim = 100
    print("[{}]".format("=" * dim))
    print(yellow_bold_underlined("DATABASE").center(100) + "\n")

    total_payed = 0
    currency = None
    for payment in payments_database_list:
        if is_valid(payment.__dict__):
            print("[~]")
            payment.url = cyan_underlined(payment.url)
            payment.price = red_bold(payment.price)
            payment.print__(4)
            print("[~]")

            total_payed += float(delete_ansi_codes(payment.price))
            currency = payment.currency

    print("[{}: {} {}]".format(yellow_bold("TOTAL_PAYED"), red_bold(total_payed), currency))
    print("[{}]".format("=" * dim))

if __name__ == '__main__':
    PrintDatabase()
