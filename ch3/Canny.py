#邊緣偵測
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

#Laplacian
lap = cv2.Laplacian(img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

#Sobel
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)

#Canny
canny = cv2.Canny(img, 30, 150)

cv2.imwrite("Laplacian.jpg", lap)
cv2.imwrite("Sobel.jpg", sobelX)
cv2.imwrite("Canny.jpg", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
