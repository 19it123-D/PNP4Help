import cv2
import numpy as np
import face_recognition
import os

path='ImagesAttendance'
images=[]
classNames=[]
myList=os.listdir(path)
print(myList)
for cl in MyList:
    currentImg = cv2.imread(f'{path}/{cl}')
    images.append(currentImg)
    classNames.append(os)

def findEncodings(images):
    encodeList=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList=[]
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datatime.now()
            dtString = now.strftime('%H:%M:%s')
            f.writelines(f'\n{name},{dtString}')

 encodeListKnown=findEncodings(images)
print('encoding complete')

cap = cv2.videoCapture(0)

while True:
    success,img= cap.read()
    imgs=cv2.resize(img,(0,0),None,0,25,0,25)
    imgs=cv2.cvtColor(imgs,COLOR_BGR2RGB)

    facescurrentframe=face_recognition.face_locations(imgs)
    encodescurrentFrame=face_recognition.face_encodings(imgs,facescurrentframe)

    for encodeFace_faceLoc in zip(encodescurrentFrame,facescurrentframe)
        matches=face_recognition.compare_faces(encodeListKnown,encodeface)
        faceDis=face_recognition.face_distance(encodeListKnown,encodeface)
        print(faceDis)
        matchIndex=np.argain(faceDis)

        if mathes(matchIndex):
            name=classNames[matchIndex].upper()
            print(name)
            y1,x2,y2,x1 = faceLoc
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HEARSHEY_COMPLEX,1,(255,255,255),2)

            markAttendance(name)


    cv2.imshow('webcam',img)
    cv2.waitkey(1)
