import cv2
import numpy as np

'''
O openCV trabalha de maneira padrão em BGR (Blue, Green, Red)  que é extremamente semelhante ao RGB(Red, Green, Blue), colorspace mais utilizado
ColorSpaces são maneiras diferentes de representar uma mesma imagem, em espaços de cor diferentes. GrayScale é um tipo de ColorSpace também
Para representação de impressões utilizamos o CMYK (Ciano, Magenta, Amarelo, Preto), que representa a mistura dessas cores em um fundo branco,
enquanto o RGB ou BGR, representa a combinação de Vermelho, Verde e Azul em um fundo preto.

RGB: praticamente padrão
BGR: representado pelo OpenCV como padrão
CMYK: representação para impressões em mundo real
'''
img = cv2.imread('../assets/fotos/cat.jpg')

print(img)
# BGR para Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Cinza', gray)

# BGR para HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

# BGR para L*a*b
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('L*a*b', lab)

# BGR para RGB --> troca o vermelho com o azul
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)

# HSV para BGR
lab_bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
cv2.imshow('LAB para BGR', lab_bgr)


cv2.waitKey(0)
