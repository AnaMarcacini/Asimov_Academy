import cv2
import numpy as np

# Vamos utilizar algumas cores aqui pra representação, então vou atribui-las a variáveis
# usamos BGR!!!!
azul = 255, 0, 0        # Blue
verde = 0, 255, 0        # Green
vermelho = 0, 0, 255        # Red

# Lendo as imagens
# blank_img = np.zeros((500, 500), dtype='uint8')
blank_img = np.zeros((500, 500, 3), dtype='uint8')  # imagem 500x500 com 3 canais de cores (3 dimensções)
cat_img = cv2.imread('../assets/fotos/cat.jpg')
cv2.imshow("blank",blank_img)


# 1. Pintando o blank de uma cor qualquer por operação matricial ==============================
# Pintando toda a matriz

blank_img[:] = 0, 0, 255        # Vermelho
cv2.imshow("Vermelho",blank_img)

blank_img[:] = 0, 255, 0        # Green
cv2.imshow("Green",blank_img)
blank_img[:] = 255, 0, 0        # Azul
cv2.imshow("Azul",blank_img)
blank_img[:] = 255, 255, 255        # branco
cv2.imshow("branco",blank_img)
    

# Se quisessemos pintar uma parte específica
blank_img[200:300, 300:400] = vermelho
# cv2.imshow("parte1",blank_img)
blank_img[:100, 50:150] = verde
# cv2.imshow("parte2",blank_img)
blank_img[400:, 200:300] = azul
cv2.imshow("parte3",blank_img)

# 2. Desenhar um retângulo ==============================
# cv2.rectangle(imagem, ponto1, ponto2, cor, thickness) Se thickness = -1 ou cv2.FILLED, pintamos todo o retangulo (grossura)
cv2.rectangle(blank_img, (0,0), (250, 250), verde, -1)
# // = Floor division
cv2.rectangle(blank_img, (0,0), (blank_img.shape[1]//2, blank_img.shape[0]//2), verde, -1)

# 3. Desenhando um círculo ==============================
# cv2.circle(imagem, ponto_central, raio, cor, thickness)
cv2.circle(blank_img, (blank_img.shape[1]//2, blank_img.shape[0]//2), 200, vermelho, -1)
cv2.circle(blank_img, (blank_img.shape[1]//2, blank_img.shape[0]//2), 200, azul, 5)

# 4. Desenhando uma linha ==============================
# cv2.line(imagem, ponto1, ponto2, cor, thickness) -> igual o retangulo
cv2.line(blank_img, (100,100), (blank_img.shape[1]//3, blank_img.shape[0]//3), verde, 2)
cv2.line(blank_img, (100,100), (blank_img.shape[1], blank_img.shape[0]), verde, 2)

# 5. Escrever texto ====================================
# cv2.putText(imagem, texto, ponto_inicial, fontes)
cv2.putText(blank_img, "Asimov Academy", (3, 253), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 255, 255), 3)
cv2.putText(blank_img, "Asimov Academy", (2, 252), cv2.FONT_HERSHEY_COMPLEX, 1.5, vermelho, 3)
cv2.putText(blank_img, "Asimov Academy", (0, 250), cv2.FONT_HERSHEY_COMPLEX, 1.5, azul, 3)


# Dispondo as imagens
cv2.imshow('gato', cat_img)
cv2.imshow('blank', blank_img)

cv2.waitKey(0)