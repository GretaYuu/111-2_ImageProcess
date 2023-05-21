# 影像旋轉
import numpy as np
import cv2

img1 = cv2.imread("D:/Documents/ImgProcess/picture/gm.jpg", -1)
nr, nc = img1.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((nc/2, nr/2), 45, 1)
#逆時針旋轉45度 nc、nr除以2是為了取得影像中心座標。最後的參數1是縮放比例，代表保持原始大小
img2 = cv2.warpAffine(img1, rotation_matrix, (nc, nr))

cv2.imwrite("gm_Image Rotation.jpg", img2)
cv2.waitKey(0)
