import cv2

img = cv2.imread("Mona_Lisa.jpg" ,0)

inverted = 255 - img
blurred = cv2.GaussianBlur(inverted, (21,21), 0)
inverted_blurrred = 255 - blurred

sketch = img / inverted_blurrred
sketch = sketch * 255

cv2.imwrite('Painting.jpg' , sketch)
cv2.waitKey()