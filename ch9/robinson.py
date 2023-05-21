#B11056251陳湘宇CH9作業4-robinson
import cv2
import numpy as np

def robinson(img, boundary='symm'):
    # Robinson 8方向
    kernel_list = [
        np.array([[-1,0,1],[-2,0,2],[-1,0,1]], np.float32),  # 水準方向
        np.array([[-2,-1,0],[-1,0,1],[0,1,2]], np.float32),  # 45度方向
        np.array([[-1,-2,-1],[0,0,0],[1,2,1]], np.float32),  # 垂直方向
        np.array([[0,-1,0],[1,0,-1],[0,1,0]], np.float32),  # 135度方向
        np.array([[1,1,1],[0,0,0],[-1,-1,-1]], np.float32),  # 水準方向
        np.array([[1,0,-1],[1,0,-1],[1,0,-1]], np.float32),  # 垂直方向
        np.array([[0,-1,-2],[1,0,-1],[2,1,0]], np.float32),  # 45度方向
        np.array([[-1,-2,-1],[1,0,-1],[0,1,0]], np.float32),  # 135度方向
    ]

    # 對每個方向進行卷積，並取絕對值，然後相加
    result = np.zeros_like(img, dtype=np.float32)
    for kernel in kernel_list:
        i_conv = cv2.filter2D(img, cv2.CV_32F, kernel, borderType=cv2.BORDER_DEFAULT)
        i_conv = np.abs(i_conv)
        result += i_conv


        # 對結果進行閾值處理
        result[result > 255] = 255
        result = result.astype(np.uint8)
        
        return result


if __name__ == '__main__':
    img = cv2.imread('D:/Documents/ImgProcess/picture/highway.jpg', 0)
    edge = robinson(img)
    cv2.imwrite('robinson_edge.jpg', edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
