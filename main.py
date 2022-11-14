from videocreation.script import scriper_multi_vids, scriper_single_vid
from videocreation.videoEdit import editor
import time
from utils.fileCheckers import mkDir, rmDir, checkFile, fileRenamer
from utils.configure import checkConfig
import json
import os, shutil
from videocreation.subtitles import subMaker, subMakerLower
from videoMaker.single_vid_d import video_downloader
import toml

print("-------------Welcome to the TripTricks bot for TikTok-------------\n")
print("This bot will help you create a video based on a trip destination\n")

absolute_path = os.path.dirname(__file__)
relative_path = "videocreation/data/country_stories.json"
full_path = os.path.join(absolute_path, relative_path)
f = open(full_path)
data = json.load(f)
num = len(data)
available_countries = []
print("Currently supported countries:\n")
for i in range(num):
    available_countries.append(data[i]['country'])
    print(f"{i+1} - {available_countries[i]}")

while True:
    try:
        input_country = int(input("Choice (1/2/..): "))
    except ValueError:
        print("Please enter a number")
        continue
    if input_country <= 0 or input_country > num:
        print("Out of range")
        continue
    else:
        break
    
country = available_countries[int(input_country)-1]
input_country = int(input_country)-1
print(f"Your choice: {country}")
print("\n")
print(f"-------------Available stories for {country}-------------\n")
available_stories = []
num_stories = len(data[input_country]['stories'])
for i in range(num_stories):
    #print(data[country]['stories'][i])
    available_stories.append(data[input_country]['stories'][i]['title'])
    print(f"{i+1} - {available_stories[i]}")

while True:
    try:
        input_story = int(input("Choice (1/2/..): "))
    except ValueError:
        print("Please enter a number")
        continue
    if input_story <= 0 or input_story > num_stories:
        print("Out of range")
        continue
    else:
        break

story = available_stories[int(input_story)-1]
input_story = int(input_story)-1

#print(story)
#print(data[input_country]['stories'][input_story]['str_0'])

