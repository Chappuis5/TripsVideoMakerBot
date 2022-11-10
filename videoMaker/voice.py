"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os, time
import sys
import subprocess
from tempfile import gettempdir
import uuid
import gtts
from playsound import playsound

#from utils.fileCheckers import mkDir

def mkDir(path):
    if os.path.isdir(path):
        #print("...directory exist...")
        return True
    else:
        os.mkdir(path)
        #print("Directory created")
        return False

def mkFile(path):
    if os.path.isfile(path):
        #print("...file exist...")
        return True
    else:
        return False

def TTS(string, name):
    mkDir("./assets")
    # Create a client using the credentials and region defined in the [adminuser]
    # section of the AWS credentials file (~/.aws/credentials).
    """ mat = ""
    while True:
        print("Choose the final video language: (en/fr)")
        language = input()
        if(language == "en"):
            mat = "Matthew"
            break
        elif (language == "fr"):
            mat = "Mathieu"
            break
        else:
            print("Please enter a valid language.\n")
            continue  """
    mat = "Matthew"         
    session = Session(profile_name="batmstrong")
    polly = session.client("polly")

    try:
        # Request speech synthesis
        response = polly.synthesize_speech(Text=string, OutputFormat="mp3",
                                            VoiceId=mat)
    except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)

    # Access the audio stream from the response
    if "AudioStream" in response:
        # Note: Closing the stream is important because the service throttles on the
        # number of parallel connections. Here we are using contextlib.closing to
        # ensure the close method of the stream object will be called automatically
        # at the end of the with statement's scope.
            with closing(response["AudioStream"]) as stream:
                directory = "audio"
                parent_dir = "./assets"
                path = os.path.join(parent_dir, directory)
                mkDir(path)
                filename = name
                f = filename + ".mp3"
                output = os.path.join(path, f)
                if mkFile(output):
                    print("File already exists.")
                    exit()
                try:
                    # Open a file for writing the output as a binary stream
                    with open(output, "wb") as file:
                        file.write(stream.read())
                        t = os.path.getctime(output)
                        m_ti = time.ctime(t)
                        #print(m_ti)
                except IOError as error:
                    # Could not write to file, exit gracefully
                    print(error)
                    sys.exit(-1)
    else:
        # The response didn't contain audio data, exit gracefully
        print("Could not stream audio")
        sys.exit(-1)

    """ ,  """

""" string = "john suce des gros sexes"

TTS(string) """

def gTTS(str):
    tts = gtts.gTTS(str)
    tts.save("hello.mp3")
    playsound("hello.mp3")

"""gTTS(string)"""