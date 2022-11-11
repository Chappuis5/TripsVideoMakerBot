import pvleopard
import os
import ffmpeg
from ffmpeg import *
from typing import *

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

def to_srt(
        words: Sequence[pvleopard.Leopard.Word],
        endpoint_sec: float = 1.,
        length_limit: Optional[int] = 1) -> str:
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


def subMaker(story, country):
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
        f.write(to_srt(words)) 

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
    while(os.path.exists(final_video_path)):
        video_index += 1
        final_video_path = f"./output/{country}/final_{story}_{video_index}.mp4"
       
    ffmpeg.concat(video.filter("subtitles", full_path4, force_style='Fontsize=22,Fontname=Impact,PrimaryColour=&H00FFFFFF,Italic=1,Bold=0,Outline=2,OutlineColour=&H00000000,BorderStyle=1,Alignment=2,MarginV=145'), audio, v=1, a=1).output(final_video_path).run()   
    

subMaker("Enigma", country="United Kingdom" )