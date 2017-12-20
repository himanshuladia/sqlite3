import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('tutorial1.db')
c = conn.cursor()


def print_table():
    c.execute("SELECT * FROM stuffToPlot")
    for row in c.fetchall():
        print(row)
    print('')


def update():
    print_table()
    c.execute("UPDATE stuffToPlot SET value = 99 WHERE value = 4")
    conn.commit()
    print_table()


def delete():
    print_table()
    c.execute("DELETE FROM stuffToPlot WHERE value = 99")
    conn.commit()
    print_table()


c.close()
conn.close()
