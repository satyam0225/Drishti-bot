import pyautogui
import cv2
import numpy as np
import keyboard
from win32api import GetSystemMetrics
import time


"""
This file is created to create video demonstratons of the project, It hase no 
relevance with the project.

"""


# Specify resolution
resolution = (GetSystemMetrics(0), GetSystemMetrics(1))

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# Specify name of Output file
filename = "Recording7.mp4"

# Specify frames rate. We can choose any 
# value and experiment with it
fps = 20.0  # Set FPS to 20

# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Calculate delay between frames to achieve desired FPS


while True:
    # Capture screen
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write frame to the output file
    out.write(frame)

    # Break the loop if 'p' is pressed
    if keyboard.is_pressed('Ctrl + m'):
        print('m pressed')
        break

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()
