import sqlite3

conn = sqlite3.connect('tutorial1.db')
c = conn.cursor()


def read_from_db():
    c.execute("SELECT datestamp, value FROM stuffToPlot WHERE value=4 AND keyword='Python'")
    # data = c.fetchall()
    # print(data)
    for row in c.fetchall():
        print(row)


read_from_db()
c.close()
conn.close()
