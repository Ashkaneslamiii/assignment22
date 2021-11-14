import cv2

img_origin = cv2.imread("origin.bmp",0)
img_testing = cv2.imread("testing.bmp",0)
img_testing = img_testing[::,::-1]

substraction = cv2.subtract(img_origin, img_testing)
result = substraction * 10

cv2.imshow('result_board', result)
cv2.imwrite('result_board.jpg', result)

cv2.waitKey()
