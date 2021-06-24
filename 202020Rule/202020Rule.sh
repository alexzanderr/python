#!/usr/bin/bash

if [ $# -eq 0 ]; then
    echo "No arguments supplied, initializing 202020Rule with 20 minutes\n"
    cd /home/alexzander/Applications__/PythonApplications/202020Rule && python3 202020Rule.py -m 20

elif [ $# -eq 1 ]; then
    echo "One argument supplied, initializing 202020Rule with _$1 minutes\n"
    cd /home/alexzander/Applications__/PythonApplications/202020Rule && python3 202020Rule.py -m $1
else
    echo "too many args. exiting"

fi