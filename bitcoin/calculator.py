
import os
from time import sleep

# core
from core.__numbers import *
from core.aesthetics import ConsoleColored

# finance
from bitcoin.BitcoinClass import Bitcoin
from bitcoin.ExchangeRates import USD_to_LEI, EURO_to_LEI

def CalculateStats(my_investment_lei: int, btc_second_price: int, currency: str="EUR"):
    euro_to_lei = EURO_to_LEI()
    my_investment_lei_red = ConsoleColored(my_investment_lei, "red", bold=1)
    my_investment_euro = my_investment_lei / euro_to_lei

    if 2 <= my_investment_euro <= 10:
        coinbase_fee_euro = 0.99
    elif 11 <= my_investment_euro <= 25:
        coinbase_fee_euro = 1.49
    elif 25 < my_investment_euro <= 50:
        coinbase_fee_euro = 1.9
    elif 50 < my_investment_euro <= 200:
        coinbase_fee_euro = 2.99
    else:
        coinbase_fee_euro = 0.399 * my_investment_euro

    my_investment_euro = float(fixed_set_precision_float(my_investment_euro, 2))
    my_investment_euro_yellow = ConsoleColored(my_investment_euro, "yellow", bold=1)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    bitcoin = Bitcoin("EUR")
    # my_investment_euro -= coinbase_fee_euro
    my_investment_btc = my_investment_euro / bitcoin.price

    print(f"my_investment_lei: {my_investment_lei_red} RON")
    print(f"euro_to_lei: 1{currency} -> {euro_to_lei} RON")
    print(f"my_investment_euro: {my_investment_euro_yellow}{currency}")
    print(f"my_investment_euro_with_fees: {my_investment_euro - coinbase_fee_euro}{currency}")


    btc_to_lei = bitcoin.price * euro_to_lei
    btc_to_lei = float(fixed_set_precision_float(btc_to_lei, 2))

    print()
    print(f"bitcoin_price: {bitcoin.price}{currency} ({btc_to_lei} RON)")
    print(f"my_investment_btc: {my_investment_btc} BTC")
    print()
    print(f"if the price of btc goes to {btc_second_price} then:")

    current_dollars_amount = btc_second_price * my_investment_btc
    current_dollars_amount = float(fixed_set_precision_float(current_dollars_amount, 2))

    profit_dollars = current_dollars_amount - my_investment_euro
    profit_dollars = float(fixed_set_precision_float(profit_dollars, 2))

    profit_dollars_green = ConsoleColored(profit_dollars, "green", bold=1)

    profit_lei = profit_dollars * euro_to_lei
    profit_lei = float(fixed_set_precision_float(profit_lei, 2))
    profit_lei_green = ConsoleColored(profit_lei, "green", bold=1)

    print(f"you would have in your account: {current_dollars_amount}{currency} ({my_investment_btc} * {btc_second_price})")
    print(f"with profit: {profit_dollars_green}{currency} OR {profit_lei_green} RON ({profit_dollars} RON * {euro_to_lei}{currency})")

    profit_percent = profit_dollars * 100 / my_investment_euro
    profit_percent = float(fixed_set_precision_float(profit_percent, 2))
    profit_percent_green = ConsoleColored(profit_percent, "green", bold=1)

    print(f"profit is +{profit_percent_green}%")

def CalculateStatsToInfinity(my_investment_lei: int, btc_second_price: int, delay: int):
    """
        1 btc ... 33500$
        x btc ... 25.12$
        x = (25.12 * 1) / 33500
        x =
    """
    while 1:
        os.system("cls")
        CalculateStats(my_investment_lei, btc_second_price)
        sleep(delay)

if __name__ == '__main__':
    # CalculateStats(100, 40000)
    # print("~" * 50``)
    CalculateStatsToInfinity(300, 81106, 10)