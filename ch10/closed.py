"""
cv2.morphologyEx(src,      # 輸入圖片
                 op,       # 需要處理類型的函數：(cv2.MORPH_OPEN,cv2.MORPH_CLOSE,cv2.MORPH_GRADIENT)
                 kernel,   # 卷積核大小
                 dst=None, 
                 anchor=None, 
                 iterations=None,     #迭代次數，默認1次
                 borderType=None, 
                 borderValue=None)
"""
#B11056251陳湘宇_習題1(d)
import cv2
import numpy as np
original_img = cv2.imread('D:/Documents/ImgProcess/picture/flower.jpg',0)
gray_res = cv2.resize(original_img,None,fx=0.8,fy=0.8,
                 interpolation = cv2.INTER_CUBIC)                #圖形太大了縮小一點
# B, G, img = cv2.split(res)
# _,RedThresh = cv2.threshold(img,160,255,cv2.THRESH_BINARY)     #設定紅色通道閾值160（閾值影響開閉運算效果）
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))         #定義矩形結構元素

closed1 = cv2.morphologyEx(gray_res, cv2.MORPH_CLOSE, kernel,iterations=1)    #閉運算1
closed2 = cv2.morphologyEx(gray_res, cv2.MORPH_CLOSE, kernel,iterations=3)    #閉運算2

cv2.imwrite("Close1.jpg",closed1)
cv2.imwrite("Close2.jpg",closed2)
cv2.waitKey(0)