
"""
import pandas as pd
from urllib.request import urlopen

path = r'D:\__Alexzander_files__\__computer_science__\pentru_dragosi\sql_script_generator'
dataset = pd.read_csv(path + r"\titanic.csv")

print(dataset['Name'][0])

# first_names_dataset = urlopen("https://raw.githubusercontent.com/philipperemy/name-dataset/master/names_dataset/first_names.all.txt")

# first_names = first_names_dataset.readlines()

with open(first_names_dataset., 'r', encoding='utf-8') as file:
    line = file.readline()
    while line != "đoka":
        first_names.append(line)
        line = file.readline()

for f in first_names:
    print(f)

"""


