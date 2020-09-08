import cv2
import numpy as np
import os
import connect
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'images'

def getImageWithId(path):

    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

    ids = []
    faces = []

    # print(imagePaths)

    for imagePath in imagePaths:

        faceImg = Image.open(imagePath)

        facenp = np.array(faceImg, 'uint8')


        # print(facenp)
        print(imagePath)

        id = int(imagePath.split('\\')[1].split('.')[0])

        ids.append(id)
        faces.append(facenp)

        cv2.imshow('Training', facenp)
        cv2.waitKey(1) & 0xFF == ord('q')

    return faces, ids

def train():

    faces, ids = getImageWithId(path)
    recognizer.train(faces, np.array(ids))

    if not os.path.exists('recognizer'):
        os.mkdir('recognizer')

    recognizer.save('recognizer/training.yml')

    db, storage = connect.connect_firebase()
    # storage.child('recognizer/training.yml').put('recognizer/training.yml')

    print('Training successfully!')

    cv2.destroyAllWindows()

train()