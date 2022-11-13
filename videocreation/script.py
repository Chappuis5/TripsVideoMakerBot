import json
from videoMaker.voice import TTS
from videoMaker.YtbScraper import ytbScraper
import os


def scriper_multi_vids(input_story, input_country):
    absolute_path = os.path.dirname(__file__)
    relative_path = "data/country_stories.json"
    full_path = os.path.join(absolute_path, relative_path)
    f = open(full_path)
    data = json.load(f)

   # print(data[input_country]['stories'][input_story]['title'])
    for i in range(len(data[input_country]['stories'][input_story]['strings'])):
        #print(data[input_country]['stories'][input_story]['strings'][i][f"str_{i}"])

        str = data[input_country]['stories'][input_story]['strings'][i][f"str_{i}"]
        keyword = data[input_country]['stories'][input_story]['videos'][i][f"video_{i}"]
        TTS(str, f"sound_{i}")
        ytbScraper(keyword, f"video_{i}")
            


#f.close()

def scriper_single_vid(input_story, input_country):
    absolute_path = os.path.dirname(__file__)
    relative_path = "data/country_stories.json"
    full_path = os.path.join(absolute_path, relative_path)
    f = open(full_path)
    data = json.load(f)
    str = data[input_country]['stories'][input_story]['strings'][0][f"str_{0}"]
    TTS(str, f"sound_{0}")
   
