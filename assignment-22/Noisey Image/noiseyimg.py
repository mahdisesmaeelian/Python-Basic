from random import randint
import cv2
import numpy as np

img = cv2.imread("chess pieces.jpg" ,0)

row , col = img.shape

for i in range(1000):
    noises = randint(0,255)
    random_x = randint(0,row-1)
    random_y = randint(0,col-1)
    img[random_x,random_y] = noises

cv2.imwrite('Output.jpg',img)
cv2.imshow('Output',img)
cv2.waitKey()