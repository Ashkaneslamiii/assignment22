import cv2
import numpy as np 


image = cv2.imread("final.jpg", 0)
res = np.zeros((400,400), dtype = "uint8")

list = []
for i in range(200):
    noises  = np.random.randint(0,400)
    list.append(noises)

res = image
for i in list:
    res[i,np.random.randint(0,400)] = 255

cv2.imwrite("Result.jpg" , res)
cv2.imshow("Output", res )
cv2.waitKey()
