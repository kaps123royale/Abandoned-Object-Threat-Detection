import cv2
import numpy as np
cap=cv2.VideoCapture("video1.avi")
_,firstframe=cap.read()
firstgray=cv2.cvtColor(firstframe,cv2.COLOR_BGR2GRAY)
firstgray=cv2.GaussianBlur(firstgray,(5,5),0)
while True:
    _,frame = cap.read()
    grayframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    grayframe=cv2.GaussianBlur(grayframe,(5,5),0)
    diff=cv2.absdiff(firstgray,grayframe)
    cv2.imshow('First frame',firstframe)
    cv2.imshow('frame',frame)
    cv2.imshow('Difference',diff)

    if cv2.waitKey(30) & 0xFF==ord('q'):

        break

cap.release()
cv2.destroyALLWindows()
