import pyautogui
import time
imagem = "imgs/captura_tela.png"
pyautogui.FailSafeException


pyautogui.screenshot(imagem)
# pyautogui.locateOnScreen(imagem)
# pyautogui.locateOnScreen("imgs/image.png")
# pyautogui.locateOnScreen(imagem, confidence=0.999)
local_imagem = pyautogui.locateCenterOnScreen(imagem)
pyautogui.moveTo(local_imagem)
print(f"tamanho da tela: {pyautogui.size()}")
pyautogui.prompt(text='Texto informando o que deve ser preenchido na caixa de texto', title='Título da caixa de texto') # 