import pyautogui
import time

#abrir DOSBox e executar High Seas Trader
pyautogui.alert("Vai começar! Aperte OK e não mexa em mais nada!")
pyautogui.press("winleft")
time.sleep(1)
pyautogui.write("dosbox")
time.sleep(1)
pyautogui.press("enter")
time.sleep(3)
pyautogui.write('mount x c:\DOSBox\OldStuff\HST', interval=0.1)
pyautogui.press("enter")
pyautogui.write("x:")
pyautogui.press("enter")
pyautogui.write("hst")
pyautogui.press("enter")
time.sleep(10)

#configurar DOSBox
'''pyautogui.keydown('ctrl')
pyautogui.press('F11', presses= 16)
pyautogui.keyup('ctrl')
pyautogui.hotkey("ctrl", "F11", presses=17)'''
pyautogui.hotkey("ctrl", "F11")
pyautogui.hotkey("ctrl", "F11")
pyautogui.hotkey("ctrl", "F11")
pyautogui.hotkey("ctrl", "F11")
pyautogui.hotkey("ctrl", "F11")
pyautogui.hotkey("ctrl", "F11")
pyautogui.hotkey("ctrl", "F11")
pyautogui.hotkey("ctrl", "F11")
pyautogui.hotkey("ctrl", "F11")
pyautogui.hotkey("ctrl", "F11")
pyautogui.hotkey("ctrl", "F11")
pyautogui.hotkey("ctrl", "F11")
pyautogui.hotkey("ctrl", "F11")
pyautogui.hotkey("ctrl", "F11")
#pyautogui.hotkey("ctrl", "F11")
time.sleep(10)
pyautogui.hotkey("alt", "enter")
time.sleep(5)

#Fechar Script
Break
ExitNow
