import cv2

# Função imread
# pega uma imagem de um path e transforma em uma matriz.
img = cv2.imread('../assets/fotos/cat.jpg')

# Função imshow(), mostra uma matriz em uma tela
# Fica ali até ser fechada ou o programa encerrar 
# Nesse caso estamos lendo uma imagem pequena
# cv2.imshow('Janela do Gato', img)

# Caso tentemos ler uma imagem grande, a janela não se adaptará
img_grande = cv2.imread('../assets/fotos/cat_large.jpg')
cv2.imshow('Janela grande', img_grande)

# Função waitKey() para não fechar a janela
cv2.waitKey(0) # espera o usuario digitar zero para continuar o codigo 