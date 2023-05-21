import numpy as np 
import cv2

def saltpepper(img, n):
    m = int((img.shape[0] * img.shape[1]) * n)
    for a in range(m):
        i = int(np.random.random() * img.shape[1]) 
        j = int(np.random.random() * img.shape[0])
        if img.ndim == 2:
            img[j, i] = 255 
        elif img.ndim == 3:
            img[j, i, 0] = 255
            img[j, i, 1] = 255
            img[j, i, 2] = 255
    for b in range(m):
        i = int(np.random.random() * img.shape[1])
        j = int(np.random.random() * img.shape[0])
        if img.ndim == 2: 
            img[j, i] = 0 
        elif img.ndim == 3:
            img[j, i, 0] = 0
            img[j, i, 1] = 0
            img[j, i, 2] = 0
    return img

img = cv2.imread('D:/Documents/ImgProcess/nj.jpg')
img = cv2.resize(img,(700,500),cv2.INTER_AREA)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
salt = saltpepper(img, 0.02)
med = cv2.medianBlur(salt, 5) # 中值
aug = cv2.blur(salt, (5, 5)) # 均值
gas = cv2.GaussianBlur(salt, (5, 5), 0) # 高斯
bil = cv2.bilateralFilter(salt, 9, 75, 75) # 雙邊
a = np.hstack((med, aug))
b = np.hstack((gas, bil))
v = np.vstack((a, b))

#儲存圖檔
cv2.imwrite("test.jpg", v)
cv2.waitKey(0)
cv2.destroyAllWindows()
