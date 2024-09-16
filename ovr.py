import time

import pyautogui


def getSite(picturePath = str,addx:int = 0,addy:int= 0):
    time.sleep(3)
    location = pyautogui.locateOnScreen(picturePath,confidence=0.9,grayscale=True)
    x,y = pyautogui.center(location)
    
    pyautogui.moveTo(x+addx,y+addy,2,pyautogui.easeOutQuad)

if __name__ == "__main__":
    pyautogui.hotkey('alt','tab')
    # pyautogui.doubleClick()
    # getSite("images\conversition.png",165,80)
    getSite("images/next.png")