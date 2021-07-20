import pyautogui
import PIL.ImageGrab


while True:
    first = PIL.ImageGrab.grab().load()[150,762]
    second = PIL.ImageGrab.grab().load()[589, 755]
    third = PIL.ImageGrab.grab().load()[1028, 759]
    fourth = PIL.ImageGrab.grab().load()[1374, 765]
    
    if first == (255,255,255):
        pyautogui.click(150,762)
        print(first)
    elif second == (255,255,255):
        pyautogui.click(589, 755)
        print(second)
    elif third == (255,255,255):
        pyautogui.click(1028, 759)
        print(third)
    elif fourth == (255,255,255):
        pyautogui.click(1374, 765)
        print(fourth)
   

