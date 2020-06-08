import numpy as np
import cv2

img = cv2.imread('E:/Python_Study/OpenCV/images/model.jpg')
cv2.imshow('original', img)

subimg = img[200:300, 300:500]
cv2.imshow('cutting', subimg)

img[200:300, 100:300] = subimg

print(img.shape)
print(subimg.shape)

cv2.imshow('modified', img)

cv2.waitKey(0)
cv2.destroyAllWindows()