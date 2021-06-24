
"""
    learning sql with python
    data types:
        NULL
        INTEGER
        REAL
        TEXT
        BLOB
"""

import sqlite3 as s
import os
import sys


print("hello my name is andrew")
x = 3
hello = x
hello_there = hello.bit_length()


class TestingSQL(object):
    def __init__(self, name):
        self.name = name



def create_table_for_first_time(cursor, connection):
    cursor.execute("""
        CREATE TABLE customers (
        name text,
        age integer,
        email text
    )""")
    connection.commit()


def insert_values(cursor, connection):
    cursor.execute("""insert into customers values ('andrew', 21, 'andrew@andrew.com')""")
    connection.commit()


def some_random_function(a: int):
    """[summary]

    Args:
        a (int): [description]

    Returns:
        [type]: [description]
    """
    x = 3
    return x ** 2

def print_table(cursor, connection):
    cursor.execute("select * from customers")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.commit()


def delete_table(cursor, connection):
    cursor.execute("drop table customers")
    x = connection.commit()



if __name__ == '__main__':
    connection = s.connect("testing_sql.db")
    cursor = connection.cursor()

    # delete_table(cursor, connection)


    connection.close()
