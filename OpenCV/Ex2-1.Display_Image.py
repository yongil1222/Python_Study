import numpy as np
import cv2

def showImage():
    imgfile = 'E:/Python_Study/OpenCV/images/model.jpg'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)

    cv2.namedWindow('model', cv2.WINDOW_NORMAL)
    cv2.imshow('model', img)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('c'):
        cv2.imwrite('E:/Python_Study/OpenCV/images/model-copy.png', img)
        cv2.destroyAllWindows()

showImage()