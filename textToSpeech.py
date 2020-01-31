

from gtts import gTTS
import pyglet

print("""\033[1m\033[91m 
        _   _ _ _       _       _   _ _      _
       | | | (_) |_ ___| |__   | | | (_) ___| | _____ _ __
       | |_| | | __/ __| '_ \  | |_| | |/ __| |/ / _ \ '__|
       |  _  | | || (__| | | | |  _  | | (__|   <  __/ |
       |_| |_|_|\__\___|_| |_| |_| |_|_|\___|_|\_\___|_|   """)
mytext = ""
language = 'en'
with open("text.txt","r") as file:
    for line in file:
        mytext = mytext + line
speech = gTTS(text="this is made by hitch hicker"+" "+mytext, lang=language, slow=False)

speech.save("Speech.mp3")

music = pyglet.resource.media('Speech.mp3',streaming=False)
music.play()
pyglet.app.run()
