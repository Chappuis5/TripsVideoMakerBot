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
    #absolute_path = os.path.dirname(__file__)
    #relative_path = f"assets/images/image_{index}.jpg"
    directory = f"images/image_{index}.jpg"
    parent_dir = "./assets"
    full_path = os.path.join(parent_dir, directory)
    with open(full_path, "wb") as file:
        # get request
        response = requests.get(url)
        # write to file
        file.write(response.content)


def imageToVid(video_object, index):
    #absolute_path = os.path.dirname(__file__)
    #relative_path_video = f"assets/backgrounds/video_{index}.mp4"
    #file_video = f"video_{index}.mp4"
    #parent_dir = "./assets/backgrounds/"
    #full_path_video = os.path.join(parent_dir, file_video)
    #relative_path_image = f"assets/images/image_{index}.jpg"
    file_image= f"image_{index}.jpg"
    parent_dir_im = "./assets/images/"
    full_path_image = os.path.join(parent_dir_im, file_image)
    #video = VideoFileClip(full_path_video)
    img = (mp.ImageClip(full_path_image)
            .set_duration(video_object.duration)
            .resize(height=700) # if you need to resize...
            .margin(right=8, top=8, opacity=0) # (optional) logo-border padding
            .set_pos(("center","center")))

    video_image_object = mp.CompositeVideoClip([video_object, img])
    #os.rename(full_path_video, os.path.join(parent_dir, f"trash_{index}.mp4"))
    #final.write_videofile(full_path_video)
    #os.remove(os.path.join(parent_dir, f"trash_{index}.mp4"))
    return video_image_object
