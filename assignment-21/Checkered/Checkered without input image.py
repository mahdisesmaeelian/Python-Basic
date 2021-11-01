import numpy as np
import cv2

img = np.zeros((800, 800), dtype = "uint8")

blacksquare = img[0:100, 0:100] = 255

for i in range(0, 800, 200):
    for j in range(0, 800, 200):
        img[i:i+100, j:j+100] = blacksquare

for i in range(100, 800, 200):
    for j in range(100, 800, 200):
        img[i:i+100, j:j+100] = blacksquare

cv2.imwrite('Output.jpg', img)

cv2.imshow('photo', img)
cv2.waitKey()
