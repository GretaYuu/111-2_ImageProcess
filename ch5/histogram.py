import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram(f):
    # 計算直方圖
    if f.ndim != 3:
        #cv2.calcHist(影像, 通道, 遮罩, 區間數量, 數值範圍)
        hist = cv2.calcHist([f], [0], None, [256], [0, 256])  
        plt.plot(hist)
    else:
        color = ('b','g','r')
        for i, col in enumerate(color):  #col 是定義的一個包含三個元素的元組，分別代表紅色、綠色和藍色
        #在每次迭代中，使用 cv2.calcHist() 函數計算圖像在當前通道的直方圖
            hist = cv2.calcHist([f], [i], None, [256], [0, 256])
            plt.plot(hist, color=col)  # plt.plot() 函數將該直方圖畫出，顏色為當前通道的顏色
        plt.xlim([0, 256])
        #設定 x 軸和 y 軸的標籤 (label) 
        plt.xlabel("Intensity")  # x 軸代表的是亮度值
        plt.ylabel("#Intensities")  #y 軸代表的是該亮度值在圖像中出現的頻率

def main():
    img = cv2.imread("D:/Documents/ImgProcess/picture/cstu.jpg", -1)
    cv2.imshow("Original", img)
    histogram(img)  #使用 histogram() 函數計算並繪製該圖片的直方圖
    plt.savefig("histogram.jpg")
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
