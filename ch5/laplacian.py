#影像銳化(強化影像的邊緣資訊)
#拉普拉斯
import cv2
import numpy as np

def laplacian(f):
    #cv2.CV_32F:將圖像數據類型轉換為 32 位浮點數格式。在進行圖像處理運算時，使用浮點數格式可以提高運算的精度和準確性
    #將圖像f轉換為浮點數格式（使用cv2.CV_32F參數）進行處理，並加上128，最後將結果存儲在變量temp中
    temp=cv2.Laplacian(f,cv2.CV_32F)+128  
    #temp = cv2.Laplacian(f, cv2.CV_16S) + 128
    #使用numpy庫中的unit8函數將temp轉換為無符號8位整數格式（範圍為0-255），並使用clip函數將像素值限制在0和255之間，將結果存儲在變量g中
    g = np.uint8(np.clip(temp, 0, 255)) 
    #g = np.uint8(np.clip(temp, -128, 127) + 128)
    return g


def main():
    img1=cv2.imread( "D:/Documents/ImgProcess/picture/cstu.jpg", -1)
    img2=laplacian(img1)
    cv2.imwrite("laplacian_32F.jpg",img2)
    cv2.waitKey(0)
    
    
main()

