import json
import os

#
#
#   DO NOT EDIT: critical infrastructure
#   if you do edit it and complain it doesn't work that's your fault
#
#

def read(url):
    f = open(url)
    if (os.stat(url).st_size == 0):
        c(f)
        return f
    data = json.load(f)
    c(f)
    return data

def appendsong(url, name, artist):
    f = open(url, "a")
    if (os.stat(url).st_size == 0):
        dict1 = {"songs": []}
        json.dump(dict1, f)
        c(f)

    name.replace("'", "")
    name.replace(",", "")
    name.replace(".", "")
    a = {"name": name, "artist": artist}
    f = open(url, "r")
    data = json.load(f)
    c(f)
    data["songs"].append(a)
    f = open(url, "w")
    json.dump(data, f)
    c(f)
    f = open(url, "r")
    d = json.load(f)
    c(f)
    return d

def getNumResults(url):
    data = read(url)
    return len(data["songs"])

def create(url):
    f = open(url, "a")
    c(f)
    return f

def c(f):
    f.close