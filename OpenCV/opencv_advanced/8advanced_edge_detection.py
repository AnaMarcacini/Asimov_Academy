'''
No vídeo anterior sobre edge detection discutimos sobre o Canny Edge Detector. Mas nessa aula, abordaremos outros dois métodos de computar as bordas de uma imagem:
- Método Laplaciano
- Método Sobel 
'''

import cv2
import numpy as np

img = cv2.imread('assets/fotos/park.jpg')

# como vamos analisar edges, primeiro devemos transformar a imagem em P&B
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Imagem em Cinza', cinza)

# MÉTODO LAPLACIANO ================================
'''
O cv2.Laplacian() é o que chamamos de um filtro derivado de segunda ordem, pela definição matemática de Laplace.
Ao contrário dos filtros de primeira ordem que detectam as arestas com base em máximos ou mínimos locais, 
o Laplaciano detecta as arestas em cruzamentos de zero, ou seja, onde o valor muda de negativo para positivo e vice-versa.
'''

# cv2.laplacian(imagem, data_depth)
# data_depth -> ddepth: matriz de intensidade de pixels em uma imagem
laplaciano = cv2.Laplacian(cinza, cv2.CV_64F)
# calcula o valor absoluto por elemento e converte para uint8 (que é de 0 e 255)
laplaciano = np.uint8(np.absolute(laplaciano))
cv2.imshow('Laplaciano', laplaciano)

# MÉTODO DE SOBEL ================================
'''
O filtro Sobel é usado para detecção de borda. 
Funciona calculando o gradiente de intensidade da imagem em cada pixel dentro da imagem. 
Encontra a direção do maior aumento da luz para a escuridão e a taxa de mudança nessa direção.
Para isso temos que calcular Sobel em x e y, pois calculamos o gradiente em relação a uma direção.
'''
# cv2.Sobel(image, ddepth, dx, dy), onde dx e dy representam as direções x e y
x = cv2.Sobel(cinza, cv2.CV_64F, 1, 0)
y = cv2.Sobel(cinza, cv2.CV_64F, 0, 1)

# resultados separados das derivadas com o método de Sobel
cv2.imshow('Sobel X', x)
cv2.imshow('Sobel Y', y)

# combinamos o nosso x e y utilizando uma bitwise operation
combined_sobel = cv2.bitwise_or(x, y)
cv2.imshow('Sobel Combinando x+y', combined_sobel)

# MÉTODO DE CANNY ================================ 
'''
Esse método foi ensinado anteriormente, apenas utilizaremos para comparação aqui
'''
canny = cv2.Canny(cinza, 150, 175)
cv2.imshow('Filtro Canny', canny)

cv2.waitKey(0)