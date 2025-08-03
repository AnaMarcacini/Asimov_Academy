import cv2
import mediapipe as mp
import numpy as np
import time
import os       # para acessar nossas imagens
from math import ceil

import hand_tracking_module as htm

# Tipagem =================
'''
Type Hints podem ser usadas por ferramentas como IDEs e verificadores de tipo para fornecer informações adicionais sobre o código.
    Por exemplo, uma IDE pode usar Type Hints para fornecer sugestões de código e verificar se você está usando o tipo correto de dados em uma variável.
Type Hints podem ser usadas para documentar o código. Isso pode ser útil se você estiver trabalhando em um projeto com várias pessoas, 
    pois permite que você especifique o tipo de dados que uma variável deve conter.
Type Hints podem ser usadas para verificar se o código está usando o tipo correto de dados em uma variável. Isso pode ser útil para encontrar 
    erros de digitação ou erros de lógica que podem ser difíceis de encontrar em tempo de execução.
Type Hints podem ser usadas para otimizar o código em tempo de execução. Por exemplo, se você usar Type Hints para especificar que uma variável contém um número inteiro, 
    o interpretador Python pode usar uma implementação mais rápida de operações matemáticas em vez de uma implementação genérica que funciona com qualquer tipo de dados.
'''
coordinates = int
# =========================

# Functions ===============
def draw_and_return_coords(xa: coordinates, 
                           ya: coordinates, 
                           x: coordinates, 
                           y: coordinates):
    if xa == 0 and ya == 0:
        xa, ya = x, y
    # caso não seja, desenha a linha do P0 ao ponto atual
    else:
        cv2.line(img, (xa, ya), (x, y), draw_color, thickness)
        cv2.line(drawing_canvas, (xa, ya), (x, y), draw_color, thickness)

    # e se reinicia o processo
    xa, ya = x, y

    return xa, ya

# =========================

# lendo todas files no nosso folder e criando uma lista de imagens que serão lidas pelo cv2
# folder_path = "headers_folder"
folder_path = "final_headers"
files = os.listdir(folder_path)
overlay_images = []

# para cada imagem, leremos e apendamos na lista de imagens
for image_path in files:
    image = cv2.imread(os.path.join(folder_path, image_path))
    overlay_images.append(image)

# o header principal (inicial) vai ser a nossa primeira imagem, dado a maneira que gravamos o nome dos pngs
header = overlay_images[0]

# inicia-se a camera e coleta suas specs
capture = cv2.VideoCapture(0)
cam_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
cam_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# hand_tracking class   
Vanze = htm.VanzeDetector(min_detec_confidence=0.85)    # minimizar erros
x_anterior, y_anterior = 0, 0

# Definir o tamanho inicial do pincel
thickness = 5

# Definir a cor da pintura
draw_color = (9, 232, 225)

'''
Definindo um novo canva para registrar o desenho
para isso vamos usar uma matriz do numpy (height, width, channels[cores])
np.uint8 -> unsigned integer de 0 a 255 (2^8)
agora, ao invés de desenhar na imagem da camera, sobreporemos esse canva, retirando os 0
'''
drawing_canvas = np.zeros((cam_height, cam_width, 3), np.uint8) 

