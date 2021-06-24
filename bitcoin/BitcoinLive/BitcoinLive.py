
import requests
import os
from time import sleep
from core.json__ import *
from core.aesthetics import *
from core.numbers__ import *
from core.datetime__ import *
from core.system import clearscreen
import logging
clearscreen()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

__logger = logging.getLogger("bitcoin_live")
__logger.setLevel(logging.INFO)


bitcoin_handler = logging.FileHandler("bitcoin.log")
bitcoin_handler.setLevel(logging.INFO)
bitcoin_handler.setFormatter(formatter)

__logger.addHandler(bitcoin_handler)


chart_logger = logging.getLogger("chart")
chart_logger.setLevel(logging.INFO)

chart_handler = logging.FileHandler("eur_chart.log")
chart_handler.setLevel(logging.INFO)

chart_logger.addHandler(chart_handler)


bpi_api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"

print_format = "Bitcoin | Price: {p_eur} EUR | {p_usd} USD | Time: {t}"

pause_interval = 5
__iterations = 0
while True:
    resp = requests.get(bpi_api_url)
    r_json = resp.json()
    # pretty_print(r_json)

    p_eur = r_json["bpi"]["EUR"]["rate_float"]
    p_eur = fixed_set_precision_str(p_eur, 2)
    chart_logger.info(p_eur)

    p_usd = r_json["bpi"]["USD"]["rate_float"]
    p_usd = fixed_set_precision_str(p_usd, 2)

    ctime = get_current_timedate("%H:%M:%S - %d.%m.%Y")
    print(print_format.format(p_eur=yellow_bold(p_eur), p_usd=yellow_bold(p_usd), t=ctime))


    __logger.info(print_format.format(p_eur=p_eur, p_usd=p_usd, t=ctime))

    __iterations += 1
    if __iterations == 30:
        clearscreen()
        __iterations = 0

    sleep(pause_interval)