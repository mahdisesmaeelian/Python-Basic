import cv2
import numpy as np

img1 = cv2.imread("1.jpg" ,0)
img2 = cv2.imread("2.jpg" ,0)

img1= cv2.resize(img1 ,(500,580))
img2= cv2.resize(img2 ,(500,580))

result1 =  img2//4 + img1//2 
result2 = img1//4 + img2//2

cv2.imwrite('Output1.jpg',result1)
cv2.imwrite('Output2.jpg',result2)

result = np.zeros((580,2000), dtype ="uint8")
result[0:580,0:500]= img1
result[0:580,500:1000] = result1
result[0:580,1000:1500]= result2
result[0:580,1500:2000] = img2

cv2.imwrite('Output.jpg',result)
cv2.imshow('Output',result)

cv2.waitKey()