#B11056251陳湘宇 CH9作業1
#Sobel_edge_detection,選取不同閥值
import numpy as np
import cv2

def Sobel_edge_detection(f_gray):
    grad_x = cv2.Sobel(f_gray, cv2.CV_32F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(f_gray, cv2.CV_32F, 0, 1, ksize=3)
    magnitude = abs(grad_x) + abs(grad_y)
    g = np.uint8(np.clip(magnitude, 0, 255))
    ret, g = cv2.threshold(g,200, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  
    return g

def main():
    img1 = cv2.imread("D:/Documents/ImgProcess/picture/highway.jpg", -1)
    img_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  #將彩色圖片轉為灰色圖片像
    img2 = Sobel_edge_detection(img_gray)
    #cv2.imshow("Original", img1)
    cv2.imwrite(" img_gray.jpg",  img_gray)
    #cv2.imwrite("Sobel_edge_detection_200.jpg", img2)
    cv2.waitKey(0)

main()


