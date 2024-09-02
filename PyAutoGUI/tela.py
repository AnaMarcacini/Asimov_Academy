import pyautogui
import time
imagem = "imgs/captura_tela.png"
pyautogui.FailSafeException


pyautogui.screenshot(imagem)
# pyautogui.locateOnScreen(imagem)
# pyautogui.locateOnScreen("imgs/image.png")
# imagem = "imgs/Aperte.png"

# local_imagem = pyautogui.locateOnScreen(imagem)
# pyautogui.locateOnScreen(imagem, confidence=0.999)

# print(local_imagem)
local_imagem = pyautogui.locateCenterOnScreen(imagem)
pyautogui.moveTo(local_imagem)
time.sleep(2)
print(f"tamanho da tela: {pyautogui.size()}")
pyautogui.prompt(text='Texto informando o que deve ser preenchido na caixa de texto', title='Título da caixa de texto') # 