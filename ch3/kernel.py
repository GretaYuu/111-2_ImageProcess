#匯入套件
import numpy as np
import cv2

#讀取圖片
img = cv2.imread(r'D:/Documents/ImgProcess/nj.jpg') 

#抓取圖片大小
height, width, channels = img.shape

#卷積運算銳化
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32) 
dst = cv2.filter2D(img, -1, kernel)

#多張圖一起顯示
hstack = np.hstack((img, dst))

#顯示圖片
cv2.imshow('image', hstack)

#儲存圖片
cv2.imwrite('kernel.jpg', dst)

#等待使用者按下任意鍵後關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()