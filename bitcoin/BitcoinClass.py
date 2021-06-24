

import os
import json
import requests
from time import sleep
from bitcoin.ExchangeRates import EURO_to_LEI, USD_to_LEI
from core.__numbers import fixed_set_precision_str

base_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

class Bitcoin:
    def __init__(self, currency: str):
        if currency not in ["EUR", "USD", "RON"]:
            raise InterruptedError("invalid currency")
        self.currency = currency

        response = requests.get(base_url)
        if response.status_code != 200:
            raise InterruptedError("cant access coindesk api to see live bitcoin price")

        self.name = "bitcoin"

        if self.currency == "RON":
            self.price = response.json()["bpi"]["USD"]["rate"]
            self.price = self.price.replace(",", "")
            self.price = float(self.price) * USD_to_LEI()
        else:
            self.price = response.json()["bpi"][currency]["rate"]
            self.price = self.price.replace(",", "")
            self.price = float(self.price)

        self.price = fixed_set_precision_str(self.price, 2)
        self.price = float(self.price)

    def __str__(self):
        return f"""bitcoin_price: {self.price} {self.currency}"""

def BitcoinLive(pause_interval):
    os.system("cls")
    print("bitcoin_live_price:")
    while True:
        bitcoin_usd = Bitcoin("USD")
        bitcoin_eur = Bitcoin("EUR")
        bitcoin_ron = Bitcoin("RON")
        print(f"usd: {bitcoin_usd.price}$ | eur: {bitcoin_eur.price}€ | ron: {bitcoin_ron.price}RON")
        sleep(pause_interval)

if __name__ == '__main__':
    BitcoinLive(5)