'''
3. Resize: redimensiona a imagem
4. Flipping: inverte a imagem
5. Cropping: cortar as imagens a partir de coordenadas
https://docs.opencv.org/3.4/d4/d61/tutorial_warp_affine.html
'''

import cv2
import numpy as np

img = cv2.imread('../assets/fotos/park.jpg')
cv2.imshow('original', img)

# Definições de funções 
def translate(img, x, y):
    '''
    Translation(translação): ato de movimentar um objeto de um ponto a outro
    -x      ESQUERDA    |    -y      ACIMA   |    x       DIREITA   |    y       ABAIXO
    '''
    # esse trecho de código criará uma matriz de duas linhas onde a ultima coluna diz respeito diretamente a x e y
    translation_matrix = np.float32([[1,0,x],[0,1,y]])    # matriz de translação:
    # coletamos então as dimensões da nossa imagem e as inserimos em uma tupla
    dimensions = (img.shape[1], img.shape[0])
    # e retornamos a função warpAffine, transformação afim, que retorna nosso resultado transladado
    return cv2.warpAffine(img, translation_matrix, dimensions)

img_tr = translate(img, 100, 250)
cv2.imshow('movida', img_tr)

def rotate(img, angle, rotation_point=None):
    '''
    2. Rotation: rotaciona/gira a imagem

    rotation_point = eixoo de rotação | default=centro da imagem
    '''
    # LEMBRANDO: coletamos o width e height assim pois temos 3 valores: height, width e channels de cor
    height, width = img.shape[:2]

    if rotation_point is None:
        rotation_point = (width//2,height//2)   # floor division
    
    # getRotationMatrix2D (ponto_de_rotação, angulo, escala)
    rotation_matrix = cv2.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width,height)

    return cv2.warpAffine(img, rotation_matrix, dimensions)

rotated = rotate(img, -45)
#rotated = rotate(img, -90)
# rotated = rotate(img, -180)
cv2.imshow('rotacionada', rotated)

# Para resizing, flipping e cropping, temos funções próprias do openCV, então basta executá-las

# Flipping: inverte um array 2D
# Aceita apenas inteiros:
flip = cv2.flip(img, 1) # horizontal
flip = cv2.flip(img, 0) # vertical 
flip = cv2.flip(img, -1) # vertical e horizontal 
cv2.imshow('invertida', flip)

# Resizing & Cropping: recapitulação
resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)
# Como dito na aula passada: cv2.INTER_CUBIC -> mais lenta, porém com a melhor qualidade
cv2.imshow('redimensionada', resized)
cropped = img[100:300, 400:500]
cv2.imshow('cortada', cropped)


cv2.waitKey(0)
