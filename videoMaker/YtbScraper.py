from pytube import Search
from pytube import YouTube
from pytube import *
import pytube.exceptions as exceptions
from typing import Tuple
import os, shutil

def mkDir(path):
    if os.path.isdir(path):
        #print("...directory exist...")
        return True
    else:
        os.mkdir(path)
        #print("Directory created")
        return False

##(parameters) keyword : keyword for searching video, name : output filename
def ytbScraper (keyword, name):
    #background_config: Tuple[str, str, str, Any]
    #Path("./assets/backgrounds/").mkdir(parents=True, exist_ok=True)
    directory = "backgrounds"
    parent_dir = "./assets"
    path = os.path.join(parent_dir, directory)
    mkDir(path)
    if mkDir(path) == True:
        s = Search(keyword)# Get first batch of videos
        i = 0
        while (int(s.results[i].vid_info.get('videoDetails', {}).get('lengthSeconds'))) > 600 or int(s.results[i].vid_info.get('videoDetails', {}).get('lengthSeconds')) < 50 or resolutionChecker(s.results[i].watch_url) == False:
            i += 1
            print(i)
            if(len(s.results) == i): #If it didn't find any good videos, it gets a new batch of videos
                s.get_next_results()
                print("No correct videos found, fetching more...")
        print("Video found !")
        url = s.results[i].watch_url
        print(s.results[i].watch_url)
        #print("Downloading video...")
        yt = YouTube(url, use_oauth=True, allow_oauth_cache=True).streams.filter(res = "1080p").first().download(path, filename=f"{name}.mp4")
        #print("Video downloaded.")
        
    else: 
        mkDir(path)
        s = Search(keyword)
        i = 0
        while (int(s.results[i].vid_info.get('videoDetails', {}).get('lengthSeconds'))) > 600 or int(s.results[i].vid_info.get('videoDetails', {}).get('lengthSeconds')) < 50 or resolutionChecker(s.results[i].watch_url) == False:
            i += 1
            print(i)
            if(len(s.results) == i):
                s.get_next_results()
                print("No correct videos found, fetching more...")
        print("Video found !")
        url = s.results[i].watch_url
        print(s.results[i].watch_url)
        #print("Downloading video...")
        yt = YouTube(url, use_oauth=True, allow_oauth_cache=True).streams.filter(res = "1080p").first().download(path, filename=f"{name}.mp4")
        #print("Video downloaded.")
        

def resolutionChecker(url):
    my_video = YouTube(url)
    video_resolutions = []
    try:
        for stream in my_video.streams.order_by('resolution'):
            video_resolutions.append(stream.resolution)
    except Exception:
        print("VIDEO BUGGE")
        return False
    for i in range(0, len(video_resolutions)):
        if video_resolutions[i] == "1080p":
            return True
        else:
            continue
    print("No 1080p")
    return False

#resolutionChecker("https://www.youtube.com/watch?v=5v47lgLLm5I")

