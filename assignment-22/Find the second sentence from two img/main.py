import cv2
import numpy as np

first_img = cv2.imread('a.tif', 0)
second_img = cv2.imread('b.tif', 0)

second_sentence = second_img - first_img 

cv2.imwrite('Output.jpg', second_sentence)
cv2.imshow('Output', second_sentence)
cv2.waitKey()