import pyautogui 
import time 

def spam_click():
    pyautogui.click(258, 278)

for i in range(100):
    spam_click()
    spam_click()
    spam_click()