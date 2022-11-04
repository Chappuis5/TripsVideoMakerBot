# TripsVideoMakerBot

## Usage

Clone git repo and change paths to /images in the scraperMethod (scraper.py).

## Don't push to origin, create another branch

The code is sans dessus sans dessous, pusher to origin would cause major
issues. Instead, create your own develop branch.

## TODO

- [ ] Get Youtube Videos based on keywords and length.
- [ ] Edit the videos and images into one single video based on user criteria.
  (try to reuse previously created methods for images)
- [ ] Add a music editing option, where the video editing is made on a selected
  music downloaded from youtube. (e.g. cuts would be made on top frequencies of
the song.)
- [ ] Manage all exceptions.
- [ ] Add a "Current files under /images weight [weight], do you want to erase
  them? (y/n)" when files are over a certain weight.
- [ ] Refactor the code for simpler usage on Windows/Linux/MacOs by creating a
  requirements.txt file and managing path emerging issues.
- [ ] Simplify the code.
- [x] Add a .gitignore for /images and mkdir images when compiled.
- [x] Add a renaming method.
- [x] Add a croping and resizing method.
- [x] Scrape images from pinterest based on keywords.
  
 
