import reader
import random
fn = "test.json" # IMPORTANT: If you've made a custom setup using 'creator.py', change this file to the filename you use there.
rand = random.Random()

score = 0
maxScore = 3
minScore = -1

howManyLettersOfName = 2

def checkScore():
    global score
    global minScore
    global maxScore
    if (score <= minScore):
        return -1
    elif (score >= maxScore):
        return 1
    else:
        return 0

def makeAnswer():
    ind = rand.randint(0, reader.getNumResults(fn) - 1)
    name = str(getSong(ind)["name"])
    artist = str(getSong(ind)["artist"])
    return name, artist

def doGuess():
    global score
    print(f"Score = {score}")
    name, artist = makeAnswer()
    nam = ""
    for i in range(howManyLettersOfName):
        nam += name[i]
    inp = input(print(f"{nam} by {artist}"))
    inp = inp.lower()
    name = name.lower()
    inp.replace("'", "")
    inp.replace(",", "")
    inp.replace(".", "")
    if (str(inp) == name):
        score += 1
        print("Good Job!")
    else:
        score -= 1
        print("Incorrect")

def main():
    while True:
        doGuess()
        print(str(checkScore()))
        if (checkScore() != 0):
            break

    print(f"Game over, Score = {score}")

def getSong(index):
    return reader.read(fn)["songs"][index]

if (__name__ == "__main__"):
    main()