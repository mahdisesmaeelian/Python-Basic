import cv2
import numpy as np

imagelist = []

for i in range(1,5):
    for j in range(1,6):
        image = cv2.imread(f"img/{i}/{j}.jpg",0)
        imagelist.append(image)
        row,col = image.shape

for i in range(1,5):
    result = np.zeros((row , col), dtype ="uint8")

    for i in range(0,20,5):
        for j in range(i,i+5):
            result += imagelist[i]//5

        cv2.imwrite(f'Output{i}.jpg',result)
        result = np.zeros((row , col), dtype ="uint8")
        
img1 = cv2.imread('Output0.jpg',0)
img1 = cv2.resize(img1, (500,500))
image[0:500, 0:500] = img1

img2 = cv2.imread('Output5.jpg',0)
img2 = cv2.resize(img2, (500,500))
image[0:500, 500:1000] = img2

img3 = cv2.imread('Output15.jpg',0)
img3 = cv2.resize(img3, (500,500))
image[500:1000, 500:1000] = img3

img4 = cv2.imread('Output10.jpg',0)
img4 = cv2.resize(img4, (500,500))
image[500:1000, 0:500] = img4

cv2.imwrite('Output.jpg',image)
cv2.imshow('Output',image)
cv2.waitKey()