import cv2

image = cv2.imread('2.jpg', 0)

image = cv2.resize(image, (450,620))

image = cv2.bitwise_not(image)

cv2.imshow("Image", image)

cv2.waitKey(0)

cv2.imwrite('Output2.jpg', image)