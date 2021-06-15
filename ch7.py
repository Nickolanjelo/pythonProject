import cv2
import numpy as np

def empty(a):
    pass


path = "Resources/lambo.jpg"

cv2.namedWindow("trackbars")
cv2.resizeWindow("trackbars",350,300)
cv2.createTrackbar("hue min","trackbars",0,179,empty)
cv2.createTrackbar("hue max","trackbars",179,179,empty)
cv2.createTrackbar("sat min","trackbars",0,255,empty)
cv2.createTrackbar("sat max","trackbars",255,255,empty)
cv2.createTrackbar("val min","trackbars",0,255,empty)
cv2.createTrackbar("val max","trackbars",255,255,empty)

while True:
     img = cv2.imread(path)
     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
     h_min = cv2.getTrackbarPos("hue min", "trackbars")
     h_max = cv2.getTrackbarPos("hue max", "trackbars")
     s_min = cv2.getTrackbarPos("sat min", "trackbars")
     s_max = cv2.getTrackbarPos("sat max", "trackbars")
     v_min = cv2.getTrackbarPos("val min", "trackbars")
     v_max = cv2.getTrackbarPos("val max", "trackbars")
     print(h_min,h_max,s_min,s_max,v_min,v_max)

     lower = np.array([h_min,s_min,v_min])
     upper = np.array([h_max,s_max,v_max])
     mask = cv2.inRange(imgHSV,lower,upper)
     imgResult = cv2.bitwise_and(img,img,mask=mask)


     cv2.imshow("or",img)
     cv2.imshow("orig",imgHSV)
     cv2.imshow("mask",imgResult)
     cv2.waitKey(1)