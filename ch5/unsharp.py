# 非銳化遮罩
import cv2
import numpy as np

def unsharp_masking(f, k=1.0):
    g = f.copy()
    nr, nc = f.shape[:2]
    f_avg = cv2.GaussianBlur(f, (15, 15), 0)
    for x in range(nr):
        for y in range(nc):
            #g_mask = int(f[x, y]) - int(f_avg[x, y])   
            #TypeError: only size-1 arrays can be converted to Python scalars
            g_mask = np.uint8(f[x, y]) - np.uint8(f_avg[x, y])
            g[x, y] = np.uint8(np.clip(f[x, y] + k * g_mask, 0, 255))
    return g


def main():
    img1 = cv2.imread("D:/Documents/ImgProcess/picture/cstu.jpg", -1)
    img2 = unsharp_masking(img1, 10.0)  
    cv2.imwrite("unsharp_masking(10.0).jpg", img2)
    cv2.waitKey(0)

main()
