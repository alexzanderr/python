
import sys
from core.aesthetics_library import ConsoleColored
from core.system import *
from core.numbers_lib import ShowDecimals

original_bitcoin_price = 11500
latest_bitcoin_price = 26000
bitcoin_difference = abs(original_bitcoin_price - latest_bitcoin_price)

def XModuloOfY(x, y):
    return x * 100 / y

script_arguments = sys.argv
if len(script_arguments) == 2:
    invested_amount = script_arguments[1].split("=")[1]
    try:
        invested_amount = float(invested_amount)
    except ValueError:
        print("money amount is invalid. exiting...")
    else:
        # the amount of bitcoin in quantity invested
        invested_bitcoin = invested_amount / original_bitcoin_price
        
        # the amount of current bitcoin cash in dollars
        latest_invested_price = invested_bitcoin * latest_bitcoin_price
        latest_invested_price = float(ShowDecimals(latest_invested_price, 2))
        
        difference = abs(latest_invested_price - invested_amount)
        difference = float(ShowDecimals(difference, 2))
        
        print("total bitcoin wallet: {}".format(latest_invested_price))
        # bitcoin is greater in present -> profit
        if latest_bitcoin_price > original_bitcoin_price:
            print("congratulations, you just made {} profit.".format(ConsoleColored(str(difference) + "$", "green", bold=1)))
            modulo_diff = XModuloOfY(original_bitcoin_price, latest_bitcoin_price)
            greater = 1
            print("profit is {}% of {} (money invested)".format(ConsoleColored(XModuloOfY(difference, invested_amount), "cyan", bold=1), invested_amount))
            
        elif latest_invested_price == original_bitcoin_price:
            print("there is no update in your cash.")
            
        else:
            modulo_diff = XModuloOfY(latest_bitcoin_price, original_bitcoin_price)
            print("you noob... you just lost {}".format(ConsoleColored(str(difference) + "$", "red", bold=1)))
            greater = 0
        
        print("original bitcoin price: {}".format(original_bitcoin_price))
        print("latest bitcoin price: {}".format(latest_bitcoin_price))
        
        if greater:
            print("difference: {}".format(ConsoleColored(bitcoin_difference, "green", bold=1)))
        else:
            print("difference: {}".format(ConsoleColored(bitcoin_difference, "red", bold=1)))
            
        modulo_diff = ShowDecimals(modulo_diff, 2)
        modulo_diff = ConsoleColored(modulo_diff + "%", "cyan", bold=1)
        print("{} is {} of {}".format(ConsoleColored(original_bitcoin_price, "yellow", bold=1), modulo_diff, ConsoleColored(latest_bitcoin_price, "yellow", bold=1)))