import pyautogui
import time

pyautogui.moveTo(1719,1000)
pyautogui.click()

for i in range(10):
    pyautogui.write('P')
    time.sleep(0.1)
    pyautogui.press('Enter')