import json
import random
from videoMaker.voice import TTS
from videoMaker.voice import gTTS
from videoMaker.YtbScraper import ytbScraper
import os
from videoMaker.image2vid import imageToVid, imageDownloader
###


def scriper(input_story, input_country):
    absolute_path = os.path.dirname(__file__)
    relative_path = "data/country_stories.json"
    full_path = os.path.join(absolute_path, relative_path)
    f = open(full_path)
    data = json.load(f)

    print(data[input_country]['stories'][input_story]['title'])

    for i in range(len(data[input_country]['stories'][input_story]['strings'])):
        print(data[input_country]['stories'][input_story]['strings'][i][f"str_{i}"])

        str = data[input_country]['stories'][input_story]['strings'][i][f"str_{i}"]
        keyword = data[input_country]['stories'][input_story]['videos'][i][f"video_{i}"]
        TTS(str, f"sound_{i}")
        ytbScraper(keyword, f"video_{i}")
        """ if(data[input_country]['stories'][input_story]['images'][i][f"image_{i}"] != ""):
            print("url image :", data[input_country]['stories'][input_story]['images'][i][f"image_{i}"])
            imageDownloader(data[input_country]['stories'][input_story]['images'][i][f"image_{i}"], i)
            imageToVid(i) """

        
      
     

#f.close()

