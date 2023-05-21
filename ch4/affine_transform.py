#使用控制點的仿射轉換
import numpy as np
import cv2

img1 = cv2.imread("D:/Documents/ImgProcess/picture/gm.jpg", -1)
nr,nc=img1.shape[:2]
pts1=np.float32([[160,165],[240,390],[270,125]])  #表示原始圖像中的三個點
pts2=np.float32([[190,140],[190,375],[310,140]])  #表示變換後圖像中的三個點
T=cv2.getAffineTransform(pts1,pts2)
img2=cv2.warpAffine(img1,T,(nc,nr))

cv2.imwrite("gm_Affine Transform.jpg", img2)
cv2.waitKey(0)