import pyautogui


class Cursor:
    def __init__(self):
        self.x,self.y=pyautogui.position()
        

    def left(self,amount):
        self.x-=amount
        pyautogui.dragTo(self.x,self.y)

    def right(self,amount):
        self.x+=amount
        pyautogui.dragTo(self.x,self.y)

    def  up(self,amount):
        self.y-=amount

    def down(self,amount):
        self.y+=amount


Cursor()