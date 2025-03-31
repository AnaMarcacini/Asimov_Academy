import cv2
import numpy as np

# Lendo a imagem - 3 channels
img = cv2.imread('../assets/fotos/cat.jpg')
img = cv2.imread('../assets/fotos/park.jpg')
###################################################################################


# 1. Convertendo para P&B (grayscale ou greyscale) --> cv2.cvtColor significa convertcolor -> (imagem, código de conversão)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # codigo de converção COLOR_BGR2GRAY
cv2.imshow('gatito cinza', gray)
###################################################################################

# 2. Blur (borrando)
# cv2.GaussianBlur (imagem, ksize, sigmaX) (tupla de dois valores e que precisam ser ímpares) Para aumentar o blur, basta aumentar o ksize
blurred = cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT)
# blurred = cv2.GaussianBlur(img, (9, 9), cv2.BORDER_DEFAULT)
cv2.imshow('blur', blurred)
###################################################################################


# 3. Edge Cascade - detecção de borda
'''
A detecção de borda é uma técnica de processamento de imagem para encontrar os limites dos objetos dentro das imagens. Ele funciona detectando descontinuidades no brilho. Canny (que da nome a função utilizada, é um método de edge detection)
Quanto menor o valor de Threshold no processo de Canny, maior a chance do método detectar bordas.
'''
# cv2.Canny(imagem, threshold1, threshold2)
canny = cv2.Canny(img, 250, 200)    # poucas bordas
# canny = cv2.Canny(img, 20, 50)      # muitas bordas
cv2.imshow('canny transf', canny)
###################################################################################

# Para que possamos diminuir as bordas de outra maneira, podemos dar um blur (borrar) a imagem
canny_blurred = cv2.Canny(blurred, 250, 200)
cv2.imshow('canny blurred', canny_blurred)
###################################################################################

# 4. Dilating Image - Dilatação de imagem
'''
A dilatação é um operador de transformação morfológica usado para aumentar o tamanho ou a espessura do objeto em primeiro plano em uma imagem. 
'''
dilated = cv2.dilate(canny_blurred, (9,9), iterations=3)
cv2.imshow('dilated', dilated)
###################################################################################

# 5. Eroding Imagem - Corroendo a imagem
'''
Basicamente o processo contrário do dilating. Torna as linhas mais finas, maior precisão de imagem. Conseguimos reverter o processo pro passo de edge cascade
'''
eroded = cv2.erode(dilated, (9,9), iterations=3)
cv2.imshow('eroded', eroded)
###################################################################################

# 6. Resize - já cobrimos em aulas passadas, mas há outras opções na função cv2.resize()
resized = cv2.resize(img, (300, 300))   # essa função ignora o ratio da imagem (proporção)
# Por padrão o cv2.resize executa uma interpolação por debaixo dos panos que é a cv2.INTER_AREA (util para diminuição de imagens)
cv2.imshow('resized', resized)

# Mas se quisermos fazer com que a imagem cresça, devemos utilizar
# cv2.INTER_LINEAR -> rápida mas com qualidade menor, ou
# cv2.INTER_CUBIC -> mais lenta, porém com a melhor qualidade
###################################################################################

# 7. Crop - cortar a imagem / já cobrimos em aulas passadas
corte = img[50:200, 200:400]
cv2.imshow('corte', corte)

# 8. Lembrando que é possível cortar a imagem direito no imshow()
cv2.imshow('corte direto', img[50:200, 200:400])

# Dispondo a imagem
cv2.imshow('gatito', img)

# WaitKey
cv2.waitKey(0)
