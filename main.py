# -*- coding: utf-8 -*-

import time
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
from navigation import *
from cursor import Cursor
from common import *
from web_test import  *

# from vlctest import VLCPlayer
# chrome_path="C:\\Users\\Sakshi agarwal\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
# webbrowser.register('chrome',webbrowser.BackgroundBrowser(chrome_path),1)

PATH=os.getcwd()
player=None

def openPLayer(filename):
    global player
    player=VLCPlayer(filename)
    player.play()
    time.sleep(5)



def listen_for_duration(idle,duration):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print(f"Listening for {duration} seconds...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=idle,phrase_time_limit=duration)
        # audio = recognizer.listen(source)

    try:
        # Recognize the speech
        text = recognizer.recognize_google(audio,language="en-IN,hi-IN")
        return str(text).lower()

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
    print(f"COMMAND SPOKEN : {command}")
    engine.say(command)
    engine.runAndWait()


#speak(f"You said {text}")
    
cursorObj=Cursor()


greet=False
while True:
    if not greet:
        speak("good morning")
        greet=True
    print(f"You are currently : \n Path ->{PATH}  \n CWD ->{cwd()}" )
    cmd =listen_for_duration(3,8)
    print(cmd)
    if cmd != None and"list directory" in cmd:
        listdir()
    if cmd !=None and  "where i am" in cmd:
        speak("you are at")
        pwd()

    if cmd != None  and "make directory" in cmd:
        speak("Give the file name ")
        filename= listen_for_duration(2,5)
        p=os.getcwd()+f"/{filename}"
        if os.path.exists(p):
            speak("File exists")
        else:

            mkdir(filename)
            p=os.getcwd()+f"/{filename}"
            if os.path.exists(p):
                print("File exists")
            print(f"{filename} created:")
    
    if cmd != None and "delete directory" in cmd:
        speak("tell the directory name to be deleted")
        filename= listen_for_duration(1,5)
        p=cwd()+f"/{filename}"
        if os.path.exists(p):
            speak("Is file empty or not")
            res=listen_for_duration(1,5)
            if res != None and "yes" in res:
                speak(f"removing file named {filename} ")
                rmdir(filename)
            else:
                speak(f"removing file named {filename} ")
                rmnotempty(filename)
        else:
            speak(f"{filename} does not exists")

    if cmd != None and "remove file" in cmd:
        speak("tell the file name to be deleted")
        filename= listen_for_duration(1,5)
        p=cwd()+f"/{filename}"
        if os.path.exists(p):
            speak(f"deleteing file named {filename}")
            rm(p)
        else:
            speak(f"file named {filename} does not exist")
    
    if cmd != None and "go up a directory" in cmd:
        goupdir()
        PATH=cwd()

    if cmd != None and "change directory" in cmd:
        speak("These are the list of directories select where you want to go")
        listdir()
        dirname=listen_for_duration(2,5)
        path=cwd()+f"/{dirname}"
        if os.path.isdir(path):
            chdir(path)
            PATH=cwd()
            speak("directory changed")
        else:
            speak("sorry it is not a diretory cannot chagne")

        
    if cmd != None and "go to desktop" in cmd:
        chdir(DESKTOP)
        PATH=cwd()

    if  cmd != None and "go to downloads" in cmd:
        chdir(DOWNLOADS)
        path=cwd()
    
    if  cmd != None and "go to documents" in cmd:
        chdir(DOCUMENTS)
        path=cwd()

    if cmd != None and "show desktop" in cmd :
        showDesktop()
        speak("Showing desktop going back in 10 seconds")
        time.sleep(10)
        showDesktop()

    if cmd != None and "close window" in cmd:
        speak("closing window")
        closeWindow()

    if cmd != None and ("open this pc" in cmd or "open my computer" in cmd):
        openMyComputer()

    if cmd != None and "open downloads" in cmd:
        openDownload()

    if cmd != None and "open document" in cmd:
        openDocuments()

    if cmd != None and "open in window" in cmd:
        if PATH == cwd():
            openInGUI(PATH)
        else:
            speak("your current working directory is not same as your path")

    if cmd != None and "list drives" in cmd:
        listDrives()

    if cmd != None and "search youtube" in cmd:
        speak("tell the keyword to search on youtube")
        time.sleep(1)
        keyword=listen_for_duration(2,6)
        speak(keyword)
        limit=10 #deafult
        speak("do you want to edit the default limit of the search")
        time.sleep(1)
        res1=listen_for_duration(2,6)
        if res1=='yes':
            speak("tell te limit")
            res2=listen_for_duration(2,6)
            if str(res2).isdigit():
                limit=res2
            else:
                speak("limit said is not a number going with default")
        else:
            data=(searchYoutube(keyword,limit))
            speak("tell which number link to open")
            for i in range(data):
                print(60+i, data[i][0],data[i][1])

            speak("tell the number which you want to open")
            no=listen_for_duration(1,5)
            webbrowser.open(data[no%60][1])

    if cmd !=None and "search google" in cmd:
        speak("tell the keyword to search")

        keyword= listen_for_duration(1,5)
        data=searchGoogle(keyword)
        print("Result: \n")
        c=0
        for i in data:
            print(c+60," ",i)
            c+=1
        speak("which link to open the with adding 60 to it")
        time.sleep(5)
        option=int(listen_for_duration(1,5))
        speak("opening link")
        webbrowser.open(data[option%60])

    
    if cmd!=None and "open video file" in cmd:
        speak("tell which file to open")
        
        for i in os.listdir():
            if ".mp4" in i:
                print(i)
        time.sleep(5)
        filename=listen_for_duration(2,5)
        print(filename)
        openPLayer(f"{cwd()}/{filename}.mp4")
        
    
    if cmd!=None and "close player" in cmd:
        player.stop()
     
        

    

    if cmd !=None and "exit" in cmd:
        break

    