# SongGuesser
Computing project gone wild

[How to Use](#how-to-use)<br>
[Authentication](#authentication)<br>
[Authentication: Resetting Key](#resetting-your-key)<br>
[Authentication: Changing Key](#changing-your-key)<br>
[Notes](#notes)<br>
[Exporting Song Lists](#how-to-export-your-own-songs-for-people-to-play)<br>
[Importing Song Lists](#how-to-import-others-songs)

# How to use:
- (optional) Edit the **"fileName"** variable in **"creator.py"** to your custom file
- Run **"creator.py"** as many times as you need to add your songs
- (optional) Edit the **"fileName"** variable in **"main.py"** to your custom file
- Run **"main.py"** and play the game.

# Notes
- You don't have to change the file name in any script **(if you're okay with overriding song lists)**, **however if you change it for one you have to change it for both**.
- You can also change the **"howManyLettersOfName"** variable in **"main.py"** to change how many letters are revealed for each word.

# Authentication
- If it is the first time entering a key, any key will work, and it will write the key to the file **"secret.txt"**.
- # Resetting your key
- Open **"secret.txt"** and clear the file
- # Changing your key
- Open **"secret.txt"** and change the text to what you want the key to be.
- Making sure the new key is **one line long** and **has minimal special characters** will reduce the risk of an error.

# How to export your own songs for people to play:
- **REQUIRED**: In **"creator.py"**, change the **"fileName"** variable to something unique, maybe try your name.
If you do not change the **"fileName"** variable, you will overwrite an existing song list.
- Use the **"creator.py"** script to make your own list, you have to run it multiple times to get multiple songs.
- Go to the directory of the project, this will usually be in downloads.
- Find a file with the same name as the one you named in **"creator.py"**
- Share this file in any way, such as Discord, Teams or Google Drive.
- For instructions on how to load the exported file, [see instructions below.](#how-to-import-others-songs)

# How to import others' songs
- **REQUIRED**: In **"main.py"**, change the **"fileName"** variable to the name of the downloaded file.
If you do not change the **"fileName"** variable, you will overwrite an existing song list.
- Launch the script, and you should have the shared file.

Follow instructions or dont complain :D
