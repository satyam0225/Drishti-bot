import speech_recognition as sr
import os

def open_word_document(filename):
    # Check if the file existsexit
    print(filename)
    if not os.path.exists(filename):
        print("File not found.")
        return

    # Open the Word document
    os.system(f"start {filename}")

def listen_and_open():
    # Initialize speech recognizer
    recognizer = sr.Recognizer()

    # Listen for speech input
    with sr.Microphone() as source:
        print("Listening for the document name...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # Convert speech to text
    try:
        document_name = recognizer.recognize_google(audio)
        print("You said:", document_name)

        # Open the document
        open_word_document(f"{document_name}"+".docx")
        
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))

if __name__ == "__main__":
    listen_and_open()