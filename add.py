import cv2
import numpy as np
import pyrebase
import os
import connect


def add_object(id, name):
    db, storage = connect.connect_firebase()

    data = {
        "id": id,
        "name": name,
    }

    db.child('objects').push(data)

# def name_img(id, name, count):
#     db = connect_firebase()

#     return db.child("objects").child({"id": id, "name": name}).child("images").push({"img": name + '.' + str(id) + '.' + str(count) + 'jpg'})

def add():

    id = input('Enter your ID: ')
    name = input('Enter your Name: ')

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    add_object(id, name)
    # db, storage = connect_firebase()
    count = 0

    while cap.isOpened:

        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)

        for(x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0),2)
            count+=1

            if not os.path.exists('images'):
                os.mkdir('images')

            cv2.imwrite('images/' + str(id) + '.' + str(count) + '.jpg' , gray[y : y + h, x : x + w])

        cv2.imshow('Add Object', frame)

        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break

        if count >= 100:
            break

    cap.release()
    cv2.destroyAllWindows()


add()
