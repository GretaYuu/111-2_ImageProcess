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

img = cv2.imread('D:/Documents/ImgProcess/picture/cstu.jpg')
img = cv2.resize(img,(700,500),cv2.INTER_AREA)

# 亮度調整
M = np.ones(img.shape, dtype="uint8") * 100
added = cv2.add(img, M)
subtracted = cv2.subtract(img, M)
l = np.hstack((added, subtracted))

# 對比度調整
N = np.ones(img.shape, dtype="uint8") * 4
mult = cv2.multiply(img, N)
div = cv2.divide(img, N)
c = np.hstack((mult, div))

#儲存圖檔
cv2.imwrite("test2_cs2.jpg", np.hstack((l, c)))
cv2.waitKey(0)
cv2.destroyAllWindows()