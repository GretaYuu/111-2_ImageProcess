# B11056251陳湘宇CH9作業4-kirsch
import cv2
import numpy as np

# 定義Kirsch 卷積範本
kirsch_kernel = np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]])

# 讀入灰階影像
img = cv2.imread('D:/Documents/ImgProcess/picture/grayLenna.png', 0)

# 周圍填充一圈
img = cv2.copyMakeBorder(img, 1, 1, 1, 1, borderType=cv2.BORDER_REPLICATE)

# 新建一個和原圖大小相同的矩陣
img1 = np.zeros(img.shape, dtype=np.uint8)

# 使用 Kirsch 卷積範本進行運算
for i in range(1, img.shape[0] - 1):
    for j in range(1, img.shape[1] - 1):
        temp = np.abs((np.dot(np.array([1, 1, 1]), (kirsch_kernel * img[i - 1:i + 2, j - 1:j + 2]))).sum())
        img1[i, j] = temp
        if img1[i, j] > 255:
            img1[i, j] = 255

# 顯示輸出影像
cv2.imshow("output", img1)

# 存儲處理後的影像
cv2.imwrite("kirsch.jpg",img1)

# 等待按鍵輸入
cv2.waitKey(0)
