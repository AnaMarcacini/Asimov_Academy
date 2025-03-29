import numpy as np
from skimage.transform import rescale
import scipy
import scipy.ndimage
import cv2
import os

FILENAME = 'teste_text.png'
PATH = os.path.join('assets', FILENAME)
img = cv2.imread(PATH)
cv2.imshow('original_image', img)

# separando as cores e diminuindo a dimensao para diminir o custo computacional
b_scaled = rescale(img[:,:,0], 0.25)
g_scaled = rescale(img[:,:,1], 0.25)
r_scaled = rescale(img[:,:,2], 0.25)
img_scaled = np.stack([b_scaled, g_scaled, r_scaled], axis=2) # colocando uma matriz em cima da outra
cv2.imshow('scaled_image', img_scaled)

# Box Blur
box_blur = (1 / 9) * np.array([[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]])
# Normalizar = 1 pixel --> a soma dos dados deve dar 1 (3x3 = 9) portanto 1/9*matriz
# box_factor = 1/box_blur.sum()*box_blur


# Gaussian Blur 3x3
gaussian_3 = (1 / 16) * np.array([[1, 2, 1],
                                  [2, 4, 2],
                                  [1, 2, 1]])
# Gaussian Blur 5x5
gaussian_5 = (1 / 256) * np.array([[1, 4, 6, 4, 1],
                                   [4, 16, 24, 16, 4],
                                   [6, 24, 36, 24, 6],
                                   [4, 16, 24, 16, 4],
                                   [1, 4, 6, 4, 1]])


# BOX Blur 10x10
box_blur_big = np.ones([10,10])
box_blur_big = box_blur_big/box_blur_big.sum()


# BOX Blur 10x10
box_blur_big2 = np.ones([100,100])
box_blur_big2 = box_blur_big2/box_blur_big2.sum()





kernels = [box_blur,box_blur_big,box_blur_big2, gaussian_3, gaussian_5]
kernel_name = ['Box Blur', "BOX Blur 10x10", "BOX Blur 100x100", '3x3 Gaussian Blur', '5x5 Gaussian Blur']

'''
O código entra em um loop, onde itera pelos kernels definidos e seus nomes correspondentes.
Para cada kernel, ele executa convolução usando scipy.ndimage.convolve. 
A função np.atleast_3d é usada para garantir que o kernel tenha o formato apropriado 
para convolução com uma imagem de 3 canais. Torna o kernel tridimensional, 
combinando com a profundidade da imagem.
O parâmetro mode='nearest' em convolve especifica que a convolução deve usar o modo 
de borda mais próximo, o que significa que o tamanho da imagem de saída corresponde 
ao tamanho de entrada.
'''

for kernel, name in zip(kernels, kernel_name):
    conv_im1 = scipy.ndimage.convolve(img, np.atleast_3d(kernel), mode='nearest')
    cv2.imshow(name, conv_im1)

cv2.waitKey(0)