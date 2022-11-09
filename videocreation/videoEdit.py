from moviepy.editor import *
import os

for filename in os.listdir(path="./assets/audio"):
    if filename.endswith(".mp3"):
        print(filename)
        continue
    else:
        continue
