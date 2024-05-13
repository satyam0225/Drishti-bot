import os
import win32api as w32
import win32gui as w32g
import pyautogui

DOCUMENTS=os.path.normpath(os.path.expanduser("~/Documents")) 
DESKTOP=os.path.normpath(os.path.expanduser("~/Desktop"))
DOWNLOADS=os.path.normpath(os.path.expanduser("~/Downloads"))


def showDesktop():
    pyautogui.hotkey("winleft",'d')

def closeWindow():
    pyautogui.hotkey("alt",'f4')
    
def openMyComputer():
    os.startfile('::{20D04FE0-3AEA-1069-A2D8-08002B30309D}')

def openDownload():
    os.startfile(DOWNLOADS)

def openDocuments():
    os.startfile(DOCUMENTS)


def openInGUI(path):
    os.startfile(path)

def listDrives():
    drives=w32.GetLogicalDriveStrings().split('\000')[:-1]
    print(drives)
    return drives