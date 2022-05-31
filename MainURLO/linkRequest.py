import sqlite3

def retrive(surl):
    try:
        database = sqlite3.connect("data.db")
        cursor = database.cursor()

        url = cursor.execute(f"SELECT url FROM data WHERE shorturl = '{surl}'").fetchall()[0][0]
        return url
    except:
        return False
    finally:
        database.commit()
        database.close()

