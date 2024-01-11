import cv2
import numpy as np

choice= input("Enter colour: ").lower()

if choice=='green':
    #green
    low= np.array([54,65,40])
    high= np.array([95,255,255])

elif choice=='red':
    #red
    low= np.array([167,77,57])
    high= np.array([180,255,255])

elif choice=='yellow':
    #yellow
    low= np.array([14,94,63])
    high= np.array([38,255,255])

elif choice=='violet':
    #violet
    low= np.array([121,77,56])
    high= np.array([140,255,255])

elif choice=='brown':
    #brown
    low= np.array([7,114,80])
    high= np.array([16,255,255])

elif choice=='orange':
    #orange
    low= np.array([6,170,120])
    high= np.array([20,255,255])

cap= cv2.VideoCapture(0)

while True:
    ret,frame= cap.read()
    cv2.imshow('Original Frame',frame)

    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    mask= cv2.inRange(hsv,low,high)
    color= cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('Masked Frame',color)

    if cv2.waitKey(1)== ord('e'):
        break

cap.release()
cv2.destroyAllWindows()