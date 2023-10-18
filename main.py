# -*- coding: utf-8 -*-

import speech_recognition as sr
import pyttsx3
import webbrowser


chrome_path="C:\\Users\\Sakshi agarwal\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome',webbrowser.BackgroundBrowser(chrome_path),1)

def listen_for_duration(idle,duration):
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print(f"Listening for {duration} seconds...")
        audio = recognizer.listen(source, timeout=idle,phrase_time_limit=duration)

    try:
        # Recognize the speech
        text = recognizer.recognize_google(audio,language="hi-IN,en-IN")
        return text
    except sr.WaitTimeoutError:
        print("not heared anything")
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

text=listen_for_duration(2,5)
print(text)