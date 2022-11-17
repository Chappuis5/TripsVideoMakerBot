import os
import requests
import moviepy.editor as mp
from moviepy.editor import *

def mkDir(path):
    if os.path.isdir(path):
        #print("...directory exist...")
        return True
    else:
        os.mkdir(path)
        #print("Directory created")
        return False

def imageDownloader(url, index):
    directory = f"images/image_{index}.jpg"
    parent_dir = "./assets"
    full_path = os.path.join(parent_dir, directory)
    with open(full_path, "wb") as file:
        # get request
        response = requests.get(url)
        # write to file
        file.write(response.content)


def imageToVid(video_object, index):
    file_image= f"image_{index}.jpg"
    parent_dir_im = "./assets/images/"
    full_path_image = os.path.join(parent_dir_im, file_image)
    #video = VideoFileClip(full_path_video)
    img = (mp.ImageClip(full_path_image)
            .set_duration(video_object.duration)
            .resize(height=700) # if you need to resize...
            .margin(right=8, top=8, opacity=0) # (optional) logo-border padding
            .set_pos(("center","center")))
    w = img.size[0] #2000 on veut
    img = img.crop(x_center = w/2, width = 400)
    video_image_object = mp.CompositeVideoClip([video_object, img])
    return video_image_object
