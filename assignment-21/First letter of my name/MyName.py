import numpy as np
import cv2

img = np.zeros((600, 600), dtype = "uint8")
img [:,:] = 255

img[200:400,170:210] = 0
img[200:400,380:420] = 0

img[200:290,190:240]= 0
img[200:290,350:400]= 0

img[240:320,230:280]= 0
img[240:320,310:360]= 0

img[280:350,270:320]= 0


cv2.imwrite('Output.jpg', img)

cv2.imshow('photo', img)
cv2.waitKey()