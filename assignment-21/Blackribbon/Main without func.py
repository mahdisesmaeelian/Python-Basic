import numpy as np
import cv2

image = cv2.imread('Input.jpg', 0)

image = cv2.resize(image, (410,620))

for i in range (100):
    image[i:i+40,100-i] = 0

# a tiny regtangle to complete the line:
for i in range (90):
    image[0:i-670,190-i] = 0

cv2.imshow("Image", image)

cv2.waitKey(0)

cv2.imwrite('Output2.jpg', image)