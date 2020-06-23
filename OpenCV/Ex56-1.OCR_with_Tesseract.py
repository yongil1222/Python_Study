from PIL import Image
from pytesseract import *

def OCR(imgfile, lang='eng'):
    im = Image.open(imgfile)
    text = image_to_string(im, lang=lang)

    print('+++ OCR Result +++')
    print(text)

OCR('E:/Python_Study/OpenCV/images/ocr_test_eng.png')

print('\n\n')

OCR('E:/Python_Study/OpenCV/images/ocr_test_kor.png', lang='kor')