import cv2
import numpy as np

result = np.zeros((240, 320), dtype ="uint8")

for i in range(15):
    image = cv2.imread(f"img/h{i}.jpg",0)
    result += image//15

cv2.imwrite('Output.jpg',result)
cv2.imshow('Output',result)
cv2.waitKey()