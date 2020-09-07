import cv2
import numpy as np
import face_recognition

imgDharm= face.recognition.load_image_file('imagesBasic/Dharm.jpg')
imgElon=cv2.cvtColor(imgDharm.cv2.COLOR_BGR2RGB)
imgTest=face.recognition.load_image_file('imagesBasic/Dharm Test.jpg')
imgTest=cv2.cvtColor(imgTest.cv2.COLOR_BGR2RGB)

faceLoc=face_recognition.face_locations(imgDharm)[0]
encodeDharm=face_recognition.face_encodings(imgDharm)[0]
cv2.rectangle(imgDharm,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest=face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

results= face_recognition.compare_faces([encodeDharm],encodeTest)
faceDis= face_recognition.face_distance([encodeDharm],encodeTest)
print(results)
cv2.putText(imgTest,f'{results} {faceDis}')

cv2.imshow('Dharm Rajvadiya',imgDharm)
cv2.imshow('Dharm Test',imgTest)
cv2.waitkey(0)
