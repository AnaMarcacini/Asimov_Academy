import cv2
import numpy as np

# utilizamos a função do cv2 para capturar o vídeo da nossa webcam de número zero
capture = cv2.VideoCapture(0)

while True:
    # essa função retorna se foi bem sucedido é o frame específico da camera
    success, img = capture.read()

    # temos que dispor esse frame
    cv2.imshow("Euzinha", img)

    # e adicionar a opção do usuário sair do loop
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break


