# 平均濾波
import cv2
import numpy as np

img1 = cv2.imread("D:/Documents/ImgProcess/picture/cstu.jpg", -1)
img2 = cv2.blur(img1,(2,2))#(5, 5) 表示卷積核的大小為 5x5，所以平均濾波是對圖像中每個像素周圍 5x5 的區域取平均值，然後將這個平均值作為該像素的值，這樣可以平滑圖像，減少噪聲的影響
cv2.imwrite("Average Filtering(2,2).jpg",img2)
cv2.waitKey(0)