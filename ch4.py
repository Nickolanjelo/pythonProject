import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#img[200:300,100:300]=255,150,0

cv2.circle(img,(200,50),50,(0,255,0),5)
cv2.putText(img,"OPENCV",(100,100),cv2.FONT_HERSHEY_COMPLEX,5,(0,100,0))


cv2.imshow('image',img)
cv2.waitKey(0)