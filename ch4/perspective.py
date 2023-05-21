#透視轉換
import numpy as np
import cv2

img1 = cv2.imread("D:/Documents/ImgProcess/picture/gm.jpg", -1)
nr,nc=img1.shape[:2]
#pts1和pts2分別代表原始圖像和變換後圖像中的四個對應點。它返回一個3x3的變換矩陣T
pts1=np.float32([[790,350],[795,690],[1090,720],[1090,250]])  
pts2=np.float32([[0,0],[0,500],[650,500],[650,0]])  

T=cv2.getPerspectiveTransform(pts1,pts2)  #用於計算從一個四邊形到另一個四邊形的透視變換矩陣
img2=cv2.warpPerspective(img1,T,(650,500))  #T是透視變換矩陣，(650,500)是目標圖像的大小

cv2.imwrite("gm_Perspective Transform.jpg", img2)
cv2.waitKey(0)