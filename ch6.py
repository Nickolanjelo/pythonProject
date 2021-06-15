import cv2
import numpy as np

img = cv2.imread("Resources/lena.jpg")
#somefunction..
#imgHor = np.hstack((img,img))
#imgVer = np.vstack((img,img))

#cv2.imshow("hor",imgHor)
#cv2.imshow("ver",imgVer)

imgStack = stackImages(0.5,([img,img,img]))
cv2.imshow("imgstack",imgStack)


cv2.waitKey(0)


