#混合拉普拉斯運算子
import cv2
import numpy as np

def composite_laplacian(f):
    kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    temp=cv2.filter2D(f,cv2.CV_32F,kernel)  #对图像进行卷积操作。kernel 则表示卷积核，通常是一个小的二维数组，用于实现图像卷积操作
    g = np.uint8(np.clip(temp, 0, 255)) 
    #g = np.uint8(np.clip(temp, -128, 127) + 128)
    return g

def main():
    img1=cv2.imread( "D:/Documents/ImgProcess/picture/cstu.jpg", -1)
    img2=composite_laplacian(img1)
    cv2.imwrite("composite_laplacian_32F.jpg",img2)
    cv2.waitKey(0)
    
    
main()
