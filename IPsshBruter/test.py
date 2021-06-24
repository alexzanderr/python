
# from core.everything import *


from abc import abstractmethod
import subprocess
from string import Template
from time import sleep
from concurrent.futures import ThreadPoolExecutor

command_template = Template("ssh alexzander@192.168.1.${X}")

with open("results.txt", "w+", encoding="utf-8") as logfile:
    logfile.truncate(0)



def brute_force_ip(ip_range):
    start, stop = ip_range
    for X in range(start + 1, stop):
        process = subprocess.Popen(
            command_template.safe_substitute(
                X=X
            ),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=1
        )
        _, out = process.communicate()
        out = out.decode("utf-8")
        # err = err.decode("utf-8")
        print(out)
        with open("results.txt", "a+", encoding="utf-8") as logfile:
            # logfile.truncate(0)
            logfile.write(out + "\n")


ranges = list(range(0, 257, 32))
ranges = [(ranges[i], ranges[i + 1]) for i in range(len(ranges) - 1)]
print(ranges)

tasks = [
    (brute_force_ip, rn) for rn in ranges
]
# print(tasks)




try:
    with ThreadPoolExecutor(max_workers=8) as executor:
        for task in tasks:
            executor.submit(task[0], task[1])

except KeyboardInterrupt:
    pass

# logfile.close()
