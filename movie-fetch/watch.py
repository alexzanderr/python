#!/usr/bin/python3


import os
import sys
from typing import DefaultDict


cwd = os.getcwd()

# have a web server on the other side, on the server
# that
# waits for you to get get request in order to download the movie with psc

"""
download the movie (with pscp),
watch the movie,
delete the movie
"""




if __name__ == '__main__':

    args = sys.argv

    if len(args) == 2:
        movie_name = args[1]
