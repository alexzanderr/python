

from time import sleep

arg = [True]

def function(arg):
    if arg:
        print(arg)
    else:
        print("not true")



function(arg)
arg[0] = False
function(arg)