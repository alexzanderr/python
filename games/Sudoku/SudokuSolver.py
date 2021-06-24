
from random import randint
from core.system import *
from pprint import PrettyPrinter

RandomTable = [
    [
        randint(1, 9) for _ in range(9)
    ] for _ in range(9)
]

# sections from 0 ... 8
ValidTable = [
    [9, 5, 7, 6, 1, 3, 2, 8, 4],
    [4, 8, 3, 2, 5, 7, 1, 9, 6],
    [6, 1, 2, 8, 4, 9, 5, 3, 7],
    [1, 7, 8, 3, 6, 4, 9, 5, 2],
    [5, 2, 4, 9, 7, 1, 3, 6, 8],
    [3, 6, 9, 5, 2, 8, 7, 4, 1],
    [8, 4, 5, 7, 9, 2, 6, 1, 3],
    [2, 9, 1, 4, 3, 6, 8, 7, 5],
    [7, 3, 6, 1, 8, 5, 4, 2, 9]
]

# rule 1: sa fie toate dintr-o casuta diferite
# rule 2: sa fie toate de pe linia x diferite
# rule 3: sa fie toate de pe coloana x diferite

def GetSection(table, index):
    if index == 0:
        return [values[:3] for values in table[:3]]
    elif index == 1:
        return [values[3:6] for values in table[:3]]
    elif index == 2:
        return [values[6:] for values in table[:3]]
    elif index == 3:
        return [values[:3] for values in table[3:6]]
    elif index == 4:
        return [values[3:6] for values in table[3:6]]
    elif index == 5:
        return [values[6:] for values in table[3:6]]
    elif index == 6:
        return [values[:3] for values in table[6:]]
    elif index == 7:
        return [values[3:6] for values in table[6:]]
    elif index == 8:
        return [values[6:] for values in table[6:]]
        
def GetLine(table, x):
    return table[x]
    
def GetColumn(table, y):
    return [line[y] for line in table]

# 3x3 square
def ValidateSection(section):
    for value in section:
        if section.count(value) > 1:
            return False
    return True
    
def ValidateLine(line):
    for value in line:
        if line.count(value) > 1:
            return False
    return True

def ValidateColumn(column):
    for value in column:
        if column.count(value) > 1:
            return False
    return True

def PrintSections(table):
    for i in range(9):
        PrettyPrinter(GetSection(table, i))
        print("-" * 20)
    print()
        
def PrintLines(table):
    for i in range(9):
        print(GetLine(table, i))
    print()
    
def PrintColumns(table):
    for i in range(9):
        print(GetColumn(table, i))
    print()
    
def ValidateTable(table):
    for i in range(9):
        if not ValidateSection(GetSection(table, i)):
            return False
        for j in range(9):
            if not ValidateLine(GetLine(table, i)):
                return False
            if not ValidateColumn(GetColumn(table, j)):
                return False
    return True
    
if __name__ == '__main__':
    print(ValidateTable(ValidTable))
    print(ValidateTable(RandomTable))