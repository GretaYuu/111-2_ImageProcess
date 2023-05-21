#B11056251陳湘宇 CH9作業4-roberts
import cv2 as cv
import numpy as np
from scipy import signal
def roberts(img, boundary='fill', fillvalue=0):
    h, w = img.shape[:2]
    h_k, w_k = 2, 2
    # 卷積核1及錨點的位置
    r1 = np.array([[1,0],[0,-1]], np.float32)
    kr1, kc1 = 0, 0
    # 計算full卷積
    img_conv_r1 = signal.convolve2d(img, r1, mode='full', boundary=boundary, fillvalue=fillvalue)
    # 根據錨點的位置截取 full 卷積，獲得 same 卷積
    img_conv_r1 = img_conv_r1[h_k-kr1-1:h+h_k-kr1-1, w_k-kc1-1:w+w_k-kc1-1]
    # 卷積核2及錨點的位置
    r2 = np.array([[0, 1], [-1, 0]], np.float32)
    kr2, kc2 = 0, 1
    # 計算full卷積
    img_conv_r2 = signal.convolve2d(img, r2, mode='full', boundary=boundary, fillvalue=fillvalue)
    # 根據錨點的位置截取 full 卷積，獲得 same 卷積
    img_conv_r2 = img_conv_r2[h_k - kr2 - 1:h + h_k - kr2 - 1, w_k - kc2 - 1:w + w_k - kc2 - 1]
    return img_conv_r1, img_conv_r2

if __name__ == '__main__':
    img = cv.imread("D:/Documents/ImgProcess/picture/highway.jpg", 0)  # 修改圖片路徑
    img_conv_r1, img_conv_r2 = roberts(img)
    img_conv_r1 = np.abs(img_conv_r1) # 45 方向上的邊緣強度的灰度級顯示
    edge_45 = img_conv_r1.astype(np.uint8)
    cv.imwrite('edge_45.jpg', edge_45)
    img_conv_r2 = np.abs(img_conv_r2)  # 135 方向上的邊緣強度
    edge_135 = img_conv_r2.astype(np.uint8)
    cv.imwrite('edge_135.jpg', edge_135)
    edge = np.sqrt(np.power(img_conv_r1, 2.0) + np.power(img_conv_r2, 2.0)) # 用平方和的開方來衡量最後輸出的邊緣
    edge = np.round(edge)
    edge[edge>255] = 255
    edge = edge.astype(np.uint8)
    cv.imwrite('edge.jpg', edge) # 顯示邊緣
    cv.waitKey(0)
    cv.destroyAllWindows()
