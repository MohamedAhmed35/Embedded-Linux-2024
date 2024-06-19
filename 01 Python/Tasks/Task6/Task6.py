import pyautogui
from time import sleep


extensions = ['clangd.png', 'c++ helper.png', 'c++ testMate.png', 'cmake tools.png', 'cmake.png']

def install(extension):
    n = 0
    pyautogui.hotkey('win', 'r')
    sleep(1)
    # pyautogui.typewrite('cmd')
    # pyautogui.press('enter')
    # sleep(1)
    pyautogui.typewrite('wsl ~')
    pyautogui.press('enter')
    sleep(10)
    # pyautogui.click()
    pyautogui.typewrite("code .", interval = 0.1)
    pyautogui.press('enter')
    sleep(10)
    
    for i in extension:
        if n > 0:
            try:
                location = None
                while location is None:
                    location = pyautogui.locateOnScreen('extension.png', confidence = 0.90)
                pyautogui.click(location.left + 15, location.top + 45)
                pyautogui.hotkey('ctrl', 'a', interval = 0.1)
                pyautogui.press('backspace')
                sleep(1)
            except pyautogui.ImageNotFoundException:
                print("Can't write extension name")
        else:
            pyautogui.hotkey('ctrl', 'shift', 'x', interval = 0.1)
            n = 1

        pyautogui.typewrite(i.split('.')[0])
        sleep(6)

        try:
            location = None
            while location is None:
                location = pyautogui.locateOnScreen(i, confidence= 0.90)
                sleep(1)
            x, y = pyautogui.center(location)
            pyautogui.click(x, y)
            sleep(1)
        except pyautogui.ImageNotFoundException:
            print("can't detect extension")

        try:
            location  = None
            while location is None:
                location = pyautogui.locateOnScreen('install.png', confidence = 0.90)
                sleep(1)
            x , y = pyautogui.center(location)
            pyautogui.click(x - 15, y)
            sleep(1)
        except pyautogui.ImageNotFoundException:
            print("can not install")
        sleep(2)

install(extensions)
