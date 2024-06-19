import pyautogui
import webbrowser
from time import sleep

email = 'https://mail.google.com/mail/u/0/#inbox'
webbrowser.open(email)
sleep(7)


def markUnreadEmails():
    location = None
    try:
        while location is None:
            location = pyautogui.locateOnScreen('markAllUnread.png')
        pyautogui.click(location.left + 30, location.top + 15)
        sleep(1)
        location = None
        while location is None:
            location = pyautogui.locateOnScreen('unread_word.png')
        pyautogui.click(pyautogui.center(location))
        sleep(1)
    except pyautogui.ImageNotFoundException:
        print("Image not found")


def openUnreadEmails(): 
    try:
        locations = list(pyautogui.locateAllOnScreen('marked.png', confidence = 0.87))
        noOfUnreadEmails = len(locations)

        for i in range(0, noOfUnreadEmails):
            x, y = locations[i].left, locations[i].top
            pyautogui.click(x + 250, y + 10)
            sleep(1)
            location = pyautogui.locateOnScreen('back.png')
            pyautogui.click(location.left+5, location.top + 5)
            sleep(3)
            # x , y = pyautogui.locateCenterOnScreen('unread.png')
            # pyautogui.moveTo(x, y)
            # sleep(2)
    except pyautogui.ImageNotFoundException:
        print("can't locate unread")

markUnreadEmails()
openUnreadEmails()
