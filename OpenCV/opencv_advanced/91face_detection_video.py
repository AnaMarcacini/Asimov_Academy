import cv2
import numpy as np

# utilizamos a função do cv2 para capturar o vídeo da nossa webcam de número zero
capture = cv2.VideoCapture(0)

# instanciando o CascadeClassifier class
cascade_class = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')    # classe


while True:
    # essa função retorna se foi bem sucedido é o frame específico da camera
    _, img = capture.read()

    # transferindo para gray pois o reconhecimento utiliza traços e não cores
    cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # identificando retangulos de rostos
    retangulos = cascade_class.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=12)
    
    # tendo as coordenadas, podemos desenhar os retangulos na imagem
    for x, y, w, h in retangulos:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), thickness=2)

    # temos que dispor esse frame
    cv2.imshow("Gravacao do r7", img)

    # e adicionar a opção do usuário sair do loop
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break
