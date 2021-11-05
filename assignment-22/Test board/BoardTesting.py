import cv2
import numpy as np

img1 = cv2.imread('board - origin.bmp', 0)
img2 = cv2.imread('board - test.bmp', 0)
img2 = img2[::,::-1]

testres =cv2.absdiff(img1,img2)

cv2.imwrite('Output.jpg', testres)
cv2.imshow('Output', testres)
cv2.waitKey()