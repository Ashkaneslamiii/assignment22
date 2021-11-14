import cv2
import numpy as np

img1 = cv2.imread('a.tif',0)
img2 = cv2.imread('b.tif',0)

result = img2 - img1

cv2.imwrite('result.jpg', result)
cv2.imshow('result', result)
cv2.waitKey()
