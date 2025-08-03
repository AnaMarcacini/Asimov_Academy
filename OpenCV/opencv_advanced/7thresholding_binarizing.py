'''
Nessa aula falaremos de Thresholding segmentação de imagens:
    - No processamento digital de imagens, Thresholding é o método mais simples de segmentação de imagens. 
    - A partir de uma imagem em tons de cinza, criamos imagens binárias

Existem algumas condições para que a separação via Threshing funcione melhor:
- Ruído baixo
- Maior variação intraclasse do que variação interclasse, ou seja, pixels de um mesmo grupo têm intensidades mais próximas entre si do que pixels de outro grupo (se o rosto for igualmente iluminado irá dar certo, agora se o rosto tem s'um lado iluminado e o outro possui uma sombra dificulta o processo)
- Luz homogênea
- etc
'''
import cv2

img = cv2.imread('assets/fotos/cats.jpg')
# cv2.imshow('Gatitos normais', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Tons de cinza', gray)

'''
Para os threshs simples usaremos a função cv2.threshold(), todos derivados da imagem em cinza
threshold(src, thresh, maxval, type[, dst])
threshold(imagem, valor_de_thresh, max_val, metodo_de_thresholding)

metodo_de_thresholding -> (ver imagem exemplo)
cv.THRESH_BINARY: focaremos nesses dois
cv.THRESH_BINARY_INV: focaremos nesses dois
cv.THRESH_TRUNC
cv.THRESH_TOZERO
cv.THRESH_TOZERO_INV
Há uma imagem em assets/didaticas que demonstra os outros métodos possíveis de Thresh

O método retorna duas saídas. A primeira é o valor de Threshing que foi usado e a segunda saída é a imagem com limite.
valor_de_thresh -> sensibilidade de transformar os pixels em preto e branco
threshold, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY) quase tudo fica branco
threshold, thresh = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY) quase tudo fica preto

'''

# Thresholding simples
threshold, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
# passa a imagem, sensibilidade (qaul valor se diferencia entre o branco e o preto, valor maximo de 255) e o método de thresholding
# cv2.imshow('Thresholding simples', thresh)

# Thresholding invertido simples - provável imagem predominantemente branca
threshold, thresh_inv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('Thresholding invertido simples', thresh_inv)

'''
Ambos métodos acima utilizam o conceito de Thresholding Global, ou seja, filtrar toda a imagem por um valor de Thresh único, nesse caso de 150 a 255.
O problema aqui é que ter apenas um valor de T pode não ser suficiente. Devido a variações nas condições de iluminação, sombreamento, etc., 
pode ser que um valor de T funcione para uma determinada parte da imagem de entrada, mas falhe completamente em um segmento diferente.
Em vez de desistir imediatamente e afirmar que a visão computacional tradicional e o processamento de imagens não funcionarão para esse problema,
em vez disso, podemos aproveitar o Thresholding Adaptativo.
Como o nome sugere, Thresholding Adaptativo considera um pequeno conjunto de pixels vizinhos por vez, calcula T para essa região local específica e, em seguida, executa a segmentação.

adaptiveThreshold(imagem, valor_maximo, metodo_adaptativo, metodo_de_thresholding, tamanho_da_vizinhança, Constante_C)
metodo_adaptativo ->
cv.ADAPTIVE_THRESH_MEAN_C: O valor limite é a média da área da vizinhança menos a constante C
cv.ADAPTIVE_THRESH_GAUSSIAN_C: O valor limite é uma soma ponderada gaussiana dos valores da vizinhança menos a constante C.
'''

# Thresholding Adaptativo
adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 9)
# adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 9)
# cv2.imshow('Thresholding Adaptativo', adaptive_thresh)

cv2.waitKey(0)