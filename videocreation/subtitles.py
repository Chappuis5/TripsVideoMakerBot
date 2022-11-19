import pvleopard
import os
import ffmpeg
from ffmpeg import *
from typing import *
import json

def mkDir(path):
    if os.path.isdir(path):
        return True
    else:
        os.mkdir(path)
        return False

def second_to_timecode(x: float) -> str:
    hour, x = divmod(x, 3600)
    minute, x = divmod(x, 60)
    second, x = divmod(x, 1)
    millisecond = int(x * 1000.)

    return '%.2d:%.2d:%.2d,%.3d' % (hour, minute, second, millisecond)

def to_srt(length_limit, endpoint_sec,
        words: Sequence[pvleopard.Leopard.Word]) -> str:
        #endpoint_sec: float = 0.5) -> str:
        #length_limit: Optional[int] = 4) -> str:
    def _helper(end: int) -> None:
        lines.append("%d" % section)
        lines.append(
            "%s --> %s" %
            (
                second_to_timecode(words[start].start_sec),
                second_to_timecode(words[end].end_sec)
            )
        )
        lines.append(' '.join(x.word for x in words[start:(end + 1)]))
        lines.append('')

    lines = list()
    section = 0
    start = 0
    for k in range(1, len(words)):
        if ((words[k].start_sec - words[k - 1].end_sec) >= endpoint_sec) or \
                (length_limit is not None and (k - start) >= length_limit):
            _helper(k - 1)
            start = k
            section += 1
    _helper(len(words) - 1)

    return '\n'.join(lines)



def subMakerLower(story, country, bold, italic,outline_width, font, font_size, pm_transp, out_transp, border_style, margin, length_limit, endpoint_sec):
    leopard = pvleopard.create(access_key="JHRxxr3akK4RilsSIOyULG8IMwwmbMQX6fLcTeB2yXgXSsDWcexbdA==")

    file = "final.mp3"
    parent_dir = "./assets/finalAudio/"
    full_path = os.path.join(parent_dir, file)
    transcript, words = leopard.process_file(full_path)


    ### CREATE SUBTITLES.SRT
    mkDir("./assets/subtitles")
    parent_dir1 = "./assets/subtitles/"
    file1 = "subtitles.srt"
    with open(os.path.join(parent_dir1, file1), 'w') as f:
        f.write(to_srt(length_limit, endpoint_sec, words)) 
    
    dir = "subtitles"
    path = "./assets/"
    full_path2 = os.path.join(path, dir)

    ## To lower case ##
    for filename in os.listdir(full_path2):
        if filename.endswith(".srt"):
            os.rename(os.path.join(full_path2, filename), os.path.join(full_path2, filename.replace(".srt", ".txt")))
            
    txt_file = open(os.path.join(full_path2, filename.replace(".srt", ".txt")), 'r')
    for x in txt_file.read():
        y = x.lower()
        txt_file_upper = open(os.path.join(full_path2, "subtitles_down.txt"), 'a')
        txt_file_upper.write(y)
        txt_file_upper.close()
    txt_file.close()
    os.remove(os.path.join(full_path2, filename.replace(".srt", ".txt")))


    for name in os.listdir(full_path2):
        if name.endswith(".txt"):
            os.rename(os.path.join(full_path2, name), os.path.join(full_path2, name.replace(".txt", ".srt")))

    semi_final_video = "final_clip.mp4"
    parent_dir2 = "./assets/final/"
    full_path3 = os.path.join(parent_dir2, semi_final_video)
    full_path_test = "./assets/final/final_clip.mp4"
    #up_sub = "subtitles_up.srt"
    down_sub = "subtitles_down.srt"
    parent_dir3 =  "assets/subtitles/"
    full_path4 = os.path.join(parent_dir3, down_sub)

    video = ffmpeg.input(full_path3)
    audio = video.audio
    video_index = 0
    final_video_path = f"./output/{country}/final_{story}_0.mp4"
    while(os.path.exists(final_video_path)):
        video_index += 1
        final_video_path = f"./output/{country}/final_{story}_{video_index}.mp4"

    ffmpeg.concat(video.filter("subtitles", full_path4, force_style=f'Fontsize={font_size},Fontname={font},PrimaryColour=&H{pm_transp}FFFFFF,Italic={italic},Bold={bold},Outline={outline_width},OutlineColour=&H{out_transp}000000,BorderStyle={border_style},Alignment=2,MarginV={margin}'), audio, v=1, a=1).output(final_video_path).run() 

