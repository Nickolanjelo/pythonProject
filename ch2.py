import cv2
import numpy as np

img = cv2.imread("Resources/lambo.jpg")
print(img.shape)

imgResize = cv2.resize(img,(500,300))

imgCropped = img[0:300,0:200]

cv2.imshow("image",imgResize)
cv2.imshow("imageCr",imgCropped)


cv2.waitKey(0)
