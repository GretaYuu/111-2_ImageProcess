#Beta矯正
import numpy as np
import cv2
import scipy.special as special

def beta_correction(f,a=2.0,b=2.0):
    g=f.copy()
    nr,nc=f.shape[:2]
    x=np.linspace(0,1,256)
    table=np.round(special.betainc(a,b,x)*255,0)
    if f.ndim !=3:
        for x in range(nr):
            for y in range(nc):
                g[x,y]=table[f[x,y]]
    else:
        for x in range(nr):
            for y in range(nc):
                for k in range(3):
                    g[x,y,k]=table[f[x,y,k]]
    return g 

def main():
    img=cv2.imread("D:/Documents/ImgProcess/picture/cstu.jpg",0)
    img1=beta_correction(img,a=0.5,b=0.5)
    img2=beta_correction(img,a=2.0,b=2.0)
    cv2.imwrite("Beta(a=b=0.5).jpg",img1)
    cv2.imwrite("Beta(a=b=2.0).jpg",img2)
    cv2.waitKey(0)
    
main()