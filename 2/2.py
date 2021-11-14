from typing import final
import cv2
import numpy as np

list1 =[]
for i in range(1,6):
    img = cv2.imread(f"1/{i}.jpg",0)
    list1.append(img)
    row , col = img.shape
result1 = np.zeros((row,col),dtype="uint8")

for pic in list1:
    result1 += pic//5



list2 =[]
for i in range(1,6):
    img = cv2.imread(f"2/{i}.jpg",0)
    list2.append(img)
result2 = np.zeros((row,col),dtype="uint8")

for pic in list2:
    result2 += pic//5



list3 = []
for i in range(1,6):
    img = cv2.imread(f"3/{i}.jpg",0)
    list3.append(img)
result3 = np.zeros((row,col),dtype= "uint8")
for pic in list3:
    result3 += pic//5



list4 =[]
for i in range(1,6):
    img = cv2.imread(f"4/{i}.jpg",0)
    list4.append(img)
result4 = np.zeros((row,col),dtype="uint8")
for pic in list4:
    result4 += pic//5

result1 = cv2.resize(result1,(200,200))
result2 = cv2.resize(result2,(200,200))
result3 = cv2.resize(result3,(200,200))
result4 = cv2.resize(result4,(200,200))

result__1 = np.concatenate((result1,result2),axis=1)
result__2= np.concatenate((result3,result4),axis=1)
final = np.concatenate((result__1, result__2),axis=0)

cv2.imshow("Final",final)
cv2.imwrite("Final.jpg", final)
cv2.waitKey()