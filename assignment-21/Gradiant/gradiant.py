import numpy as np
import cv2

img = np.zeros((600, 600), dtype = "uint8")

for i in range (0,600):
    img[i , 0:600] = 255 - (i/2.5)

cv2.imwrite('Output.jpg', img)

cv2.imshow('photo', img)
cv2.waitKey()