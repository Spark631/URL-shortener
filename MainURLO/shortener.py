import sqlite3

from numpy import short

def shorten(URL):
    database = sqlite3.connect("data.db")
    cursor = database.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY, url TEXT, shorturl TEXT)")
    cursor.execute("INSERT INTO data(url, shorturl) VALUES(?, ?)", (URL, "test"))
    database.commit()

    try:
        all_url = cursor.execute("SELECT shorturl FROM data").fetchall()
        for SURL in all_url:
            if URL in SURL:
                print("This URL is already used")
    except:
        return "Error"
        
    database.close()

shorten("test")

