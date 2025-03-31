import cv2

# Lendo vídeos, temos que criar um objeto de captura
# Existe o parâmetro dentro dessa função que pode ser um int (para especificar o numero da webcam)
# Ou pode ser um path para um vídeo qualquer
cap = cv2.VideoCapture('../assets/videos/dog.mp4')

# Ler vídeos é um pouquinho diferente de ler imagens, pois temos que ler frame a frame de um vídeo
# Pra isso criamos um loop que opera sobre a função .read() do objeto cap (que é o VideoCapture)
while True:
    # confirmacao, frame = cap.read()
    _, frame = cap.read()

    cv2.imshow('video do dog', frame)

    # Não é necessário focar nessa explicação MAS:
    # cv2.waitKey() retorna um 32 Bit integer (pode depender da plataforma). 
    # O key input (input do teclado) é um ASCII de 8 Bit integer value. Então tu só precisa se preocupar com esses 8, os outros podem ser zero. 
    # 0xFF é uma máscara pros 8bits finais
    # é uma bitwise operation
    # É possível alcançar isso com:
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

    # (-215 assertion failed), openCV não conseguiu achar frames ao final do vídeo. O vídeo acabou
    # Esse mesmo erro aconteceria se enviassemos um path errado de imagem.

cap.release()
cv2.destroyAllWindows()