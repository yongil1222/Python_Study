import numpy as np
import cv2

img = cv2.imread('E:/Python_Study/OpenCV/images/model.jpg', cv2.IMREAD_GRAYSCALE)

ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
thr2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thr3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('original', img)
cv2.imshow('Global Threshold(v=127)', thr1)
cv2.imshow('Adaptive Mean', thr2)
cv2.imshow('Adaptive Gaussian', thr3)

cv2.waitKey(0)
cv2.destroyAllWindows()
