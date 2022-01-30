import sys
import time
import pyautogui

print(sys.executable)

time.sleep(5)
pyautogui.hotkey('ctrl','t')
time.sleep(1)
link = 'https://www.facebook.com'
pyautogui.typewrite(link + '\n')
time.sleep(5)
pyautogui.press('p')
time.sleep(3)
pyautogui.typewrite('Hello from python')
time.sleep(3)
pyautogui.hotkey('ctrl','enter')
