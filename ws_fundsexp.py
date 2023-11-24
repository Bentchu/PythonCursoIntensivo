import webbrowser
import pyautogui
import pyperclip
import time

webbrowser.open('https://www.fundsexplorer.com.br/ranking')
time.sleep(15)
pyautogui.click(1336, 318)
pyautogui.moveTo(239, 849)
pyautogui.dragTo(576, 931, button='left')
