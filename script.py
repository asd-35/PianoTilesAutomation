import pyautogui
import PIL.ImageGrab


black = (8,8,8)

print("Mozart plays")

while True:
    
    
    first = [PIL.ImageGrab.grab().load()[150,1000] == black,
    PIL.ImageGrab.grab().load()[150,975] == black,
    PIL.ImageGrab.grab().load()[150,985] == black
    ]
    
    second = [PIL.ImageGrab.grab().load()[589, 975] == black,
    PIL.ImageGrab.grab().load()[589, 1000] == black,
    PIL.ImageGrab.grab().load()[589, 985] == black
    ]
    
    third = [PIL.ImageGrab.grab().load()[1028, 1000] == black,
    PIL.ImageGrab.grab().load()[1028, 975] == black,
    PIL.ImageGrab.grab().load()[1028, 985] == black
    ]
    
    fourth = [PIL.ImageGrab.grab().load()[1600, 1000] == black,
    PIL.ImageGrab.grab().load()[1600, 975] == black,
    PIL.ImageGrab.grab().load()[1600, 985] == black
    ]
    
    if first.count(True) == 3:
        pyautogui.click(150,975)
        print(first,"1nd")
    elif second.count(True) == 3:
        pyautogui.click(589, 975)
        print(second,"2nd")
    elif third.count(True) == 3:
        pyautogui.click(1028, 975)
        print(third,"3rd")
    elif fourth.count(True) == 3:
        pyautogui.click(1600, 975)
        print(fourth,"4th")
   

