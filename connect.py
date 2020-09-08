import pyrebase

def connect_firebase():
    config = {
        "apiKey": "AIzaSyDtnB1UUQDfZG0V-9-qJOYdrfEI3_ZM37I",
        "authDomain": "opencv-python-project.firebaseapp.com",
        "databaseURL": "https://opencv-python-project.firebaseio.com",
        "projectId": "opencv-python-project",
        "storageBucket": "opencv-python-project.appspot.com",
        "messagingSenderId": "771693239128",
        "appId": "1:771693239128:web:65c52d9288376891e3632d",
        "measurementId": "G-HGHN035JT3"
    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    storage = firebase.storage()


    return db, storage

def getInfo():

    db, storage = connect_firebase()

    objects = db.child('objects').get()

    return objects