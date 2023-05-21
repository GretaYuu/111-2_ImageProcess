#影像縮放
import numpy as np
import cv2
img1=cv2.imread("D:/Documents/ImgProcess/picture/gm.jpg",-1) 
#-1 參數表示讀取原始圖像

nr,nc=img1.shape[:2] 
#nr 設置為圖像的高度，nc 設置為圖像的寬度。取圖像尺寸信息的高度及寬度 
scale=eval(input("Please enter scale:"))
nr2 = int(nr * scale)
nc2 = int(nc * scale)
img2=cv2.resize(img1,(nr2,nc2),interpolation=cv2.INTER_LINEAR) 
#INTER_LINEAR:雙線性插值法，在縮放時平滑圖像，減少鋸齒狀邊緣的出現。
cv2.imwrite("gm_Original Image.jpg",img1)
cv2.imwrite("gm_Image Scaling.jpg",img2)
cv2.waitKey(0)