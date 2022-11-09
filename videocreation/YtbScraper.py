from pytube import Search
from pytube import YouTube
from typing import Tuple
import os, shutil
#from utils.fileCheckers import mkDir

# in construction
""" s = Search('Learn Python')
for v in s.results:
  print(f"{v.title}\n{v.watch_url}\n")


# get object keys
keys = "\n".join([k for k in s.results[0].__dict__])
print(keys)  """

def mkDir(path):
    if os.path.isdir(path):
        print("...directory exist...")
        return True
    else:
        os.mkdir(path)
        print("Directory created")
        return False
""" 
s = Search('Learn Python')
for v in s.results:
  print(f"{v.title}\n{v.watch_url}\n")

# get object keys
keys = "\n".join([k for k in s.results[0].__dict__])
print(keys)
print(s.results[1].vid_info.get('videoDetails', {}).get('lengthSeconds'))
i = 0
while (int(s.results[i].vid_info.get('videoDetails', {}).get('lengthSeconds'))) > 500:
    i += 1
    print(i)
    print(s.results[i].vid_info.get('videoDetails', {}).get('lengthSeconds')) """
    

    

#background_config: Tuple[str, str, str, Any]
destination = "Los-Angeles"
#Path("./assets/backgrounds/").mkdir(parents=True, exist_ok=True)
directory = "backgrounds"
parent_dir = "./assets"
path = os.path.join(parent_dir, directory)
mkDir(path)
directory2 = destination
parent_dir2 = path
path2 = os.path.join(parent_dir2, directory2)
if mkDir(path2):
    print("Directory already exists.")
    print("Do you want to replace it? (y/n)")
    while True:
        try:
            answer = input()
        except:
            print("Please enter a valid answer.")
            continue
        else:
            break
    if answer == "y":
        print("Removing directory...")
        shutil.rmtree(path2)
        print("Directory removed.")
        print("Creating new directory...")
        os.mkdir(path2)
        print("Directory created.")
        print("Enter a keyword")
        keyword = input()
        s = Search(keyword)
        i = 0
        while (int(s.results[i].vid_info.get('videoDetails', {}).get('lengthSeconds'))) > 500:
            i += 1
            print(i)
            print(s.results[i].vid_info.get('videoDetails', {}).get('lengthSeconds'))
        print("Video found !")
        print(s.results[i].video_id)
        url = s.results[i].watch_url
        print(s.results[i].watch_url)
        print("Downloading video...")
        yt = YouTube(url).streams.filter(res="1080p").first().download(path2, filename=f"{s.results[i]._title}.mp4")
        print("Video downloaded.")
    elif answer == "n":
        print("Exiting...")
        exit()
    else:
        print("Please enter a valid answer.")
        exit()
else:
    print("Enter a keyword")
    keyword = input()
    s = Search(keyword)
    i = 0
    while (int(s.results[i].vid_info.get('videoDetails', {}).get('lengthSeconds'))) > 500:
        i += 1
        print(i)
        print(s.results[i].vid_info.get('videoDetails', {}).get('lengthSeconds'))
    print("Video found !")
    print(s.results[i].video_id)
    url = s.results[i].watch_url
    print(s.results[i].watch_url)
    print("Downloading video...")
    yt = YouTube(url).streams.filter(res="1080p").first().download(path2, filename=f"{s.results[i]._title}.mp4")
    print("Video downloaded.") 


""" # note: make sure the file name doesn't include an - in it
# uri, filename, credit, _ = background_config
print("---Srape a video---")


if Path(f"assets/backgrounds/{credit}-{filename}").is_file():
    return
print_step(
    "We need to download the backgrounds videos. they are fairly large but it's only done once. 😎"
)
print_substep("Downloading the backgrounds videos... please be patient 🙏 ")
print_substep(f"Downloading {filename} from {uri}")
YouTube(uri, on_progress_callback=on_progress).streams.filter(res="1080p").first().download(
    "assets/backgrounds", filename=f"{credit}-{filename}"
)
print_substep("Background video downloaded successfully! 🎉", style="bold green") """
