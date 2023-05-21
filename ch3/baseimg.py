import numpy as np
import cv2

img = cv2.imread('D:/Documents/ImgProcess/picture/cstu.jpg')
height, width, channels = img.shape #抓取圖片大小

#色彩空間轉換
#RGB轉換成灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_3c = cv2.merge([gray, gray, gray])

#轉換成二值圖
ret, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
thresh1_3c = cv2.merge([thresh1, thresh1, thresh1])

#RGB轉換成HSV(色相、飽和度、明亮度)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv_gray = cv2.cvtColor(hsv, cv2.COLOR_BGR2GRAY)
hsv_gray_3c = cv2.merge([hsv_gray, hsv_gray, hsv_gray])

#RGB轉換成YUV(色彩和飽和度)
yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
yuv_gray = cv2.cvtColor(yuv, cv2.COLOR_BGR2GRAY)
yuv_gray_3c = cv2.merge([yuv_gray, yuv_gray, yuv_gray])

merged_img = np.hstack((img, gray_3c, thresh1_3c, hsv_gray_3c, yuv_gray_3c))
#cv2.imshow('Merged Image', merged_img)
cv2.imwrite('Merged Image.jpg', merged_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
