import numpy as np
import cv2

image = cv2.imread('Input.jpg', 0)

image = cv2.resize(image, (410,620))

image[90:120,0:40] = 0
image[60:90,30:70] = 0
image[30:60,60:100] = 0
image[0:30,90:130] = 0

cv2.imshow("Image", image)

cv2.waitKey(0)

cv2.imwrite('Output2.jpg', image)