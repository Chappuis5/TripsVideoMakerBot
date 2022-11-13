# TikTokVideoMakerBot

## Installation

1. Clone this repo.
2. Change paths to /images in scraper.py (scraperMethod).
3. Run ``pip install -r requirements.txt``.

## Usage

WARNING: If you have ffmpeg installed with ffmpeg-python run ```pip uninstall ffmpeg```, ```pip uninstall ffmpeg```, ```pip install ffmpeg-python``` 
On WINDOWS: follow ffmpeg's github installation tutorial
1. Setup the [AWS cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), and set the maximum session duration to seven days. 
2. Change the 35th line in ```voice.py```with your user profile name.
3. Run main.py ```python3 main.py```
4. Connect to AWS before each session using ```aws sso login --profile your_profile``` , the session will last 7 days. 

After a push, if __pycache__.py files can be found on the git repo, remove them using: ```git rm -r --cached . && git add . && git commit -m "fixing .gitignore"```

## TODO

WARNING: Don't forget to update the requirements.txt file!  

- [ ] Translate text in other languages
- [ ] Add sound effects
- [ ] Add aws identifier with a toml file
- [ ] Add a check in the menu when a video subject has been treated
  
 
