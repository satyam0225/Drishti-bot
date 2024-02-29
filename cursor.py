import pyautogui
import time

class Cursor:
    def __init__(self):
        self.x,self.y=pyautogui.position()
        self.height, self.width=pyautogui.size()

    def left(self,amount):
        self.x-=amount
        pyautogui.moveTo(self.x,self.y,1)

    def right(self,amount):
        self.x+=amount
        pyautogui.moveTo(self.x,self.y,1)

    def  up(self,amount):
        self.y-=amount
        pyautogui.moveTo(self.x,self.y,1)

    def down(self,amount):
        self.y+=amount
        pyautogui.moveTo(self.x,self.y,1)

    def scrollUp(self, scrollAmount):
        pyautogui.scroll(scrollAmount)

    def scrollDown(self, scrollAmount):
        pyautogui.scroll(-scrollAmount)
    
    def moveToCenter(self):
        pyautogui.moveTo(self.height/2,self.width/2)

if __name__=="__main__":
    obj=Cursor()
    print("Movineg Cursor up 50")
    obj.up(50)
    print("testing scroll")
    time.sleep(20)
    obj.scrollDown(2)
    time.sleep(5)
    print("moving to center")
    obj.moveToCenter()
