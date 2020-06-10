import numpy as np
import cv2

def transform():
    img = cv2.imread('E:/Python_Study/OpenCV/images/model.jpg')
    h,w = img.shape[:2]

    pts1 = np.float32([[50,50], [200,50], [20,200]])
    pts2 = np.float32([[10,100], [200,50], [100,250]])

    pts3 = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
    pts4 = np.float32([[200, 0], [w-200, 0], [w, h], [0, h]])

    M1 = cv2.getAffineTransform(pts1, pts2)
    M2 = cv2.getPerspectiveTransform(pts3, pts4)

    img2 = cv2.warpAffine(img, M1, (w,h))
    img3 = cv2.warpPerspective(img, M2, (w,h))
    
    cv2.imshow('Original', img)
    cv2.imshow('Affine-Transform', img2)
    cv2.imshow('Perspective-Transform', img3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

transform()