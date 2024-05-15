import pyautogui
import time


count = int(input())

message = input()

time.sleep(5)

while(count > 0):
    pyautogui.typewrite(message)
    pyautogui.press("Enter")

    count -=1