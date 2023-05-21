#影像負片
import numpy as np
import cv2

def image_negative(f):
    g=255-f
    return g

def main():
    img1=cv2.imread("D:/Documents/ImgProcess/picture/lenna_full.jpg",-1) 
    # 0，以灰度模式讀取圖像。也就是說，圖像將被讀取為灰度圖像，即只有一個通道，像素值的範圍從0到255
    # 1，以彩色模式讀取圖像，這樣圖像將包含3個通道，即紅色、綠色和藍色通道
    #-1，表示讀取帶有透明度通道的圖像，即ARGB格式
    img2=image_negative(img1)
    cv2.imwrite("ch5_image negative_-1.jpg",img2)
    cv2.waitKey(0)
    
main()
