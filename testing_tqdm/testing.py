
"""
    this is a docstring for a module.opy

    im writing something here and im very happy
"""

from time import sleep
from tqdm import trange, tqdm
from multiprocessing import Pool, RLock, freeze_support

from core.aesthetics import *

print_cyan_bold("my text is very good")

class SomeClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_function(self):
        for i in range(100):
            print("vad ca se misca foarte bine")


def progresser(n):
    interval = 0.001 / (n + 2)
    total = 5000
    text = "#{}, est. {:<04.2}s".format(n, interval * total)
    for _ in trange(total, desc=text, position=n):
        # do stuff
        sleep(0.1)

if __name__ == '__main__':
    freeze_support()  # for Windows support
    tqdm.set_lock(RLock())  # for managing output contention
    p = Pool(initializer=tqdm.set_lock, initargs=(tqdm.get_lock(),))
    p.map(progresser, range(2))