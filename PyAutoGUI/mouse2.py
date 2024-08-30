import pyautogui
import time
pyautogui.moveTo(x=220, y=100) # movimento absoluto
pyautogui.moveTo(x=1900, y=400, duration=5)
pyautogui.moveRel(xOffset=100, yOffset=150) # movimento relativo
    # time.sleep(2)
pyautogui.mouseDown(x=100, y=130) # clicar nessa posição e fica clicando (segurando até o comando de mouseUp)
pyautogui.moveTo(x=1900, y=400, duration=5)
pyautogui.mouseUp() 

# movimento com clique pressionado t
pyautogui.dragTo(x=100, y=100, duration=5) # pyautogui.dragTo()e a outra de forma relativa pyauto-gui.dragRel().


# Exemplo de clique simples:
pyautogui.click(x=470, y=855, clicks=1, interval=0)
# Exemplo de clique duplo:
pyautogui.click(x=470, y=855, clicks=2, interval=0)
# Exemplo de clique múltiplo:
pyautogui.click(x=470, y=855, clicks=5, interval=0)
# pyau-togui.doubleClick() ou pyautogui.tripleClick()
# pyautogui.rightClick().
# pyautogui.middleClick() # pyautogui.middleClick(x=140, y=20, interval=0)
# x e y -> coordenadas do ponto na tela em que será executado o clique com botão esquerdo
# clicks -> número de cliques que serão executados
# interval -> intervalo de tempo (em segundos) entre cada execução de um clique

pyautogui.scroll(clicks=-5, x=500, y=150) # scroll de 5 unidades para baixo.
pyautogui.scroll(10, 500, 150)
#  pyautogui.scroll()
