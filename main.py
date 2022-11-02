import reader
import json
import random
import time
from datetime import datetime

fileName = "example.json"  # IMPORTANT: If you've made a custom setup using 'creator.py', change this file to the filename you use there.
rand = random.Random()

score = 0
maxScore = 10
minScore = -1

howManyLettersOfileNameame = 2


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
    ind = rand.randint(0, reader.getNumResults(fileName) - 1)
    name = str(getSong(ind)["name"])
    artist = str(getSong(ind)["artist"])
    return name, artist


def doGuess():
    global score
    print(f"Score = {score}")
    name, artist = makeAnswer()
    nam = ""
    names = name.split(" ")
    for x in range(len(names)):
        for i in range(howManyLettersOfileNameame):
            nam += names[x][i]

        nam += " "

    inp = input(print(f"{nam}by {artist}"))
    inp = inp.lower()
    name = name.lower()
    name = name.replace(" ", "")
    inp = inp.replace("'", "")
    inp = inp.replace(",", "")
    inp = inp.replace(".", "")
    inp = inp.replace(" ", "")
    if (str(inp) == name):
        score += 2
        print("Good Job!")
    else:
        inp = input(print("Incorrect, please retry"))
        inp = inp.lower()
        name = name.lower()
        inp.replace("'", "")
        inp.replace(",", "")
        inp.replace(".", "")
        if (str(inp) == name):
            score += 1
            print("Good Job!")
        else:
            print(f"Still incorrect. The correct answer was {name}.")
            score -= 1




def getSetAndDisplayScores(t1, name):
    global score
    t2 = time.time()
    print(f"Game over, Score = {score}")
    t = t2 - t1
    ct = time.time()
    readableTime = datetime.fromtimestamp(ct).strftime("%m/%d/%Y, %H:%M:%S")
    data = reader.setAndReadScores(name, score, ct, t)

    for i in range(len(data["scores"])):
        if (float(data["scores"][i]["date"]) == ct):
            print(f"{name}'s score (you): {score}; Taken at {readableTime}; Time Taken: {t}")

    for i in range(len(data["scores"])):
        if (float(data["scores"][i]["date"]) != ct):
            dt = datetime.fromtimestamp(data["scores"][i]["date"])
            dt = dt.strftime("%m/%d/%Y, %H:%M:%S")
            print(f'Player: {data["scores"][i]["name"]}, Score: {data["scores"][i]["score"]}; Taken at {dt}; Time Taken: {(round(float(data["scores"][i]["timetaken"]), 2))}')

def main():
    name = input("Please enter your name > ")

    if (fileName == "example.json"):
        print("You are playing with a list with 15 of Virgin Radio Dubai's top 41 songs for 2021.")

    t1 = time.time()
    while True:
        doGuess()
        if (checkScore() != 0):
            break

    getSetAndDisplayScores(t1, name)


def getSong(index):
    return reader.read(fileName)["songs"][index]


if (__name__ == "__main__"):
    main()
