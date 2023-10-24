import pyautogui
from time import *
sleep(15)
for i in range(0, 4):
    pyautogui.write(
        'How are you bro? what are you thinking about me?', interval=0.25)
    pyautogui.press('enter')
