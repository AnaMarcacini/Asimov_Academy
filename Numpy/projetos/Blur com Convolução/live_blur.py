import cv2
import numpy as np
import scipy
import scipy.ndimage
from scipy import signal

def generate_kernel(kernlen=5, std=5):
    '''
    Retorna 2D Gaussian kernel array

    - A função signal.gaussian da biblioteca scipy é usada para gerar um kernel gaussiano 1D.
    - Para converter o kernel Gaussiano 1D em um kernel Gaussiano 2D, a função np.outer é usada.
    - Nesse caso, é necessário generate_kernel1d (o kernel gaussiano 1D) como ambos os vetores de entrada, multiplicando efetivamente o kernel 1D por si mesmo, 
    resultando em um kernel gaussiano 2D.
    - Finalmente, a função retorna o kernel Gaussiano 2D gerado como uma matriz numpy 2D.
    '''
    generate_kernel1d = signal.gaussian(kernlen, std=std).reshape(kernlen, 1)
    generate_kernel2d = np.outer(generate_kernel1d, generate_kernel1d) # multiplica ele por ele mesmo
    return generate_kernel2d

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

kernel = generate_kernel(23, std=20)

kernel_tile = np.tile(kernel, (3, 1, 1))
kernel_sum = kernel.sum()
kernel = kernel / kernel_sum

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    '''
    O OpenCV cv2.CascadeClassifier (aqui representado como face_cascade) é usado para detectar rostos no quadro em tons de cinza. 
    A função detectMultiScale detecta objetos (rostos) em diferentes escalas na imagem.
    Vários parâmetros são definidos: 
    scaleFactor ajusta a escala da imagem entre a detecção em várias escalas. 
    minNeighbours define o número de vizinhos que uma região deve ter para ser considerada uma face. 
    minSize especifica o tamanho mínimo do rosto detectado.
    flags determinam o modo de imagem em escala.
    '''
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for x, y, w, h in faces:  
        # frame[y:y+h, x:x+w] = scipy.ndimage.convolve(frame[y:y+h, x:x+w], np.atleast_3d(kernel), mode='nearest')
        frame[y:y+h, x:x+w] = cv2.GaussianBlur(frame[y:y+h, x:x+w] ,(23,23), cv2.BORDER_DEFAULT)
    
    # display the resulting frame
    cv2.imshow('AsimoVideo', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()