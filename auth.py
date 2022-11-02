import os

def getSecret(secret):
    f = open("secret.txt", "a")
    if (os.stat("secret.txt").st_size == 0):
        f.write(str(secret))
    f.close()
    f = open("secret.txt", "r")
    data = f.read()
    f.close()
    return data

def authenticate(secret):
    auth = getSecret(secret)
    if (secret == auth):
        return True
    else:
        return False