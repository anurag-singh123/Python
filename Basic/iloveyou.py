import pyautogui
import time
time.sleep(0)
count = 0
while count<=50:
    pyautogui.typewrite("Good Night"+str(count))
    pyautogui.press("enter")
    count = count +1