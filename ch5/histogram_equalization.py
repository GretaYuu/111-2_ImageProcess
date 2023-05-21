# 直方圖等化
import cv2
import numpy as np

img1 = cv2.imread("D:/Documents/ImgProcess/picture/cstu.jpg", -1)
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) # 將彩色圖像轉換為灰度圖像
img2 = cv2.equalizeHist(img1_gray) # 對灰度圖像進行直方圖均衡化
cv2.imwrite("Histogram Equalization.jpg",img2)
cv2.waitKey(0)
