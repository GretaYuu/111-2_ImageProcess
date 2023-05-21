# 匯入套件
import numpy as np
import cv2

# 讀取圖片並抓取圖片大小
img = cv2.imread('D:/Documents/ImgProcess/cstu.jpg')
height, width, channels = img.shape

# 展示圖片
cv2.imshow('cstu2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 顯示原圖片大小
resized_img = cv2.resize(img, (width, height), cv2.INTER_AREA)

# 多張圖片水平合併
hstacked_img = np.hstack((img, resized_img))

# 多張圖片垂直合併
vstacked_img = np.vstack((img, resized_img))

# 顯示圖片
cv2.imshow('Original and Resized Image', hstacked_img)
cv2.imshow('Original and Resized Image Vertically', vstacked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


