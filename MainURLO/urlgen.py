import random
import sqlite3

from regex import F

def URL_generator():
    """
    Generates a random URL from a list of characters.
    """

    # prefix = "spark/"
    # prefix = "127.0.0.1:5000/"
    chars = ["a","b","c","d","e","f","g","h","i","j",
            "k","l","m","n","o","p","q","r","s","t",
            "u","v","w","x","y","z","0","1","2","3",
            "4","5","6","7","8","9","A","B","C","D",
            "E","F","G","H","I","J","K","L","M","N",
            "O","P","Q","R","S","T","U","V","W","X",
            "Y","Z"]
    database = sqlite3.connect("data.db")
    cursor = database.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY, url TEXT, shorturl TEXT)")
    all_url = cursor.execute("SELECT shorturl FROM data").fetchall() # Gives a tuple of all shorturls
    
    randomURL = random.choices(chars, k=6)
    print("This is the before of the randomURL" + str(randomURL))
    randomURL = "".join(randomURL)
    print("this is allurl" + str(all_url))
    while True:
        try:
            if all_url == []:
                # return prefix + randomURL
                return randomURL
            for url in all_url:
                if randomURL in url:
                    randomURL = []
                    randomURL = random.choices(chars, k=6)
                    randomURL = "".join(randomURL)
                    print("This is the after of the randomURL" + str(randomURL))
                else:
                    # return prefix + randomURL
                    return randomURL
            # return(f"{prefix}" + randomURL)
        except:
            print("this iwh yu")
            return False

