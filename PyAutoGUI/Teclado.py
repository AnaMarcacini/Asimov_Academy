import pyautogui

pyautogui.PAUSE = 3 # define um intervalo depois dos comandos do pyautogui
pyautogui.sleep(4)
# Acento não funciona
pyautogui.typewrite("Ola, Ana", interval = 0.1) # velocidade de digitação
pyautogui.typewrite("\nTudo bom com voce")
pyautogui.write("Write Olá", interval = 0.1)

pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.press("space")
pyautogui.press("space")
pyautogui.press("space")
pyautogui.press("space")

pyautogui.keyDown("ctrl")
pyautogui.press("+")
pyautogui.press("+")
pyautogui.sleep(4)
pyautogui.press("-")
pyautogui.press("-")

pyautogui.keyUp("ctrl")


pyautogui.keyDown("shift")
pyautogui.typewrite("\nTudo, bom com voce")
pyautogui.keyUp("shift")

# pyautogui.hotkey("ctrl","shift","esc")
# pyautogui.hotkey("ctrl","f5")
# pyautogui.hotkey("ctrl","c")
# pyautogui.hotkey("ctrl","v")
# pyautogui.hotkey("alt","tab")