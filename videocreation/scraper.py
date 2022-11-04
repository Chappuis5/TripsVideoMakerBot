import os
import random
from pinscrape import pinscrape
from PIL import Image
import cv2
import glob, random
from pathlib import Path
import shutil
from utils.fileCheckers import mkDir

def scraperMethod(destination, keywords):

    directory = destination
    parent_dir = "/Users/evanflament/Documents/Git-Projects/TripsVideoMakerBot/images"
    path = os.path.join(parent_dir, directory)
    mkDir(parent_dir)
    if os.path.exists(path) == True:
        print("WARNING: Directory already exists.")
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
            shutil.rmtree(path)
            print("Directory removed.")
            print("Creating new directory...")
            os.mkdir(path)
            print("Directory created.")
            print("Scraping images...")
            details = pinscrape.scraper.scrape(keywords, path, {}, 10)

            if details["isDownloaded"]:
                print("\nDownloading completed !!")
                print(f"\nTotal urls found: {len(details['extracted_urls'])}")
                print(f"\nTotal images downloaded (including duplicate images): {len(details['url_list'])}")
                #print(details)
            else:
                print("\nNothing to download !!")
        elif answer == "n":
            print("Exiting...")
            exit()
        else:
            print("Please enter a valid answer.")
            exit()
    else:
        print("Creating directory...")
        os.mkdir(path)
        print("Directory created.")
        print("Scraping images...")
        details = pinscrape.scraper.scrape(keywords, path, {}, 10)

        if details["isDownloaded"]:
            print("\nDownloading completed !!")
            print(f"\nTotal urls found: {len(details['extracted_urls'])}")
            print(f"\nTotal images downloaded (including duplicate images): {len(details['url_list'])}")
            #print(details)
        else:
            print("\nNothing to download !!")
    
    return path

def imageSelectorJPG(path):
    images = Path(path).glob("*.jpg")
    image_strings = [str(p) for p in images] # create a list of string paths 
    directory = "_temp_"
    parent_dir = path
    temp_path = os.path.join(parent_dir, directory)

    if os.path.exists(temp_path) == True:
        for j in image_strings:
            img = cv2.imread(j)
            h, w, c  = img.shape[:3]
            if h >= 1920 and w >= 1080 and c ==3:
                name = os.path.basename(j)
                t_temp_path = os.path.join(temp_path, name)
                img = cv2.imread(j)
                shape = str(img.shape)
                cv2.imwrite(t_temp_path, img)
                print("kept: " + name + " dimensions: " + shape)
            else:
                os.remove(j)
        selected_images = Path(path).glob("*.jpg")
        selected_image_strings = [str(p) for p in selected_images] # create a list of string paths
        for y in selected_image_strings:
            os.remove(y)
    else:
        os.mkdir(temp_path)
        for j in image_strings:
            img = cv2.imread(j)
            h, w, c  = img.shape[:3]
            if h >= 1920 and w >= 1080 and c ==3:
                name = os.path.basename(j)
                t_temp_path = os.path.join(temp_path, name)
                img = cv2.imread(j)
                shape = str(img.shape)
                cv2.imwrite(t_temp_path, img)
                print("kept: " + name + " dimensions: " + shape)
            else:
                os.remove(j)
        selected_images = Path(path).glob("*.jpg")
        selected_image_strings = [str(p) for p in selected_images] # create a list of string paths
        for y in selected_image_strings:
            os.remove(y)
    files_created = next(os.walk(temp_path))[2]
    images_number = len(files_created)
    print("__________SUCESS________\n")
    print("----------------------------------------")
    print("Number of images selected: " + str(images_number))
    print("----------------------------------------")
    return temp_path

    
def imageSelectorPNG(path):
    images = Path(path).glob("*.png")
    image_strings = [str(p) for p in images] # create a list of string paths 
    directory = "_temp_"
    parent_dir = path
    temp_path = os.path.join(parent_dir, directory)

    if os.path.exists(temp_path) == True:
        for j in image_strings:
            img = cv2.imread(j)
            h, w, c  = img.shape[:3]
            if h >= 1920 and w >= 1080 and c ==3:
                name = os.path.basename(j)
                t_temp_path = os.path.join(temp_path, name)
                img = cv2.imread(j)
                shape = str(img.shape)
                cv2.imwrite(t_temp_path, img)
                print("kept: " + name + " dimensions: " + shape)
            else:
                os.remove(j)
        selected_images = Path(path).glob("*.png")
        selected_image_strings = [str(p) for p in selected_images] # create a list of string paths
        for y in selected_image_strings:
            os.remove(y)
    else:
        os.mkdir(temp_path)
        for j in image_strings:
            img = cv2.imread(j)
            h, w, c  = img.shape[:3]
            if h >= 1920 and w >= 1080 and c ==3:
                name = os.path.basename(j)
                t_temp_path = os.path.join(temp_path, name)
                img = cv2.imread(j)
                shape = str(img.shape)
                cv2.imwrite(t_temp_path, img)
                print("kept: " + name + " dimensions: " + shape)
            else:
                os.remove(j)
        selected_images = Path(path).glob("*.png")
        selected_image_strings = [str(p) for p in selected_images] # create a list of string paths
        for y in selected_image_strings:
            os.remove(y)
    files_created = next(os.walk(temp_path))[2]
    images_number = len(files_created)
    print("__________SUCESS________\n")
    print("----------------------------------------")
    print("Number of PNG images selected: " + str(images_number))
    print("----------------------------------------")
    return temp_path
