from moviepy.editor import *
import os
import time
import sys
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import cv2
import random

def mkDir(path):
    if os.path.isdir(path):
        print("...directory exist...")
        return True
    else:
        os.mkdir(path)
        print("Directory created")
        return False

def getvidDuration(filename):
    clip = VideoFileClip(filename)
    duration = clip.duration
    return duration

def getsoundDuration(filename):
    clip = AudioFileClip(filename)
    duration = clip.duration
    return duration
    
def videoCroper(interval, filename):
    duration = getvidDuration(filename)
    print("Duration of the video: " + str(duration))

    video = VideoFileClip(filename)
    start_time = (random.randint(10, int(duration-interval-10)))
    clip = video.subclip(start_time, start_time + interval)
    return clip

def concatenate_audio_moviepy(audio_clip_paths, output_path):
    """Concatenates several audio files into one audio file using MoviePy
    and save it to `output_path`. Note that extension (mp3, etc.) must be added to `output_path`"""
    clips = [AudioFileClip(c) for c in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile(output_path)

list = []
for sound in os.listdir("./assets/audio"):
    #print(sound)
    list.append(sound)
s_num = len(list)

list_sound =[]
for i in range (0, s_num):
    list_sound.append(f"./assets/audio/sound_{i}.mp3")

mkDir("./assets/finalAudio")





mkDir("./assets/edited")
""" for i in range(0, s_num):
    print(i)
    videoCroper(getsoundDuration(f"./assets/audio/sound_{i}.mp3"), f"./assets/backgrounds/New-York/video_{i}.mp4").set_audio(AudioFileClip(f"./assets/audio/sound_{i}.mp3")).write_videofile(f"./assets/edited/{i}.mp4", codec='libx264', audio_codec='aac')
    print(f"Video {i} edited.")
    time.sleep(1)  """ 

def concatenate(video_clip_paths, output_path, method="compose"):
    """Concatenates several video files into one video file
    and save it to `output_path`. Note that extension (mp4, etc.) must be added to `output_path`
    `method` can be either 'compose' or 'reduce':
        `reduce`: Reduce the quality of the video to the lowest quality on the list of `video_clip_paths`.
        `compose`: type help(concatenate_videoclips) for the info"""
    # create VideoFileClip object for each video file
    clips = [VideoFileClip(c) for c in video_clip_paths]
    if method == "reduce":
        # calculate minimum width & height across all clips
        min_height = min([c.h for c in clips])
        min_width = min([c.w for c in clips])
        # resize the videos to the minimum
        clips = [c.resize(newsize=(min_width, min_height)) for c in clips]
        # concatenate the final video
        final_clip = concatenate_videoclips(clips)
    elif method == "compose":
        # concatenate the final video with the compose method provided by moviepy
        final_clip = concatenate_videoclips(clips, method="compose")
    # write the output video file
    final_clip.write_videofile(output_path)




listF = []
for i in os.listdir("./assets/edited"):
    listF.append(i)
f_num = len(listF)
print(f_num)

mkDir("./assets/final") 

list_video = []
for i in range (0, f_num):
    list_video.append(f"./assets/edited/{i}.mp4")

print(list_video)

concatenate_audio_moviepy(list_sound, "./assets/finalAudio/final.mp3")
concatenate(list_video, "./assets/final/final.mp4", method="compose")



VideoFileClip("./assets/final/final.mp4").set_audio(AudioFileClip("./assets/finalAudio/final.mp3")).write_videofile("./assets/final/final_video.mp4", codec='libx264', audio_codec='aac')



