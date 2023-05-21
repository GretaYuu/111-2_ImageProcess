#B11056251陳湘宇_習題3
import numpy as np
import cv2

img1=cv2.imread("D:/Documents/ImgProcess/picture/dt.png",0)
dist=cv2.distanceTransform(img1,cv2.DIST_C,0)
cv2.normalize(dist,dist,0,255,cv2.NORM_MINMAX)
img2=np.uint8(dist)
cv2.imwrite("Distance Transform_C_0.png",img2)
cv2.waitKey(0)