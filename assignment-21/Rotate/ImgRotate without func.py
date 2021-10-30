import cv2

img = cv2.imread('Input.jpg', 0)

img = cv2.resize(img, (960,530))

img_rotate_180 = img[::-1,::-1]

cv2.imwrite('Output.jpg',  img_rotate_180)

cv2.imshow('Reverse photo',  img_rotate_180)
cv2.waitKey()