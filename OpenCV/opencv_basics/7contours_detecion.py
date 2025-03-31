import cv2
import numpy as np

# importando as Imagens =======================================================
img = cv2.imread('../assets/fotos/cats.jpg')
cv2.imshow('Cats', img)

# desenhando um canva branco do mesmo tamanho que a imagem de trabalho
blank = np.zeros(img.shape, dtype='uint8')
cv2.imshow('Blank', blank)

# transferindo-a para cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# Detecção de contornos ==================================================
blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)# borrar a imagem, com a função GaussianBlur (+ksize (5,5) +blur)
cv2.imshow('Blur', blur)
canny = cv2.Canny(blur, 125, 175)# Funciona detectando descontinuidades no brilho.
cv2.imshow('Canny Edges', canny)

#"For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection."
#cv2.findContours(imagem, modo_deteccao, metodo_aproximacao_contorno)

contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #cv2.RETR_LIST, é o recomendado pela documentação
'''
cv.CHAIN_APPROX_NONE: salva absolutamente todos os pontos de contorno, custoso, imagina se tivessemos uma linha apenas, precisamos de todos os pontos ou apenas seus dois extremos?
cv.CHAIN_APPROX_SIMPLE: Ele remove todos os pontos redundantes e comprime o contorno, economizando memória.
'''



# contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(f'{len(contours)} contornos encontrados!!')

cv2.drawContours(blank, contours, -1, (0,0,255), 1)
cv2.imshow('contornos desenhados', blank)

cv2.waitKey(0)