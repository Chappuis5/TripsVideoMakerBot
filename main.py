from videocreation.script import scriper
from videocreation.videoEdit import editor
import time
from utils.fileCheckers import mkDir, rmDir
import json
import os, shutil
from subtitles import subMaker

print("-------------Welcome to the TripTricks bot for TikTok-------------\n")
print("This bot will help you create a video based on a trip destination\n")

absolute_path = os.path.dirname(__file__)
relative_path = "videocreation/data/country_stories.json"
full_path = os.path.join(absolute_path, relative_path)
f = open(full_path)
data = json.load(f)
num = len(data)
available_countries = []
print("Currently supported cities:\n")
for i in range(num):
    print(data[i]['country'])
    available_countries.append(data[i]['country'])
    print(f"{i+1} - {available_countries[i]}")

while True:
    try:
        input_country = int(input("Choice (1/2/..): "))
    except ValueError:
        print("Please enter a number")
        continue
    if input_country <= 0 or input_country > num:
        print("Out of range")
        continue
    else:
        break
    
country = available_countries[int(input_country)-1]
input_country = int(input_country)-1
print(f"Your choice: {country}")
print("\n")
print(f"-------------Available stories for {country}-------------\n")
available_stories = []
num_stories = len(data[input_country]['stories'])
for i in range(num_stories):
    #print(data[country]['stories'][i])
    available_stories.append(data[input_country]['stories'][i]['title'])
    print(f"{i+1} - {available_stories[i]}")

while True:
    try:
        input_story = int(input("Choice (1/2/..): "))
    except ValueError:
        print("Please enter a number")
        continue
    if input_story <= 0 or input_story > num_stories:
        print("Out of range")
        continue
    else:
        break

story = available_stories[int(input_story)-1]
input_story = int(input_story)-1
#print(story)
#print(data[input_country]['stories'][input_story]['str_0'])

rmDir("./assets")
time.sleep(0.5)
mkDir("./assets")
mkDir("./assets/images")
print("\n")
print(f"-------------Downloading videos for {story}-------------\n")
scriper(input_story, input_country)
editor(input_story, input_country)
mkDir("./output")
mkDir(f"./output/{country}")
subMaker(story, country)
shutil.rmtree("./assets")
os.system("echo clear")
print("-------------Video created!-------------\n")
print(f"---------./output/final_{story}---------")




