import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
for i in range(0, 113):
    np_img = np.array(Image.open('face_dataset/Person1.' + str(i) + '.jpg'), 'uint8')
    faces.append(np_img)
    
for i in range(1, 114):
    np_img = np.array(Image.open('face_dataset/Person2.' + str(i) + '.jpg'), 'uint8')
    faces.append(np_img)

recognizer.train(faces, np.array(([0] * 113) + ([1] * 114)))
recognizer.write('trained/recognizer.yml')