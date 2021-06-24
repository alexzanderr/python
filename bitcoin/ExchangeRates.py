

import json
import requests
from core.__numbers import ShowDecimals

def USD_to_LEI():
    """ -> float .{2}"""
    current_usd_rate_url = "https://api.exchangeratesapi.io/latest?base=USD"
    response = requests.get(current_usd_rate_url)
    usd_to_lei = response.json()["rates"]["RON"]
    return float(ShowDecimals(usd_to_lei, 2))

def EURO_to_LEI():
    """ -> float .{2}"""
    current_usd_rate_url = "https://api.exchangeratesapi.io/latest?base=EUR"
    response = requests.get(current_usd_rate_url)
    usd_to_lei = response.json()["rates"]["RON"]
    return float(ShowDecimals(usd_to_lei, 2))

if __name__ == '__main__':
    print(EURO_to_LEI())