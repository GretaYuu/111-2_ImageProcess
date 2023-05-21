#B11056251陳湘宇 CH9作業3
#adaptive_thresholding.py
import numpy as ap
import cv2

img=cv2.imread("D:/Documents/ImgProcess/picture/highway.jpg",0)
thresh,img1=cv2.threshold(img,128,255,cv2.THRESH_BINARY)
img2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,0)
img3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,0)
cv2.imwrite("adaptive_thresholding_(MEAN.5).jpg",img2)
cv2.imwrite("adaptive_thresholding_(GAUSSIAN.5).jpg",img3)
cv2.waitKey(0)

