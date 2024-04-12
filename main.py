# -*- coding: utf-8 -*-

import datetime
import os
import subprocess
import time
import webbrowser

import psutil
import pyttsx3
import speech_recognition as sr

# chrome_path="C:\\Users\\Sakshi agarwal\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
# webbrowser.register('chrome',webbrowser.BackgroundBrowser(chrome_path),1)
from test3 import dotsetup, openwebsite


def listen_for_duration(idle,duration):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print(f"Listening for {duration} seconds...")
        audio = recognizer.listen(source, timeout=idle,phrase_time_limit=duration)

    try:
        # Recognize the speech
        text = recognizer.recognize_google(audio,language="en-IN,hi-IN")
        return text
    except sr.WaitTimeoutError:
        print("not heared anything")
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# text=listen_for_duration(2,5)
# print(text)

#web interaction
# specific url opening like google , youtube, etc
# automated task : email , search(url ), software download
#
# system navigation
# basics: my computer , documents ,recyclye bin ,


def speak(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def print_disk_partitions():
    print("Disk Partitions:")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"Device: {partition.device}")
        print("--------------")

# speak(f"You said {text}")
def greet():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if (hour > 0 and hour < 12):
        speak("Good Morning!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hello, how may i help you")

greet()
text=listen_for_duration(2,5)
print(text)
while True:

    if "open website" in text:
        openwebsite("https://"+text[13:])

    elif "get partition list" in text or "get names of my disk " in text:
        print_disk_partitions()
        speak("Here is your computers disk list")

    elif "open my computer" in text:
        subprocess.run(["explorer", "shell:MyComputerFolder"], shell=True)

    elif "open downloads folder" in text:
        subprocess.run(["explorer", "shell:Downloads"], shell=True)

    elif "open documnets folder" in text:
        subprocess.run(["explorer", "shell:DocumentsFolder"], shell=True)

    elif "open drive" in text:
        p=psutil.disk_partitions()
        l=[x.device[0] for x in p]
        if text[11].upper() not in l:
            print(l)
            speak("partition named such is not there")
        else:
            os.startfile(f"{text[11].upper()}:/")


    elif "quit the program" in text:
        speak("Have a nice day!")
        break


    time.sleep(4)
    try:
        text=listen_for_duration(2,5)
        print(text)
    except Exception as e:
        text=""
        print(e)
