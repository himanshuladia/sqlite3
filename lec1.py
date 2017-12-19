import sqlite3

# Create connection and cursor
conn = sqlite3.connect('tutorial.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(13215466, '2018-01-01', 'Hello', '10')")
    conn.commit()
    c.close()
    conn.close()


create_table()
data_entry()
