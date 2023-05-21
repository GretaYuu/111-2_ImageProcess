#B11056251陳湘宇CH9作業4-sobel
import math
import cv2 as cv
import numpy as np
from scipy import signal


def pascal_smooth(n):
  	# 返回 n 階的非歸一化的高斯平滑運算元
    pascal_smooth = np.zeros([1, n], np.float32)
    for i in range(n):
        pascal_smooth[0][i] = math.factorial(n-1) / (math.factorial(i) * math.factorial(n-1-i))
    return pascal_smooth

def pascal_diff(n):
  	# 返回 n 階的差分運算元
    pascal_diff = np.zeros([1, n], np.float32)
    pascal_smooth_previous = pascal_smooth(n-1)
    for i in range(n):
        if i == 0:
            # 恒等於 1
            pascal_diff[0][i] = pascal_smooth_previous[0][i]
        elif i == n-1:
            # 恒等於 -1
            pascal_diff[0][i] = - pascal_smooth_previous[0][i-1]
        else:
            pascal_diff[0][i] = pascal_smooth_previous[0][i] - pascal_smooth_previous[0][i-1]
    return pascal_diff


def get_sobel_kernel(n):
    pascal_smooth_kernel = pascal_smooth(n)
    pascal_diff_kernel = pascal_diff(n)
    # 水準方向的卷積核
    sobel_kerenl_x = signal.convolve2d(pascal_smooth_kernel.transpose(), pascal_diff_kernel, mode='full')
    # 垂直方向的卷積核
    sobel_kerenl_y = signal.convolve2d(pascal_smooth_kernel, pascal_diff_kernel.transpose(), mode='full')
    return sobel_kerenl_x, sobel_kerenl_y

def sobel(img, n):
    rows, cols = img.shape[:2]
    # 平滑運算元
    pascal_smooth_kernel = pascal_smooth(n)
    # 差分運算元
    pascal_diff_kernel = pascal_diff(n)
    # 水準方向上的 sobel 核卷積
    # 先進行垂直方向的平滑
    img_sobel_x = signal.convolve2d(img, pascal_smooth_kernel.transpose(), mode='same')
    # 再進行水準方向上的差分
    img_sobel_x = signal.convolve2d(img_sobel_x, pascal_diff_kernel, mode='same')
    # 垂直方向上的 sobel 核卷積
    img_sobel_y = signal.convolve2d(img, pascal_smooth_kernel, mode='same')
    img_sobel_y = signal.convolve2d(img_sobel_y, pascal_diff_kernel.transpose(), mode='same')

    return img_sobel_x, img_sobel_y


if __name__ == '__main__':
    img = cv.imread('D:/Documents/ImgProcess/picture/highway.jpg', 0)
    img_sobel_x, img_sobel_y = sobel(img, 3)

    img_sobel_x_c, img_sobel_y_c = img_sobel_x.copy(), img_sobel_y.copy()
    img_sobel_x_c, img_sobel_y_c = abs(img_sobel_x_c), abs(img_sobel_y_c)
    img_sobel_x_c[img_sobel_x_c>255] = 255
    img_sobel_y_c[img_sobel_y_c>255] = 255
    img_sobel_x_c = img_sobel_x_c.astype(np.uint8)
    img_sobel_y_c = img_sobel_y_c.astype(np.uint8)
    cv.imwrite('sobel x.jpg', img_sobel_x_c)
    cv.imwrite('sobel y.jpg', img_sobel_y_c)
    # 平方和開方的方式
    edge = np.sqrt(np.power(img_sobel_x, 2.0) + np.power(img_sobel_y, 2.0))

    # 直接截斷顯示
    edge_c = edge.copy()
    edge_c[edge_c > 255] = 255
    edge_c = edge_c.astype(np.uint8)
    cv.imwrite('sobel edge 1.jpg', edge_c)
    # 歸一化後顯示，邊緣強度的灰度級顯示
    edge = edge/np.max(edge)
    edge = np.power(edge, 1)
    edge *= 255
    edge = edge.astype(np.uint8)
    cv.imwrite('sobel edge 2.jpg', edge)

    cv.waitKey(0)
    cv.destroyAllWindows()
