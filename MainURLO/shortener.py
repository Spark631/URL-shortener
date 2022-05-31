import sqlite3

from numpy import short
from urlgen import URL_generator

def shorten(URL, short):

    while True:
        try:
            database = sqlite3.connect("data.db")
            cursor = database.cursor()

            cursor.execute("CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY, url TEXT, shorturl TEXT)")
            all_url = cursor.execute("SELECT shorturl FROM data").fetchall() # Gives a tuple of all shorturls
            for SURL in all_url:
                if short in SURL:
                    short = URL_generator() # generate new short URL
                else:
                    cursor.execute("INSERT INTO data(url, shorturl) VALUES(?, ?)", (URL, short)) # Inserts the URL and the short URL into the database
        except:
            database.close()
            return "Error"
        finally:
            database.commit()
            database.close()


shorten("test")

