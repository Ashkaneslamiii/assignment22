from typing import final
import cv2
import numpy as np

himm = cv2.imread("himm.jpg", 0)
himm = cv2.resize(himm,(200,200))
him = cv2.imread("him.jpg", 0)
him = cv2.resize(him,(200,200))


result1 = np.zeros((200,200), dtype = "uint8")
result2 = np.zeros((200,200), dtype = "uint8")
for i in range(200):
    for j in range(200):
        result1[i][j] = 2*himm[i][j]/3 + him [i][j]/3
        result2[i][j] = himm[i][j]/3 + 2*him [i][j]/3



final_pic = np.concatenate((himm,result1,result2,him), axis= 1)

cv2.imwrite("result.jpg",final_pic)
cv2.imshow("result",final_pic)
cv2.waitKey()

