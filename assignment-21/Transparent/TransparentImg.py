import cv2

img = cv2.imread('4.jpg', 0)
# img = cv2.resize(img, (810,520))

threshold = 110
height, width = img.shape
print(img.shape)

for i in range(height):
    for j in range(width):
        if img[i,j] <= threshold:
            img[i,j] = 0

cv2.imwrite("Output.png", img)
cv2.imshow("Output.png", img)
cv2.waitKey()