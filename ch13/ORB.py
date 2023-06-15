#B11056251 陳湘宇 ch13習題3-ORB
import cv2 as cv

def orb_feature_detection(f):
    orb = cv.ORB_create()
    kp, des = orb.detectAndCompute(f, None)
    g = cv.drawKeypoints(f, kp, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return g

def main():
    img1 = cv.imread("D:/Documents/ImgProcess/picture/brick.jpg", 0)
    img2 = orb_feature_detection(img1)
    #cv.imshow("Original Image", img1)
    cv.imwrite("ORB Features.jpg", img2)
    cv.waitKey(0)
    cv.destroyAllWindows()

main()
