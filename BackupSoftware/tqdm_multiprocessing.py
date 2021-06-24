

from requests.sessions import default_headers
from tqdm import tqdm, trange
from concurrent.futures import ThreadPoolExecutor



def progresser():
    print("a123123123123")

    for _ in trange(100):
        sleep(0.1)




def progresser2():
    print("123123123123")

    for _ in trange(100):
        sleep(0.1)



if __name__ == '__main__':
    with ThreadPoolExecutor() as p:
        # p.map(progresser, range(1))
        # p.map(progresser2, range(1))
        p.submit(progresser)
        p.submit(progresser2)
