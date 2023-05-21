"""
膨脹
cv2.dilate(src,                    # 輸入圖像
           kernel,                 # 卷積核
           dst=None, 
           anchor=None, 
           iterations=None,        # 迭代次數，默認1
           borderType=None, 
           borderValue=None)
"""
#B11056251陳湘宇_習題1(b)
import cv2
import numpy as np
original_img = cv2.imread('D:/Documents/ImgProcess/picture/flower.jpg')
res = cv2.resize(original_img,None,fx=0.6, fy=0.6,
                 interpolation = cv2.INTER_CUBIC) #圖形太大了縮小一點
B, G, R = cv2.split(res)                    #獲取紅色通道
img = R
_,RedThresh = cv2.threshold(img,160,255,cv2.THRESH_BINARY)
#OpenCV定義的結構矩形元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
dilated = cv2.dilate(RedThresh,kernel)      #膨脹圖像
cv2.imwrite("Dilated Image.png",dilated)    #顯示膨脹後的圖像

cv2.waitKey(0)