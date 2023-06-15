#B11056251 陳湘宇 ch13習題3-SIFT
import numpy as np
import cv2

def sift_feature_detection(f):
    g = cv2.cvtColor(f, cv2.COLOR_GRAY2BGR)
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(f, None)
    g = cv2.drawKeypoints(f, kp, g)
    return g

def main():
    img1 = cv2.imread("D:/Documents/ImgProcess/picture/brick.jpg", 0)
    img2 = sift_feature_detection(img1)
    #v2.imshow("Original Image", img1)
    cv2.imwrite("SIFT Features.jpg", img2)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()

main()
