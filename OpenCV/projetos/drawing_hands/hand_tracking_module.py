import cv2
import mediapipe as mp
import numpy as np
import time     # check framerate

from typing import Union

'''
Criando um módulo de tudo que aprendemos, para que não seja necessário repetir toooodo esse código quando formos usar
Utilizaremos apenas requisições
'''

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
webcam_image = np.ndarray
confidence = float
coords_vector = Union[int, list[int]]
rgb_tuple = tuple[int, int, int]
# =========================


# Class ===================
class VanzeDetector():
    def __init__(self, 
                    mode: bool = False, 
                    number_hands: int = 2,   # numero de mãos
                    model_complexity: int = 1, # complexidade do modelo 
                    min_detec_confidence: confidence = 0.5,     # confiança mínima de detecção
                    min_tracking_confidence: confidence = 0.5 #confiança mínima de rastreamento
                ):
        
        # Parametros necessário para inicializar o hands -> solução do mediapipe
        self.mode = mode
        self.max_num_hands = number_hands
        self.complexity = model_complexity
        self.detection_con = min_detec_confidence
        self.tracking_con = min_tracking_confidence

        # Inicializando o hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode,
                                        self.max_num_hands,
                                        self.complexity,
                                        self.detection_con,
                                        self.tracking_con)    
        self.mp_draw = mp.solutions.drawing_utils #importando o módulo de desenho do mediapipe
        self.tip_ids = [4, 8, 12, 16, 20]# ids das regiões da mão que queremos analisar

    def find_hands(self, 
                    img: webcam_image, #passamos a imagem da webcam
                    draw_hands: bool = True): #quermos desenhar as mãos ou não?
        # Correção de cor - converte a imagem BGR (padrão do OpenCV) para RGB (padrão do mediapipe)
        # Isso é necessário porque o mediapipe espera imagens no formato RGB
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Coletando resultados do processo das hands e analisando-os
        self.results = self.hands.process(img_RGB)
        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:
                if draw_hands:
                    self.mp_draw.draw_landmarks(img, hand, self.mp_hands.HAND_CONNECTIONS)  

        return img

    def find_position(self, 
                        img: webcam_image, 
                        hand_number: int = 0, 
                        draw_hands: bool = True):
        self.required_landmark_list = []
        # my_hand = None
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_number]
            # print(my_hand)
            height, width, _ = img.shape
            for id, lm in enumerate(my_hand.landmark):
                center_x, center_y = int(lm.x*width), int(lm.y*height)

                self.required_landmark_list.append([id, center_x, center_y])  

        return self.required_landmark_list

    def fingers_up(self):
        '''
        Para essa função devemos examinar a ponta do dedo do dedo que queremos verificar, para dar o veredito se ele está levantado ou não
        Para isso, vamos analisar sempre a ponta do dedo e dois landmarks abaixo deste. Como por exemplo:
        Se quero saber se o dedo indicador está pra cima, devo analisar o eixo y do LM 8 e do LM 6. Se o y_8 > y_6, significa que o dedo está levantado,
            caso contrário, não está.
        O conceito se repete para todos os outros dedos.
        '''
        fingers = []

        # dedão - analisado diferente por que o dedão se comporta de maneira diferente. Não desce no eixo y que nem os outros dedos
        if self.required_landmark_list[self.tip_ids[0]][1] < self.required_landmark_list[self.tip_ids[0] - 1][1]: fingers.append(1)
        else: fingers.append(0)

        # Para os outros 4 dedos
        for id in range(1, 5):
            if self.required_landmark_list[self.tip_ids[id]][2] < self.required_landmark_list[self.tip_ids[id] - 2][2]: fingers.append(1)
            else: fingers.append(0)

        return fingers

    def draw_in_position(self,
                            img: webcam_image,
                            x_vector: coords_vector, 
                            y_vector: coords_vector,
                            rgb_selection: rgb_tuple = (255, 0, 0),
                            thickness: int = 10):
        x_vector = x_vector if type(x_vector) == list else [x_vector]
        y_vector = y_vector if type(y_vector) == list else [y_vector]

        for x, y in zip(x_vector, y_vector):
            cv2.circle(img, (x, y), thickness, rgb_selection, cv2.FILLED)

        return img
        
# Main ==================== 
def main():
    # coletando o framerate e capturando o vídeo
    previous_time = 0
    current_time = 0
    capture = cv2.VideoCapture(0)# numero da câmera, 0 é a webcam padrão
    #classe
    Vanze = VanzeDetector()

    while True:
        #Capturando a imagem da webcam
        _, img = capture.read()# retora o sucesso da captura e a imagem capturada (ignoramos o sucesso)
        
        #manipulando a o frame
        img = Vanze.find_hands(img) #, draw_hands=False)
        landmark_list = Vanze.find_position(img) #, draw_hands=False)
        if landmark_list:  # Verifica se a lista de landmarks não está vazia
            print(landmark_list[8]) # # printa o landmark do dedo indicador

        current_time = time.time()
        fps = 1/(current_time - previous_time)
        previous_time = current_time

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_DUPLEX, 2, (255,0,255), 3)
        # Exibindo a imagem capturada com a detecção de mãos
        cv2.imshow("Image", img)
        cv2.waitKey(1)
#para teste de classe
if __name__ == '__main__':
    main()
