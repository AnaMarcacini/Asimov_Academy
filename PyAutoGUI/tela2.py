import pyautogui
import time
imagem = "imgs/captura_tela.png"
pyautogui.FailSafeException

## Vendo dados da tela
pyautogui.screenshot(imagem)
time.sleep(10)
try:
    # pyautogui.locateOnScreen(imagem)
    # pyautogui.locateOnScreen(imagem, confidence=0.999)
    local_imagem = pyautogui.locateCenterOnScreen(imagem)
    pyautogui.moveTo(local_imagem)
    print("Funcionou")
except Exception as e:
    print(e) 

print(f"tamanho da tela: {pyautogui.size()}")
## Criando Janelas do sistema
pyautogui.prompt(text='Texto informando o que deve ser preenchido na caixa de texto', title='Título da caixa de texto') # 
pyautogui.confirm(text="Pergunta a ser respondida", title="Título do menu", buttons=['Opção 1', 'Opção 2', 'Opção 3', 'Opção 3'])
pyautogui.alert(text='Texto do aviso', title='Aviso', button='OK')


nome_site = pyautogui.prompt(text='Informe o nome do site em que você está navegando', title='Pergunta')
resposta_aba = pyautogui.confirm(text=f"Qual aba você quer acessar no site {nome_site}", title="Menu interativo", buttons=['Esportes', 'Notícias', 'Horóscopo', 'Educação'])
pyautogui.alert(f"O código será redirecionado para a aba {resposta_aba}")