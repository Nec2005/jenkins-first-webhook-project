

import random as rnd
def passwd(name):
    passw = ""
    for i in range(3):
        randIndex = rnd.randint(0, len(name)-1)
        letter = name[randIndex]
        passw += letter.lower()
        randNum = rnd.randint(1000,9999)
        passw += str(randNum)
    print(passw)

passwd("tomascerny")