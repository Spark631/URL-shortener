import sqlite3

from numpy import short
from .urlgen import URL_generator

def shorten(URL, short):
    while True:
        try:
            database = sqlite3.connect("data.db")
            cursor = database.cursor()

            cursor.execute("CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY, url TEXT, shorturl TEXT)")
            cursor.execute("INSERT INTO data(url, shorturl) VALUES(?, ?)", (URL, short)) # Inserts the URL and the short URL into the database
            print(cursor.execute("SELECT * FROM data").fetchall())
            print(URL)
            print(short)
        except:
            return "Error"
        finally:
            database.commit()
            database.close()
            return short


