#影像縮放
import numpy as np
import cv2

img=cv2.imread("D:/Documents/ImgProcess/picture/gm.jpg",-1)

nr1,nc1=img.shape[:2] 
scale=eval(input("Please enter scale:"))
nr2,nc2 = nr1//3,nc1//3  #//3 表示將 nr1 和 nc1 各自除以3 並向下取整的結果，得到了縮小 1/3 的影像的高度和寬度

img1=cv2.resize(img,(nr2,nc2),interpolation=cv2.INTER_NEAREST) #cv2.INTER_NEAREST：最近鄰插值法。
img1=cv2.resize(img1,(nr1,nc1),interpolation=cv2.INTER_NEAREST) 
img2=cv2.resize(img,(nr2,nc2),interpolation=cv2.INTER_LINEAR) #cv2.INTER_LINEAR：雙線性插值法。
img2=cv2.resize(img1,(nr1,nc1),interpolation=cv2.INTER_NEAREST) 
img3=cv2.resize(img,(nr2,nc2),interpolation=cv2.INTER_CUBIC) #cv2.INTER_CUBIC：雙三次插值法。
img3=cv2.resize(img1,(nr1,nc1),interpolation=cv2.INTER_NEAREST) 

cv2.imwrite("gm_Original Image.jpg",img)
cv2.imwrite("gm_NEAREST Neighbor.jpg",img1)
cv2.imwrite("gm_BILINEAR.jpg ",img2)
cv2.imwrite("gm_BICUBIC.jpg",img3)

cv2.waitKey(0)