# loop para colar o header e pintar a tela
while True:
    '''
    1. import image
    2. achar os landmarks - usando o module
    3. Checar quais dedos estão levantados - para selecionar os necessários
    4. Drawing mode - dedo indicador acima
        - Free drawing
    5. If eraser mode - dois dedos acima
        - Select, not draw
    6. Selecting size mode - três dedos pra cima
    '''
    # 1. import image
    _, img = capture.read()
    img = cv2.flip(img, 1)  # invertendo a imagem para que o desenho seja natural, intuitivo
    
    # 2. achar os landmarks - usando o module
    img = Vanze.find_hands(img)#, draw_hands=True)
    landmark_list = Vanze.find_position(img)

    if len(landmark_list) != 0:
        #     print(landmark_list)
        x1, y1 = landmark_list[8][1:]       # dedo indicador - acessar imagem nos assets
        x2, y2 = landmark_list[12][1:]      # dedo do meio
        x3, y3 = landmark_list[16][1:]      # dedo anelar

    # 3. Checar quais dedos estão levantados - para selecionar os necessários
        fingers = Vanze.fingers_up()
        # print(fingers)

    # Se qualquer seleção for feita, devemos zerar o nosso xp e yp
    # 4. Drawing mode
        if fingers[1] and not (fingers[2] or fingers[3] or fingers[4]):
            print('drawing mode')
            # draw_color = (9, 232, 225)  
            draw_color = (254, 220, 156)

            # dividindo o thickness por dois pq estamos tratando de raio [era possível trabalhar com cv2.circle (testar)]
            # img = Vanze.draw_in_position(img, [x1], [y1], draw_color, int(thickness/2))
            cv2.circle(img, (x1, y1), int(thickness/2), draw_color, -1)
            x_anterior, y_anterior = draw_and_return_coords(x_anterior, y_anterior, x1, y1)

            header = overlay_images[1]

    # 5. Moving mode
        elif fingers[1] and fingers[2] and not (fingers[3] or fingers[4]):
            print('moving mode')            
            x_anterior, y_anterior = 0, 0
            header = overlay_images[2]
    
    # 6. Selecting size mode
        elif fingers[1] and fingers[2] and fingers[3] and not (fingers[4]):
            print('sizing mode')
            # draw_color = (186, 222, 9) 
            draw_color = (9, 232, 225)
            x_anterior, y_anterior = 0, 0

            thickness = ceil(x2/10) if x2 > 1 else thickness

            cv2.circle(img, (x1, y1), int(thickness/2), draw_color, -1)
            header = overlay_images[3]

    # 7. Erasing mode
        elif not (fingers[1] and fingers[2] and fingers[3] and fingers[4]):
            print('Eraser mode')

            draw_color = (0, 0, 0)
            # img = Vanze.draw_in_position(img, [x1], [y1], draw_color, int(thickness/2))
            
            cv2.circle(img, (x1, y1), int(thickness/2), draw_color, -1)
            x_anterior, y_anterior = draw_and_return_coords(x_anterior, y_anterior, x1, y1)

            header = overlay_images[-1]
            
    # If none of those commands, return to main header
        else: 
            x_anterior, y_anterior = 0, 0
            header = overlay_images[0]

    # Processo de criação de mascara para que seja possível dar o merge entre as imagens
    # criando uma imagem em cinza do nosso drawing_canvas -> é uma parte complicada, fazer com calma
    # .cvtColor é uma função que permite converter uma imagem de um "colorspace" para outro. Como é o exemplo de BGR para RGB
    img_gray = cv2.cvtColor(drawing_canvas, cv2.COLOR_BGR2GRAY)

    # convertendo a imagem para binário e ao mesmo tempo invertendo-a
    # Thresholding significa do inglês limiarização. É um método simples de segmentação de imagens e pode ser usado no processo de binarização
    # NOTE iniciar jupyter de threshold
    _, img_inverse = cv2.threshold(img_gray, 50, 255, cv2.THRESH_BINARY_INV)
    img_inverse = cv2.cvtColor(img_inverse, cv2.COLOR_GRAY2BGR) # passando para BGR para fazer o merge, visto que a nossa imagem principal é BGR

    # NOTE iniciar o jupyter de bitwise

    # bitwise_and(src1, src2) -> dst     @Computes bitwise conjunction of the two arrays (dst = src1 & src2)
    img = cv2.bitwise_and(img, img_inverse)
    # bitwise_or(src1, src2) -> dst      @Calculates the per-element bit-wise disjunction of two arrays  (dst = src1 // src2)
    img = cv2.bitwise_or(img, drawing_canvas)

    # colando o header correto
    img[0:header.shape[0], 0:cam_width] = header

    # solução possível, blend, mas não uma sobreposição
    # img = cv2.addWeighted(img, 0.5, drawing_canvas, 0.5, 0)

    cv2.imshow("Asimov Image", img)
    cv2.imshow("Drawing Canvas", drawing_canvas) # -> mostrar na aula
    cv2.waitKey(1)  

