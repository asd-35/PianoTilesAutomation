import pyautogui
import PIL.ImageGrab
import sys
from pynput.keyboard import Key, Listener


black = (8,8,8) #in my gaem rgb values of the black was like this

print(
  "__  __  ____ ______         _____ _______\n" +
 "|  \/  |/ __ \___  /   /\   |  __ \__   __|\n"+
 "| \  / | |  | | / /   /  \  | |__) | | |\n"+   
 "| |\/| | |  | |/ /   / /\ \ |  _  /  | |\n"+   
 "| |  | | |__| / /__ / ____ \| | \ \  | |\n"+  
 "|_|  |_|\____/_____/_/    \_\_|  \_\ |_|\n"   
    )
print("press SHIFT to start ESC to quit")
print("------------------------------------------")
print("Adjust the coordinates of your screen to the bot --> check source code you will find what you need")

def on_press(key):
    
        while (key == Key.shift):    

            if PIL.ImageGrab.grab().load()[150, 700] == black:
                pyautogui.click(150,725)
                print("1nd")
            elif PIL.ImageGrab.grab().load()[589, 700] == black:
                pyautogui.click(589, 725)
                print("2nd")
            elif PIL.ImageGrab.grab().load()[1028, 700] == black:
                pyautogui.click(1028, 725)
                print("3rd")
            elif PIL.ImageGrab.grab().load()[1600, 700] == black:
                pyautogui.click(1600, 725)
                print("4th")
    

def on_release(key):
    if(key == Key.esc):
        sys.exit(0)

with Listener(on_press=on_press,on_release=on_release) as listen:
    listen.join()


    
   


#this will give you the rgb values

#color = PIL.ImageGrab.grab().load()[150, 700] 

#this block of code makes it click

#pyautogui.click(x, y)