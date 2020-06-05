import numpy as np
import cv2

def showVideo():
    try:
        print('Init. Camera')
        cap = cv2.VideoCapture(0)
    except:
        print('failed init camera')
        return
    
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

    while True:
        ret, frame = cap.read()

        if not ret:
            print('Error while reading video')
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('video', gray)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

showVideo()