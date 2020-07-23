import cv2
import numpy as np
frameWidth = 700
frameHeight = 500
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)

myColors = [[0,178,109,20,255,255],#Orange
            [101,255,88,157,255,255], #Blue
            [73,178,54,88,255,255]] #green
myColorValues = [[5,114,247],  #BGR
                 [247,5,9],
                 [0,110,16]]
myPoints = [] # [x,y,colorID]

def getContours(img):
    contours,heirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,myColorValues):
    for myp in myPoints:
        cv2.circle(imgResult, (myp[0],myp[1]), 10, myColorValues[myp[2]], cv2.FILLED)
def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        result = cv2.bitwise_and(img, img, mask=mask)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x !=0 and y !=0:
            newPoints.append([x,y,count])
        count+= 1
        #cv2.imshow(str(color[0]),result)
    return newPoints
while True:
    success, img =cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myColorValues)
    if len(newPoints) !=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) !=0:
        drawOnCanvas(myPoints,myColorValues)
    #cv2.imshow("Image",img)
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