def subMaker(story, country, bold, italic,outline_width, font, font_size, pm_transp, out_transp, border_style, margin, length_limit, endpoint_sec):
    leopard = pvleopard.create(access_key="JHRxxr3akK4RilsSIOyULG8IMwwmbMQX6fLcTeB2yXgXSsDWcexbdA==")

    file = "final.mp3"
    parent_dir = "./assets/finalAudio/"
    full_path = os.path.join(parent_dir, file)
    transcript, words = leopard.process_file(full_path)


    ### CREATE SUBTITLES.SRT
    mkDir("./assets/subtitles")
    parent_dir1 = "./assets/subtitles/"
    file1 = "subtitles.srt"
    with open(os.path.join(parent_dir1, file1), 'w') as f:
        f.write(to_srt(length_limit, endpoint_sec, words)) 
    
    ### SUBTITLES.SRT TO UPPERCASE
    dir = "subtitles"
    path = "./assets/"
    full_path2 = os.path.join(path, dir)

    for filename in os.listdir(full_path2):
        if filename.endswith(".srt"):
            os.rename(os.path.join(full_path2, filename), os.path.join(full_path2, filename.replace(".srt", ".txt")))
            
    txt_file = open(os.path.join(full_path2, filename.replace(".srt", ".txt")), 'r')
    for x in txt_file.read():
        y = x.upper()
        txt_file_upper = open(os.path.join(full_path2, "subtitles_up.txt"), 'a')
        txt_file_upper.write(y)
        txt_file_upper.close()
    txt_file.close()
    os.remove(os.path.join(full_path2, filename.replace(".srt", ".txt")))
    

    for name in os.listdir(full_path2):
        if name.endswith(".txt"):
            os.rename(os.path.join(full_path2, name), os.path.join(full_path2, name.replace(".txt", ".srt")))

    semi_final_video = "final_clip.mp4"
    parent_dir2 = "./assets/final/"
    full_path3 = os.path.join(parent_dir2, semi_final_video)
    full_path_test = "./assets/final/final_clip.mp4"
    
    up_sub = "subtitles_up.srt"
    parent_dir3 =  "assets/subtitles/"
    full_path4 = os.path.join(parent_dir3, up_sub)

    video = ffmpeg.input(full_path3)
    audio = video.audio
    video_index = 0
    final_video_path = f"./output/{country}/final_{story}_0.mp4"
    lol_path = os.path.join(f"./output/{country}/", f"final_final_{story}_0.mp4") 
    while(os.path.exists(final_video_path)):
        video_index += 1
        final_video_path = f"./output/{country}/final_{story}_{video_index}.mp4"
    
    ffmpeg.concat(video.filter("subtitles", full_path4, force_style=f'Fontsize={font_size},Fontname={font},PrimaryColour=&H{pm_transp}FFFFFF,Italic={italic},Bold={bold},Outline={outline_width},OutlineColour=&H{out_transp}000000,BorderStyle={border_style},Alignment=2,MarginV={margin}'), audio, v=1, a=1).output(final_video_path).run() 
    #video2 = ffmpeg.input(final_video_path)
    #audio2 = video2.audio
    #ffmpeg.concat(video2.filter("subtitles", full_path4 , force_style=f'Fontsize={font_size},Fontname={font},PrimaryColour=&H{pm_transp}FFFFFF,Italic={italic},Bold={bold},Outline={outline_width},OutlineColour=&H{out_transp}000000,BorderStyle={border_style},Alignment=2,MarginV=55'), audio2, v=1, a=1).output(lol_path).run() 

#def CheckIfOtherSubtitlesPosition():
""" country = "Reddit stories"
story = "15_11_03"
up_or_down = "up"
data = json.load(open("./videocreation/data/country_stories.json"))
for i in range(len(data)):
    if data[i]["country"] == country:
        for j in range(len(data[i]["stories"])):
            if data[i]["stories"][j]["title"] == story:
                #print(data[i]["stories"][j])
                if len(data[i]['stories'][j]['strings'][0]) == 1 and data[i]['stories'][j]['strings'][0] == "":
                    print("No sub subtitles found")
                else: 
                    print(len(data[i]['stories'][j]['strings']))
                    # create .srt
                    sub_parent_dir = "./assets/subtitles/"
                    sub_file = "sub_subtitles.srt"
                    with open(os.path.join(sub_parent_dir, sub_file), 'w') as f:
                        f.write(to_srt(length_limit, endpoint_sec, words)) 
                    if up_or_down == "up":

                #for z in range(len(data[i]['stories'][j]['strings'])) """
                

   
        
        


