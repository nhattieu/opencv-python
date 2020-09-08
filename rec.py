import cv2
import numpy as np
import pyrebase
import os
import connect
from PIL import Image

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer/training.yml')

font = cv2.FONT_HERSHEY_SIMPLEX

objects = connect.getInfo()

def getInfoById(id):

    db, storage = connect.connect_firebase()

    info = None

    for object in objects.each():
        if(object.val().get('id') == str(id)):
            info = object.val()

    return info

def rec():

    cap = cv2.VideoCapture(0)

    while cap.isOpened:

        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)

        for(x, y, w, h) in faces:
            
            cur_gray = gray[y : y + h, x : x + w]

            id, acc = recognizer.predict(cur_gray)

            if acc < 40:
                info = getInfoById(id)
                print(info)
                if(info != None):
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0),2)
                    cv2.putText(frame, str(info['name']), (x + 10, y - 10), font, 1, (0, 255, 0), 3)

            else:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255),2)
                cv2.putText(frame, 'Khong biet', (x + 10, y - 10), font, 1, (0, 0, 255), 3)
            



        cv2.imshow('OpenCV', frame)

        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break

    cap.release()
    cv2.destroyAllWindows()


rec()