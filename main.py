from videocreation.script import scriper
from videocreation.videoEdit import editor
import time
from utils.fileCheckers import mkDir
import json
import os

print("-------------Welcome to the TripTricks bot for TikTok-------------\n")
print("This bot will help you create a video based on a trip destination\n")

#f = open('/Users/evanflament/Documents/Git-Projects/TripsVideoMakerBot/videocreation/data/CityBank.json')
absolute_path = os.path.dirname(__file__)
relative_path = "videocreation/data/CityBank.json"
full_path = os.path.join(absolute_path, relative_path)
f = open(full_path)
data = json.load(f)
num = len(data)
available_destinations = []
print("Currently supported cities:\n")
for i in range(num):
    #print(data[i]['city'])
    available_destinations.append(data[i]['city'])
    print(f"{i+1} - {available_destinations[i]}")
#print("\n")
destination = input("Choice (1/2/..): ")
destination = available_destinations[int(destination)-1]
print(f"Your choice: {destination}")


time.sleep(0.5)
print("\n")
print(f"-------------Downloading videos for {destination}-------------\n")
scriper(destination)
editor()



""" dirname = os.path.dirname("videocreation")
f = open(os.path.join(dirname, 'data/CityBank.json'))
data = json.load(f)
print(type(data))
num = len(data)
print(num) """
""" print("Destination name: ")

destination = input()

print("input:" + destination + "\n")

mkDir("./assets")
mkDir("./assets/images")

scriper(destination)
 """



