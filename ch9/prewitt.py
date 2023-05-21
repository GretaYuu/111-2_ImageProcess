##B11056251陳湘宇 CH9作業4-prewitt
import cv2 as cv
import numpy as np
from scipy import signal

def prewitt(img, boundary='symm'):
    # 垂直方向上的均值平滑
    ones_y = np.array([[1], [1], [1]], np.float32)
    i_conv_pre_x = signal.convolve2d(img, ones_y, mode='same', boundary=boundary)
    # 水準方向的差分
    diff_x = np.array([[1, 0, -1]], np.float32)
    i_conv_pre_x = signal.convolve2d(i_conv_pre_x, diff_x, mode='same', boundary=boundary)

    # 水準方向上的均值平滑
    ones_x = np.array([[1,1,1]], np.float32)
    i_conv_pre_y = signal.convolve2d(img, ones_x, mode='same', boundary=boundary)
    # 垂直方向的差分
    diff_y = np.array([[1], [0], [-1]], np.float32)
    i_conv_pre_y = signal.convolve2d(i_conv_pre_y, diff_y, mode='same', boundary=boundary)
    return i_conv_pre_x, i_conv_pre_y

if __name__ == '__main__':
    img = cv.imread("D:/Documents/ImgProcess/picture/highway.jpg", 0)
    i_conv_pre_x, i_conv_pre_y = prewitt(img)
    # 取絕對值，分別得到水準方向和垂直方向上的邊緣強度
    abs_i_conv_pre_x = np.abs(i_conv_pre_x)
    abs_i_conv_pre_y = np.abs(i_conv_pre_y)
    # 水準方向和垂直方向上的邊緣強度的灰度級顯示
    edge_x = abs_i_conv_pre_x.copy()
    edge_y = abs_i_conv_pre_y.copy()
    edge_x[edge_x>255] = 255
    edge_y[edge_y>255] = 255
    edge_x = edge_x.astype(np.uint8)
    edge_y = edge_y.astype(np.uint8)
    cv.imwrite('prewitt_edgex.jpg', edge_x)
    cv.imwrite('prewitt_edge_y.jpg', edge_y)
    # 利用 abs_i_conv_pre_x 和 abs_i_conv_pre_y 求最終的邊緣強度
    # 求邊緣強度，此處使用插值法
    edge = 0.5 * abs_i_conv_pre_x + 0.5 * abs_i_conv_pre_y
    edge[edge>255] = 255
    edge = edge.astype(np.uint8)
    cv.imwrite('prewitt_edge.jpg', edge)
    cv.waitKey(0)
    cv.destroyAllWindows()
