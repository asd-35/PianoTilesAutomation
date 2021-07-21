import pyautogui
import PIL.ImageGrab


black = (8,8,8) #in my gaem rgb values of the black was like this

print(
  "__  __  ____ ______         _____ _______\n" +
 "|  \/  |/ __ \___  /   /\   |  __ \__   __|\n"+
 "| \  / | |  | | / /   /  \  | |__) | | |\n"+   
 "| |\/| | |  | |/ /   / /\ \ |  _  /  | |\n"+   
 "| |  | | |__| / /__ / ____ \| | \ \  | |\n"+  
 "|_|  |_|\____/_____/_/    \_\_|  \_\ |_|\n"   
    )

while True:
    
    
  
    
    if PIL.ImageGrab.grab().load()[150, 700] == black:
        pyautogui.click(150,625)
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
   

