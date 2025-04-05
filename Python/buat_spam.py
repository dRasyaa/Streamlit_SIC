import pyautogui
import time

pyautogui.moveTo(1600,985)
pyautogui.click()

for i in range(10):
    pyautogui.write('Ga dijawab nih')
    time.sleep(0.1)
    pyautogui.press('Enter')