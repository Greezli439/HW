import faker
from random import random, choice
import sqlite3


def create_db():
    with open('students.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('students.db') as con:
        cur = con.cursor()
        cur.executescript(sql)


if __name__ == "__main__":
    create_db()