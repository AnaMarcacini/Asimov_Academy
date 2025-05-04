import cv2
import numpy as np

# criando um canva em completamente preto (0)
blank = np.zeros([400,400], dtype='uint8')
# cv2.imshow('Retangulo', blank)

# IMPORTANTE: utilizando as funções .copy() do numpy para não ter problemas de alterar duas matrizes simultâneamente
rectangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv2.circle(blank.copy(), (200,200), 200, 255, -1)

cv2.imshow('Retangulo', rectangle)
cv2.imshow('Circulo', circle)

# bitwise AND -> a intersecção das duas imagens (onde ambos são 1 [brancos])
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow('Bitwise AND', bitwise_and)

# bitwise OR -> intersecção onde há qualquer um dos dois objetos envolvidos
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow('Bitwise OR', bitwise_or)

# bitwise XOR -> intersecção apenas as áreas onde há apenas UM OU OUTRO
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT -> intersecção apenas onde não há nada (0)
bitwise_not = cv2.bitwise_not(circle)
cv2.imshow('Circulo NOT', bitwise_not)

cv2.waitKey(0)