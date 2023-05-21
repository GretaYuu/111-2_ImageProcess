#影像翻轉
import numpy as np
import cv2

img = cv2.imread("D:/Documents/ImgProcess/picture/gm.jpg", -1)

# 0 表示垂直翻轉（即s上下翻轉），1 表示水平翻轉（即左右翻轉）
img1=cv2.flip(img,0)
img2=cv2.flip(img,1)

cv2.imwrite("gm_Flip Vertically.jpg", img1)
cv2.imwrite("gm_Flip Horizontally.jpg", img2)
cv2.waitKey(0)