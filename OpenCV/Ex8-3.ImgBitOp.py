import numpy as np
import cv2

def bitOperation(hpos, vpos):
    img1 = cv2.imread('E:/Python_Study/OpenCV/images/model.jpg')
    img2 = cv2.imread('E:/Python_Study/OpenCV/images/openCV.jpg')

    rows, cols, channel = img2.shape
    roi = img1[vpos:rows+vpos, hpos:cols+hpos]

    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 15, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    #cv2.imshow('mask', mask)
    #cv2.imshow('mask_inv', mask_inv)

    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    #cv2.imshow('img1_bg', img1_bg)
    #cv2.imshow('img2_fg', img2_fg)

    dst = cv2.add(img1_bg, img2_fg)
    
    #cv2.imshow('added', dst)

    img1[vpos:rows+vpos, hpos:cols+hpos] = dst
    
    cv2.imshow('result', img1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

bitOperation(10,10)