rmDir("./assets")
mkDir("./assets")
mkDir("./assets/images")
print("Checking exiting config.toml....")
checkConfig()
print("\n")
if len(data[input_country]['stories'][input_story]['strings']) == 1:
    print("The story you've selected only has one string.\n")
    print("Do you want to edit with a video from the database? (y/n)")
    while True:
        try:
            input_choice = input("Choice (y/n): ")
        except ValueError:
            print("Please enter a number")
            continue
        if input_choice != "y" and input_choice != "n":
            print("Please enter y or n")
            continue
        elif input_choice == "y":
            print("\n")
            print("-------------Available categories-------------\n")
            absolute_path_backgrounds = os.path.dirname(__file__)
            relative_path_backgrounds = "videocreation/data/backgrounds.json"
            full_path_backgrounds = os.path.join(absolute_path_backgrounds, relative_path_backgrounds)
            f_b = open(full_path_backgrounds)
            data_b = json.load(f_b)
            num_b = len(data_b)
            available_tags = []
            for i in range(num_b):
                available_tags.append(data_b[i]['tag'])
                print(f"{i+1} - {available_tags[i]}")
            while True:
                try:
                    input_tag = int(input("Choice (1/2/..): "))
                except ValueError:
                    print("Please enter a number")
                    continue
                if input_tag <= 0 or input_tag > num_b:
                    print("Out of range")
                    continue
                else:
                    break
            print("\n")
            print("-------------Available videos-------------\n")
            num_videos = len(data_b[input_tag-1]['videos'])
            selected_tag_index = int(input_tag)-1
            available_videos = []
            for i in range(num_videos):
                available_videos.append(data_b[input_tag-1]['videos'][i]['title'])
                print(f"{i+1} - {available_videos[i]}")
            while True:
                try:
                    input_video = int(input("Choice (1/2/..): "))
                    
                except ValueError:
                    print("Please enter a number")
                    continue
                if input_video <= 0 or input_video > num_videos:
                    print("Out of range")
                    continue
                else:
                    break
            print("\n")
            mkDir("./backgrounds")
            mkDir(f"./backgrounds/{data_b[selected_tag_index]['tag']}")
            background_selected_path = os.path.join(f"./backgrounds/{data_b[selected_tag_index]['tag']}/", f"{data_b[selected_tag_index]['videos'][input_video-1]['title']}.mp4")
            print(f"./backgrounds/{data_b[selected_tag_index]['tag']}/")
            print(f"{data_b[selected_tag_index]['videos'][input_video-1]['title']}")
            if checkFile(background_selected_path):
                print("File already exists")
                fileRenamer(background_selected_path,f"./backgrounds/{data_b[selected_tag_index]['tag']}/", f"{data_b[selected_tag_index]['videos'][input_video-1]['title']}.mp4", "video_0.mp4")
                scriper_single_vid(input_story, input_country)
                back_video_path = os.path.join(f"./backgrounds/{data_b[selected_tag_index]['tag']}/", "video_0.mp4")
                editor(input_story, input_country, 0, back_video_path)
                mkDir("./output")
                mkDir(f"./output/{country}")
                print("Do you want to add uppercase subtitles or lowercase subtitles?")
                print("1 - Uppercase")
                print("2 - Lowercase")
                while True:
                    try:
                        input_subtitle = int(input("Choice (1/2): "))
                    except ValueError:
                        print("Please enter a number")
                        continue
                    if input_subtitle <= 0 or input_subtitle > 2:
                        print("Out of range")
                        continue
                    elif input_subtitle == 1:
                        print("Uppercase")
                        config_data = toml.load("config.toml")
                        subMaker(story, country, config_data['settings']['bold'], config_data['settings']['italic'], config_data['settings']['font'], config_data['settings']['font_size'], config_data['settings']['pm_transp'], config_data['settings']['out_transp'], config_data['settings']['border_style'], config_data['settings']['margin'],config_data['settings']['length_limit'], config_data['settings']['endpoint_sec'] )
                        break

                    elif input_subtitle == 2:
                        config_data = toml.load("config.toml")
                        subMakerLower(story, country, config_data['settings']['bold'], config_data['settings']['italic'], config_data['settings']['font'], config_data['settings']['font_size'], config_data['settings']['pm_transp'], config_data['settings']['out_transp'], config_data['settings']['border_style'], config_data['settings']['margin'],config_data['settings']['length_limit'], config_data['settings']['endpoint_sec'] )
                        break
                    else:
                        break
                shutil.rmtree("./assets") ## COMMENT THIS LINE IF ON WINDOWS
                new_background_selected_path = os.path.join(f"./backgrounds/{data_b[selected_tag_index]['tag']}/", "video_0.mp4")
                fileRenamer(new_background_selected_path,f"./backgrounds/{data_b[selected_tag_index]['tag']}/","video_0.mp4", f"{data_b[selected_tag_index]['videos'][input_video-1]['title']}.mp4")
                os.system("echo clear")
                print("-------------Video created!-------------\n")
                print(f"---------./output/final_{story}---------")
            else:
                print("Downloading video...")
                video_downloader(data_b[selected_tag_index]['videos'][input_video-1]['url'], f"./backgrounds/{data_b[selected_tag_index]['tag']}/", f"{data_b[selected_tag_index]['videos'][input_video-1]['title']}")
                fileRenamer(background_selected_path,f"./backgrounds/{data_b[selected_tag_index]['tag']}/", f"{data_b[selected_tag_index]['videos'][input_video-1]['title']}.mp4", "video_0.mp4")
                scriper_single_vid(input_story, input_country)
                back_video_path = os.path.join(f"./backgrounds/{data_b[selected_tag_index]['tag']}/", "video_0.mp4")
                editor(input_story, input_country, 0, back_video_path)
                mkDir("./output")
                mkDir(f"./output/{country}")
                print("Do you want to add uppercase subtitle or lowercase subtitles?")
                print("1 - Uppercase")
                print("2 - Lowercase")
                while True:
                    try:
                        input_subtitle = int(input("Choice (1/2): "))
                    except ValueError:
                        print("Please enter a number")
                        continue
                    if input_subtitle <= 0 or input_subtitle > 2:
                        print("Out of range")
                        continue
                    elif input_subtitle == 1:
                        config_data = toml.load("config.toml")
                        subMaker(story, country, config_data['settings']['bold'], config_data['settings']['italic'], config_data['settings']['font'], config_data['settings']['font_size'], config_data['settings']['pm_transp'], config_data['settings']['out_transp'], config_data['settings']['border_style'], config_data['settings']['margin'],config_data['settings']['length_limit'], config_data['settings']['endpoint_sec'] )
                        break
                    elif input_subtitle == 2:
                        config_data = toml.load("config.toml")
                        subMakerLower(story, country, config_data['settings']['bold'], config_data['settings']['italic'], config_data['settings']['font'], config_data['settings']['font_size'], config_data['settings']['pm_transp'], config_data['settings']['out_transp'], config_data['settings']['border_style'], config_data['settings']['margin'],config_data['settings']['length_limit'], config_data['settings']['endpoint_sec'] )
                        break
                    else:
                        break
                shutil.rmtree("./assets") ## COMMENT THIS LINE IF ON WINDOWS
                new_background_selected_path = os.path.join(f"./backgrounds/{data_b[selected_tag_index]['tag']}/", "video_0.mp4")
                fileRenamer(new_background_selected_path,f"./backgrounds/{data_b[selected_tag_index]['tag']}/","video_0.mp4", f"{data_b[selected_tag_index]['videos'][input_video-1]['title']}.mp4")
                os.system("echo clear")
                print("-------------Video created!-------------\n")
                print(f"---------./output/final_{story}---------")

            
            break
        elif input_choice == "n":
            print("\n")
            print(f"-------------Downloading videos for {story}-------------\n")
            scriper_multi_vids(input_story, input_country)
            editor(input_story, input_country)
            mkDir("./output")
            mkDir(f"./output/{country}")
            print("Do you want to add uppercase subtitle or lowercase subtitles?")
            print("1 - Uppercase")
            print("2 - Lowercase")
            while True:
                try:
                    input_subtitle = int(input("Choice (1/2): "))
                except ValueError:
                    print("Please enter a number")
                    continue
                if input_subtitle <= 0 or input_subtitle > 2:
                    print("Out of range")
                    continue
                elif input_subtitle == 1:
                    config_data = toml.load("config.toml")
                    subMaker(story, country, config_data['settings']['bold'], config_data['settings']['italic'], config_data['settings']['font'], config_data['settings']['font_size'], config_data['settings']['pm_transp'], config_data['settings']['out_transp'], config_data['settings']['border_style'], config_data['settings']['margin'],config_data['settings']['length_limit'], config_data['settings']['endpoint_sec'] )
                    break
                elif input_subtitle == 2:
                    config_data = toml.load("config.toml")
                    subMakerLower(story, country, config_data['settings']['bold'], config_data['settings']['italic'], config_data['settings']['font'], config_data['settings']['font_size'], config_data['settings']['pm_transp'], config_data['settings']['out_transp'], config_data['settings']['border_style'], config_data['settings']['margin'],config_data['settings']['length_limit'], config_data['settings']['endpoint_sec'] )
                    break
                else:
                    break
            shutil.rmtree("./assets") ## COMMENT THIS LINE IF ON WINDOWS
            os.system("echo clear")
            print("-------------Video created!-------------\n")
            print(f"---------./output/final_{story}---------")
            break
            
