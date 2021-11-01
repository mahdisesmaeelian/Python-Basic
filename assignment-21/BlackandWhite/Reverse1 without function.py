import cv2

image = cv2.imread('1.jpg', 0)

image[: :] = 255 - image [: :]

cv2.imshow("Image", image)

cv2.waitKey(0)

cv2.imwrite('Output1.jpg', image)