from videocreation.ImScraper import scraperMethod, imageSelectorJPG, imageSelectorPNG
from videocreation.condition_image import dirCleaner, imageCroper
import time
from utils.fileCheckers import mkDir
print("-------------Welcome to the TripTricks bot for TikTok-------------\n")
print("This bot will help you create a video based on a trip destination\n")
print("Destination name: ")
destination = input()

print("input:" + destination + "\n")
print("Image attribute: (example: landscape) ")
attribute = input()
print("input: " + attribute + "\n")
space = " "
print("-----Scraping Images from Pinterest-----\n")

keywords = destination + space + attribute
mkDir("./assets")
mkDir("./assets/images")
path = scraperMethod(destination ,  keywords)

print("-------------Image selection-------------\n")

print("Do you want to select JPG, PNG images or both? (1/2/3)")

while True:
    try:
        choice = input()
    except ValueError:
        print("Please enter either 1, 2 or 3")
        continue
    else:
        break
if choice == "1":
    temp_path = imageSelectorJPG(path)
    print("Do you want to select PNGs? (y/n)")
    while True:
        try:
            answer = input()
        except:
            print("Please enter a valid answer.")
            continue
        else:
            break
    if answer == "y":
        temp_path = imageSelectorPNG(path)
        dirCleaner(path)
    elif answer == "n":
        print("Exiting...")
        dirCleaner(path)
        #exit()
    else:
        print("Please enter a valid answer.")
        #exit()
elif choice == "2":
    temp_path = imageSelectorPNG(path)
    print("Do you want to select JPGs? (y/n)")
    while True:
        try:
            answer = input()
        except:
            print("Please enter a valid answer.")
            continue
        else:
            break
    if answer == "y":
        temp_path = imageSelectorJPG(path)
        dirCleaner(path)
    elif answer == "n":
        print("Exiting...")
        dirCleaner(path)
        #exit()
    else:
        print("Please enter a valid answer.")
        #exit()
elif choice == "3":
    temp_path = imageSelectorJPG(path)
    temp_path = imageSelectorPNG(path)
    dirCleaner(path)

print("-------------------------------")
print("-----Croping images now...-----")
print("-------------------------------")
time.sleep(2)
imageCroper(path, temp_path)


