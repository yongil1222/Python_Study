import numpy as np
import cv2

def recordVideo():
    try:
        print('Init. Camera')
        cap = cv2.VideoCapture(0)
    except:
        print('failed init camera')
        return
    
    fps = 25.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    heigh = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fcc = cv2.VideoWriter_fourcc('D','I','V','X')

    out = cv2.VideoWriter('E:/Python_Study/OpenCV/video.avi', fcc, fps, (width, heigh))
    print('Recording started')

    while True:
        ret, frame = cap.read()

        if not ret:
            print('Error while reading video')
            break

        cv2.imshow('video', frame)
        out.write(frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

recordVideo()