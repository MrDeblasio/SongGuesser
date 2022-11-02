import reader
import json
# Use this script to create content for the app.

fileName = "example.json" # edit this line to change the file, important

def AddSong(name, artist):
    print(str(reader.appendsong(fileName, name, artist)))

# to remove a song, edit the json directly. sorry I couldn't handle the insanity
   
if (__name__ == "__main__"):
    inp1 = input("Please type the name of the song > ")
    inp2 = input("Please type the artist of the song > ")
    print("Thank you, please check the .JSON file to confirm.")
    AddSong(str(inp1), str(inp2))