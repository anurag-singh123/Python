import pyautogui
import time
time.sleep(0)
count = 0
while count<=1000:
    pyautogui.typewrite("I Love You"+str(count))
    pyautogui.press("enter")
    count = count +1