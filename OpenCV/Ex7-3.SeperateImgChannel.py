import numpy as np
import cv2

img = cv2.imread('E:/Python_Study/OpenCV/images/model.jpg')
cv2.imshow('original', img)

b,g,r = cv2.split(img)

cv2.imshow('blue channel', b)
cv2.imshow('green channel', g)
cv2.imshow('red channel', r)

cv2.waitKey(0)
cv2.destroyAllWindows()