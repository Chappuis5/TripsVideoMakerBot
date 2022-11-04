import os
import cv2
from pathlib import Path
from PIL import Image
import shutil
import time
import sys

def dirCleaner(path):
    for file_name in os.listdir(path):
        ext = [".webp", ".gif", ".svg", ".jpg", ".png"]
        if file_name.endswith(tuple(ext)):
            os.remove(os.path.join(path, file_name))

def dirRemover(temp_path):
    shutil.rmtree(temp_path)

def imageRenamer(croped_path):
    i = 0
    for filename in os.listdir(croped_path):
        if filename.endswith(".jpg"):  
            os.rename(os.path.join(croped_path, filename), os.path.join(croped_path, "image" + str(i) + ".jpg"))
            i += 1
        elif filename.endswith(".png"):
            os.rename(os.path.join(croped_path, filename), os.path.join(croped_path, "image" + str(i) + ".png"))
            i += 1
    print("__________SUCCESS________\n")
    print("----------------------------------------")
    print("Images renamed")
    print("----------------------------------------") 
    print("Done!")

def imageCroper(path, temp_path):
    h = 1920
    w = 1080
    images = Path(temp_path).glob("*.jpg")
    image_strings = [str(p) for p in images] # create a list of string paths
    directory = "Croped-Images"
    parent_dir = path
    croped_path = os.path.join(parent_dir, directory)
    if os.path.exists(croped_path) == True:
        print("WARNING: Croped Directory already existing, do you want to replace it? (y/n)")
        while True:
            try:
                answer = input()
            except:
                print("Please enter a valid answer.")
                continue
            else:
                break
        if answer == "y":
            shutil.rmtree(croped_path)
            os.mkdir(croped_path)
            print("in")
            for j in image_strings:
                print("in")
                img = cv2.imread(j)
                h1, w1  = img.shape[:2]
                print(img.shape)
                hp = h/h1 * 100
                wp = w/w1 * 100
                y = 0
                x = 0
                if hp == wp:
                    if h != h1 and w != w1:
                        img = cv2.resize(img, (w, h))
                        name = os.path.basename(j)
                        new_path = os.path.join(croped_path, name)
                        cv2.imwrite(new_path, img)
                        print("Resized: " + name)   
                else:
                    h = 1920
                    w = 1080
                    a = int((h1-h)/2)
                    b = int((w1-w)/2)
                    crop = img[a:a+h, b:b+w]
                    name = os.path.basename(j)
                    new_path = os.path.join(croped_path, name)
                    cv2.imwrite(new_path, crop)
                    print("Cropped: " + name)
        elif answer == "n":
            print("Exiting...")
            #exit()
    else:
        os.mkdir(croped_path)
        for j in image_strings:
            img = cv2.imread(j)
            h1, w1  = img.shape[:2]
            print(img.shape)
            hp = h/h1 * 100
            wp = w/w1 * 100
            if hp == wp:
                if h != h1 and w != w1:
                    img = cv2.resize(img, (w, h))
                    name = os.path.basename(j)
                    new_path = os.path.join(croped_path, name)
                    cv2.imwrite(new_path, img)
                    print("Resized: " + name)   
            else:
                h = 1920
                w = 1080
                a = int((h1-h)/2)
                b = int((w1-w)/2)
                crop = img[a:a+h, b:b+w]
                name = os.path.basename(j)
                new_path = os.path.join(croped_path, name)
                cv2.imwrite(new_path, crop)
                print("Cropped: " + name)
    files_croped = next(os.walk(croped_path))[2]
    images_number = len(files_croped)
    print("__________SUCCESS________\n")
    print("----------------------------------------")
    print("Number of images croped: " + str(images_number))
    print("----------------------------------------")
    print("Removing temp file...\n")
    dirRemover(temp_path)
    print("Renaming images...")
    imageRenamer(croped_path)
    time.sleep(1)
    print("-----The process has selected " + str(images_number) + " images.-----")
    
    for filename in os.listdir(croped_path):
        if filename.endswith(".jpg"):
            path = os.path.join(croped_path, filename)
            img = cv2.imread(path)
            cv2.imshow(filename, img)
            print("Do you want to keep this image? (y/n)")
            k = cv2.waitKey(0)
            if k == ord("y"):
                print("Image saved")
                os.system('say "Image saved"')
                continue
            elif k == ord("n"):
                print("Image removed")
                os.system('say "Image removed"')
                os.remove(path)
                continue
            else:
                print("Please enter a valid answer.")
                continue
        elif filename.endswith(".png"):
            path = os.path.join(croped_path, filename)
            img = cv2.imread(path)
            cv2.imshow(filename, img)
            print("Do you want to keep this image? (y/n)")
            k = cv2.waitKey(0)
            if k == ord("y"):
                print("Image saved")
                os.system('say "Image saved"')
                continue
            elif k == ord("n"):
                print("Image removed")
                os.system('say "Image removed"')
                os.remove(path)
                continue
            else:
                print("Please enter a valid answer.")
                continue
    #cv2.destroyAllWindows() 
    image_selected = next(os.walk(croped_path))[2]
    images_number = len(image_selected)
    print("You have selected " + str(images_number) + " images.")


















