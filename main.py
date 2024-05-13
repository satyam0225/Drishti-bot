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
from ailocal import localGreetingAi,localAi
import vlc

# chrome_path="C:\\Users\\Sakshi agarwal\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
# webbrowser.register('chrome',webbrowser.BackgroundBrowser(chrome_path),1)

PATH=os.getcwd()

player=None


def openPLayer(filename):
    global player
    player=vlc.MediaPlayer(filename)
    player.play()
    
    time.sleep(5)

def open_word_document(filename):
    # Check if the file existsexit
    print(filename)
    if not os.path.exists(filename):
        print("File not found.")
        speak("File not found")
        return

    # Open the Word document
    os.system(f"start {filename}")

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
        text = recognizer.recognize_google(audio,language="en-IN")
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
        speak(localGreetingAi())
        greet=True
    print(f"You are currently : \n Path ->{PATH}  \n CWD ->{cwd()}" )
    cmd =listen_for_duration(5,8)
    print(cmd)
    if cmd !=None and "jarvis" in cmd:
        resposne_jarvis=(localAi(cmd[7:]))
        print("AI Resposne:",resposne_jarvis)
        speak(resposne_jarvis)

    if cmd != None and "list directory" in cmd:
        listdir()
    if cmd !=None and  "where i am" in cmd:
        speak("you are at")
        pwd()

    if cmd != None  and "make directory" in cmd:
        speak("Give the file name ")
        filename= listen_for_duration(7,5)
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
        filename= listen_for_duration(7,5)
        p=cwd()+f"/{filename}"
        if os.path.exists(p):
            speak("Is file empty or not , Say yes or no")
            res=listen_for_duration(7,5)
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
        dirname=listen_for_duration(5,8)
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
        keyword=listen_for_duration(8,5)
        if keyword is None:
            speak("couldn't understand the word")
            continue
        speak(keyword)
        limit=10 #deafult
        # speak("do you want to edit the default limit of the search")
        time.sleep(1)
        # res1=listen_for_duration(2,6)
        res1="no"
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
            for i in range(len(data)):
                print(60+i, data[i][0],data[i][1])

            speak("tell the number which you want to open")
            no=int(listen_for_duration(2,6))
            print(no)
            if no:
                webbrowser.open(data[no%60][0])
            else:
                speak("coldn't under stand the option you said")
    if cmd !=None and "search google" in cmd:
        speak("tell the keyword to search")

        keyword= listen_for_duration(10,8)
        print(keyword)
        data=searchGoogle(keyword)
        print("Result: \n")
        c=0
        for i in data:
            print(c+60," ",i)
            c+=1
        speak("which link to open the with adding 60 to it")
        time.sleep(5)
        option=int(listen_for_duration(10,8))
        print(option)
        speak("opening link")
        webbrowser.open(data[option%60])

    
    if cmd!=None and "open video file" in cmd:
        speak("tell which file to open")
        
        for i in os.listdir():
            if ".mp4" in i:
                print(i)
        time.sleep(5)
        filename=listen_for_duration(5,8)
        print(filename)
        openPLayer(f"{cwd()}/{filename}.mp4")

    if player!=None and cmd!=None and "play video" in cmd:
        player.play()    
    if cmd!=None and "pause video" in cmd:
        player.pause()
    if cmd!=None and "close video" in cmd:
        player.stop()
     
    if cmd!=None and "type" in cmd:
        speak("say speaking completed when done dictating")
        words=listen_for_duration(5,8)
        while("speaking completed" not in words):
            speak("writing")
            pyautogui.write(words)
            pyautogui.press("Enter")
            words=""
            time.sleep(2)
            speak("speak the next line")
            words=listen_for_duration(5,8)
        speak("saving file")
        pyautogui.press("rctrl","S") 
        
    if cmd!=None and "open word file" in cmd:
        speak("tell which file to open")
        
        for i in os.listdir():
            if ".docx" in i:
                print(i)
        time.sleep(5)
        filename=listen_for_duration(5,8)
        if filename!=None:
            open_word_document(filename+".docx")
        else:
            speak("unable to understand the filename")    

    if cmd !=None and "exit" in cmd:
        break

    