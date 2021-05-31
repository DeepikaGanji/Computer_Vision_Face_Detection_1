import cv2  

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')         # Loading the cascade

cap = cv2.VideoCapture(0)           # To capture video from webcam

while True:
    
    _, img = cap.read()         # Read the frame

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        # Converting image to grayscale

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)         # Detecting the faces

    for (x, y, w, h) in faces:          

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255 , 0), 2)         # To draw rectangle around each face

    cv2.imshow('img', img)          # To Display

    k = cv2.waitKey(30) & 0xff          # Display stops if escape key is pressed 

    if k==27:

        break

cap.release()       # Release the VideoCapture object
