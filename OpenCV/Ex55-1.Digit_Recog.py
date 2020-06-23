import cv2
import numpy as np

def resize2D(digitImg):
    img = cv2.imread(digitImg)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret = cv2.resize(gray, (20,20), fx=1, fy=1, interpolation=cv2.INTER_AREA)
    ret, thr = cv2.threshold(ret, 127, 255, cv2.THRESH_BINARY_INV)

    cv2.imshow('ret', thr)

    return thr.reshape(-1, 400).astype(np.float32)

def learningDigit():
    img = cv2.imread('E:/Python_Study/OpenCV/images/digits.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
    x = np.array(cells)

    train = x[:,:].reshape(-1, 400).astype(np.float32)

    k = np.arange(10)
    train_labels = np.repeat(k,500)[:, np.newaxis]

    np.savez('E:/Python_Study/OpenCV/images/digits_for_ocr.npz', train=train, train_labels=train_labels)
    print('Data Saved')

def loadLearningDigit(ocrdata):
    with np.load(ocrdata) as f:
        traindata = f['train']
        traindatra_lebels = f['train_labels']
    
    return traindata, traindatra_lebels

def OCR_for_Digits(test, traindata, traindata_labels):
    knn = cv2.ml.KNearest_create()
    knn.train(traindata, cv2.ml.ROW_SAMPLE, traindata_labels)
    ret, result, neighbors, dist = knn.findNearest(test, k=5)

    return result

def main():
    #learningDigit()

    ocrdata = 'E:/Python_Study/OpenCV/images/digits_for_ocr.npz'
    traindata, traindata_labels = loadLearningDigit(ocrdata)
    digits = ['E:/Python_Study/OpenCV/images/' + str(x) + '.png' for x in range(10)]

    print(traindata.shape)
    print(traindata_labels.shape)

    savenpz = False
    for digit in digits:
        test = resize2D(digit)
        result = OCR_for_Digits(test, traindata, traindata_labels)

        print(result)

        k = cv2.waitKey(0)

        if k > 47 and k < 58:
            savenpz = True
            traindata = np.append(traindata, test, axis=0)
            new_label = np.array(int(chr(k))).reshape(-1,1)
            traindata_labels = np.append(traindata_labels, new_label, axis=0)

    cv2.destroyAllWindows()
    if savenpz:
        np.savez('E:/Python_Study/OpenCV/images/digits_for_ocr.npz', train=traindata, train_labels=traindata_labels)

main()