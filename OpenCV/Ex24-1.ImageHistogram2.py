import numpy as np
import cv2

img = cv2.imread('E:/Python_Study/OpenCV/images/hist.jpg', cv2.IMREAD_GRAYSCALE)

def histogram():
    hist, bins = np.histogram(img.ravel(), 256, [0, 256])
    cdf = hist.cumsum()

    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m-cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')

    img2 = cdf[img]
    cv2.imshow('Histogram Equalization', img2)

def clahe():
    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(16,16))
    img2 = clahe.apply(img)

    cv2.imshow('Clahe', img2)

cv2.imshow('Original', img)

histogram()
clahe()

cv2.waitKey(0)
cv2.destroyAllWindows()