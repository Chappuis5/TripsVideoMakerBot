import pytube
import json
import os

def mkDir(path):
    if os.path.isdir(path):
        #print("...directory exist...")
        return True
    else:
        os.mkdir(path)
        #print("Directory created")
        return False

def video_downloader(url, path, title):
    yt = pytube.YouTube(url)
    stream = yt.streams.filter(res="1080p").first()
    stream.download(path, filename=f"{title}.mp4")
