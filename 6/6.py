import cv2

img = cv2.imread("her.jpg",0)

inverted_img = 255 - img 
blured_inverted_img = cv2.GaussianBlur(inverted_img , (31,31), 0)
inverted_blured_inverted_img = 255 - blured_inverted_img

sketch = img / inverted_blured_inverted_img
sketch = sketch * 255


cv2.imwrite("herr.jpg", sketch)
cv2.imshow("result.jpg", sketch)
cv2.waitKey()

