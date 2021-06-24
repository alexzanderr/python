
"""
    setarile se aplica fara sa dai restart
"""


from requests.sessions import default_headers
from tqdm import tqdm, trange
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from string import Template
from core.aesthetics import AnsiCodes


L = list(range(2))


def progresser(n):
    interval = 0.001 / (n + 2)
    total = 5000
    text = "#{} progresser".format(n, interval * total)

    for _ in trange(total, desc=text):
        with open("pro1.txt", "a+", encoding="utf-8") as f:
            f.write("this line was wrote from pro1\n")

        sleep(1)



def progresser2(n):
    interval = 0.001 / (n + 2)
    total = 5000
    text = "#{} progresser2".format(n, interval * total)

    for _ in trange(total, desc=text):
        with open("pro2.txt", "a+", encoding="utf-8") as f:
            f.write("this line was wrote from pro2\n")

        sleep(0.1)


if __name__ == '__main__':
    with ThreadPoolExecutor() as p:
        p.map(progresser, range(1))
        p.map(progresser2, range(1))
