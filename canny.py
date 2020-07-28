import numpy as np
import cv2
firstframe_path =r'/Users/KAPIL SHARMA/Desktop/FrameNo0.png'

firstframe = cv2.imread(firstframe_path)
firstframe_gray = cv2.cvtColor(firstframe, cv2.COLOR_BGR2GRAY)
firstframe_blur = cv2.GaussianBlur(firstframe_gray,(21,21),0)

while(1):

    edged = cv2.Canny(firstframe,50,100) #any gradient between 50 and 100 are considered edges
    cv2.imshow('CannyEdgeDet',edged)
    cv2.imshow('firstframe ',firstframe )

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
