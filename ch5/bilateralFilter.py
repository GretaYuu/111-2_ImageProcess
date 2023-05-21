#雙邊濾波
import cv2
import numpy as np

img1 = cv2.imread("D:/Documents/ImgProcess/picture/face.jpg", -1)
img2 = cv2.bilateralFilter(img1,5,100,100)  
cv2.imwrite("bilateralFilter(5,100,100).jpg", img2)
cv2.waitKey(0)
