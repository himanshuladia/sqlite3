import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt

conn = sqlite3.connect('tutorial1.db')
c = conn.cursor()


def graph_data():
    c.execute("SELECT unix, value FROM stuffToPlot")
    dates = []
    values = []
    for row in c.fetchall():
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()


graph_data()
