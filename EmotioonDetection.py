import cv2
from deepface import DeepFace
import numpy as np
import os
import sys

aceCascade=cv2.CascadeClassifier(r'C:\Users\HP\AppData\Roaming\Python\Python39\site-packages\cv2\data\haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(1)

if not cap.isOpened():
     cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("cannot open web cam")
    
while True:
    ret,frame = cap.read()
    
    result = DeepFace.analyze(frame, actions = ['emotion'],enforce_detection=False)
       
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
    faces = aceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for(x, y, w, h) in faces:
        cv2.rectangle(frame,(x,y), (x+w, y+h), (0, 255, 0), 2)
    
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    
    cv2.putText(frame,
               result['dominant_emotion'],
               (50, 50),
               font, 3,
               (0, 0, 255), 
               2,
               cv2.LINE_4)
    
    cv2.imshow('orginal video',frame)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

     
  




cap.release()
cv2.destroyAllWindows()
                                   



