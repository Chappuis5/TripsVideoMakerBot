import os

def checkFile(path):
    if os.path.isfile(path):
        return True
    else:
        return False

def checkDir(path):
    if os.path.isdir(path):
        return True
    else:
        return False

def checkFileExt(path, ext):
    if os.path.isfile(path):
        if os.path.splitext(path)[1] == ext:
            return True
        else:
            return False
    else:
        return False

def mkDir(path):
    if os.path.isdir(path):
        print("...directory exist...")
    else:
        os.mkdir(path)
        print("Directory created")
