import numpy as np
import cv2
import matplotlib.pyplot as plt

def showImage():
    imgfile = 'E:/Python_Study/OpenCV/images/model.jpg'
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)

    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([])
    plt.yticks([])
    plt.title('model')
    plt.show()

showImage()