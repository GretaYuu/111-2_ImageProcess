#高斯濾波
import cv2
import numpy as np

img1 = cv2.imread("D:/Documents/ImgProcess/picture/cstu.jpg", -1)
img2 = cv2.GaussianBlur(img1,(9,9),0)
cv2.imwrite("Gaussian Filtering(9,9).jpg",img2)
cv2.waitKey(0)