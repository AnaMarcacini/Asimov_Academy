import cv2
import numpy as np

'''
Cascade Classifier: 
Um Cascade Classifier (classificador em cascata) é uma técnica usada em Visão Computacional para detecção de objetos 
em imagens. Ele funciona através da combinação de vários classificadores simples em uma estrutura em cascata, 
que é treinada para identificar características específicas do objeto de interesse.

Imagine que você queira encontrar rostos em uma imagem. O Cascade Classifier irá analisar a imagem em diferentes 
estágios, cada estágio usando um classificador diferente. Por exemplo, o primeiro estágio pode usar um classificador 
simples para detectar bordas retas que possam fazer parte do rosto, enquanto o segundo estágio pode usar um 
classificador mais complexo para identificar as características do rosto, como os olhos, nariz e boca.

Cada estágio do Cascade Classifier é projetado para rejeitar rapidamente as partes da imagem que não contêm o objeto 
de interesse. Isso é importante porque a detecção de objetos pode ser computacionalmente cara e demorada, e a maioria 
das partes da imagem não contém o objeto de interesse.

Ao combinar vários classificadores em cascata, o Cascade Classifier pode alcançar alta precisão de detecção, enquanto 
mantém o tempo de processamento baixo. Essa técnica é usada em muitas aplicações de Visão Computacional, como 
reconhecimento facial, detecção de veículos em imagens de trânsito, entre outros.

Diferença Face Recognition x Face Detection

Para essa aula é necessário baixar o haarcascade_frontalface_default.xml do link:
https://github.com/opencv/opencv/tree/master/data/haarcascades
que contém diversos modelos ja treinados para casos diferentes utilizando o método de Cascade Classifier
'''

# img = cv2.imread('assets/fotos/lady.jpg')
# img = cv2.imread('assets/fotos/group 1.jpg')
img = cv2.imread('assets/fotos/group 2.jpg')
# img = cv2.imread('assets/fotos/grupo.png')
# img = cv2.imread('assets/fotos/grupo2.png')
cv2.imshow('Pessoa', img)


# Vamos utilizar imagens em cinza pois em image recognition não analisamos tom de pele ou semelhantes, apenas traços específicos
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Pessoa Cinza', cinza)

cascade_class = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')    # classe

# é uma instancia da classe CascadeClassifier, para identificar o rosto na imagem e retornar o retangulo que envolve o rosto
retangulos = cascade_class.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=12)
# scaleFactor -> Parâmetro que especifica o quanto o tamanho da imagem é reduzido em cada escala de imagem. Por padrão = 1.1
# minNeighbors -> Parâmetro que especifica quantos vizinhos cada retângulo candidato deve ter para retê-lo. Por padrão = 3

print(f'Contagem de rostos: {len(retangulos)}')   # representa a quantidade de rostos que foram encontrados a partir da quantidade de retangulos
print(retangulos) # o que essa variável representa?

'''
A variavel retangulo nos retorna 4 valores como visto, sendo eles:
x -> coordenada x
y -> coordenada y
w -> largura 
h -> altura
'''

for x, y, w, h in retangulos:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)

cv2.imshow('Pessoa com retangulo', img)

'''
TESTAR IMAGENS DE GRUPO
Nas imagens de grupo teremos resultados levemente errados.
Isso ocorre pois o método de Haar Cascade é extremamente sensível a imagens com ruído.
Para que possamos corrigir esse fato, devemos alterar o parâmetro de minNeighbors.

É possível aplicar Haar Cascades a vídeos, é o que faremos na próxima aula

Lembrando que Haar Cascades é o método mais fácil de se utilizar, porém não o melhor
Tem um setup rápido e uma precisão relativamente boa, mas é muito sensível a ruído, não recomendo para
projetos profissionais de visão computacional.
'''

'''
Sugerir que os alunos tentem implementar essa funcionalidade nos projetos de vídeo lidos diretamente da webcam
Dar a brecha no final da aula para que seja implementado por eles. Na aula seguinte tem a solução
'''

cv2.waitKey(0)
