import numpy as np 
import cv2

# 读取一张图像
img = cv2.imread("lenna.bmp",-1)

# 显示图像
cv2.imshow("lenna_full.jpg", img)

# 等待用户按下任意按键
cv2.waitKey(0)

# 关闭窗口
cv2.destroyAllWindows()

