import cv2

image = cv2.imread('Input.jpg', 0)

image = cv2.resize(image, (410,620))

cv2.line(image, (140,-10), (-10,140), (0), 25)
 
cv2.imshow("Image", image)

cv2.waitKey(0)

cv2.imwrite('Output.jpg', image)