import cv2
import numpy as np

list = []
for i in range (15):
    img = cv2.imread(f"h{i}.jpg",0)
    list.append(img)

row , col = img.shape
result = np.zeros((row,col), dtype = "uint8")

for pic in list:
    result += img//16

cv2.imwrite("result.jpg" , result)
cv2.imshow("result", result)
cv2.waitKey()
    
