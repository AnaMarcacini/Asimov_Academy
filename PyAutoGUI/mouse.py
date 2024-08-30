import pyautogui
import time
print('Aperte Ctrl-C para sair.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    pyautogui.moveTo(x=220, y=100) # movimento absoluto
    # pyautogui.moveTo(x=1900, y=400, duration=5)
    # pyautogui.moveRel(xOffset=100, yOffset=150) # movimento relativo
    # time.sleep(2)
    # pyautogui.moveTo(x=x, y=y)
    # pyautogui.mouseDown(x=100, y=130) # clicar nessa posição e fica clicando (segurando até o comando de mouseUp)
    # pyautogui.mouseUp() 