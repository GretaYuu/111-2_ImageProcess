#B11056251陳湘宇 CH9作業2
#Canny_edge_detection.py
import numpy as ap
import cv2

img1=cv2.imread( "D:/Documents/ImgProcess/picture/highway.jpg", -1)
img2=cv2.Canny( img1,100,200)
cv2.imwrite("Canny_edge_detection_highway_100.jpg",img2)
cv2.waitKey(0)