elif len(data[input_country]['stories'][input_story]['strings']) > 1:
    print(f"-------------Downloading videos for {story}-------------\n")
    scriper_multi_vids(input_story, input_country)
    editor(input_story, input_country, 1, "")
    mkDir("./output")
    mkDir(f"./output/{country}")
    print("Do you want to add uppercase subtitle or lowercase subtitles?")
    print("1 - Uppercase")
    print("2 - Lowercase")
    while True:
        try:
            input_subtitle = int(input("Choice (1/2): "))
        except ValueError:
            print("Please enter a number")
            continue
        if input_subtitle <= 0 or input_subtitle > 2:
            print("Out of range")
            continue
        elif input_subtitle == 1:
            config_data = toml.load("config.toml")
            subMaker(story, country, config_data['settings']['bold'], config_data['settings']['italic'], config_data['settings']['font'], config_data['settings']['font_size'], config_data['settings']['pm_transp'], config_data['settings']['out_transp'], config_data['settings']['border_style'], config_data['settings']['margin'],config_data['settings']['length_limit'], config_data['settings']['endpoint_sec'] )
            break
        elif input_subtitle == 2:
            config_data = toml.load("config.toml")
            subMakerLower(story, country, config_data['settings']['bold'], config_data['settings']['italic'], config_data['settings']['font'], config_data['settings']['font_size'], config_data['settings']['pm_transp'], config_data['settings']['out_transp'], config_data['settings']['border_style'], config_data['settings']['margin'],config_data['settings']['length_limit'], config_data['settings']['endpoint_sec'] )
            break
        else:
            break
    shutil.rmtree("./assets") ## COMMENT THIS LINE IF ON WINDOWS
    os.system("echo clear")
    print("-------------Video created!-------------\n")
    print(f"---------./output/final_{story}---------")




