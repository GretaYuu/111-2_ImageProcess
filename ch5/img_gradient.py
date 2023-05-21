#影像梯度
import cv2
import numpy as np

def Sobel_gradient(f,direction=1):
    sobel_x=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    sobel_y=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    if direction ==1:
        grad_x=cv2.filter2D(f,cv2.CV_32F,sobel_x)
        gx = np.abs(grad_x)
        g = np.uint8(np.clip(gx, 0, 255))
    elif direction == 2:
        grad_y = cv2.filter2D(f,cv2.CV_32F, sobel_y)
        gy = np.abs(grad_y)
        g = np.uint8( np.clip( gy, 0, 255 ))
    else:
        grad_x = cv2.filter2D(f,cv2.CV_32F,sobel_x)
        grad_y = cv2.filter2D(f,cv2.CV_32F,sobel_y)
        magnitude = np.abs(grad_x)+ np.abs(grad_y)
        g = np.uint8( np.clip(magnitude, 0, 255))
    return g

def main():
    img = cv2.imread( "D:/Documents/ImgProcess/picture/cstu.jpg", -1)
    gx =Sobel_gradient(img,1) 
    gy =Sobel_gradient(img,2)
    g = Sobel_gradient(img,3) 
    cv2.imwrite( "Gradient in x.jpg", gx) 
    cv2.imwrite( "Gradient in y.jpg", gy) 
    cv2.imwrite( "Gradient.jpg", g ) 
    cv2.waitKey(0)
        
main()
