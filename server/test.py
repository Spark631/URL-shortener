import random

def URL_generator():
    """
    Generates a random URL from a list of characters.
    """

    prefix = "spark.at/"

    chars = ["a","b","c","d","e","f","g","h","i","j",
            "k","l","m","n","o","p","q","r","s","t",
            "u","v","w","x","y","z","0","1","2","3",
            "4","5","6","7","8","9","A","B","C","D",
            "E","F","G","H","I","J","K","L","M","N",
            "O","P","Q","R","S","T","U","V","W","X",
            "Y","Z"]

    randomURL = random.choices(chars, k=6)
	
    randomURL = "".join(randomURL)
    print("it worked!")
    return(f"{prefix}" + randomURL)
