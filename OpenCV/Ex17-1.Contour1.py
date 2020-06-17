import numpy as np
import cv2

def contour():
    img = cv2.imread('E:/Python_Study/OpenCV/images/globe.png')
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    contour_img = np.zeros((img.shape[0],img.shape[1],3), np.uint8)

    ret, thr = cv2.threshold(img_gray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(contour_img, contours, -1, (255, 255, 255), 1)
    cv2.imshow('thresh', thr)
    cv2.imshow('original', img)
    cv2.imshow('contour', contour_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

contour()