#B11056251 陳湘宇 ch13習題2
import cv2
import numpy as np

def harris_corner_detection(f):
    g = cv2.cvtColor(f, cv2.COLOR_GRAY2BGR)
    nr, nc = f.shape[:2]
    gray = np.float32(f)
    dst = cv2.cornerHarris(gray, 2, 3, 0.15)
    for x in range(nr):
        for y in range(nc):
            if dst[x, y] > 0.1 * dst.max():
                cv2.circle(g, (y, x), 5, [255, 0, 0], 2)
    return g

def main():
    imgl = cv2.imread("D:/Documents/ImgProcess/picture/brick.jpg", 0)
    img2 = harris_corner_detection(imgl)
    #cv2.imshow("Original Image", imgl)
    cv2.imwrite("Harris Corners(015).jpg", img2)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()

main()
