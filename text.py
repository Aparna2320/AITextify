#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
from PIL import Image
from pytesseract import pytesseract

camera = cv2.VideoCapture(0)

while True:
    _,Image=camera.read()
    cv2.imshow('image', image)
    if cv2.waitkey(1)& 0xFF==ord('s'):
        cv2.imwrite('test1.jpg',image)
        break
camera.release()
cv2.destroyAllWindows()

def tesseract():
    path_t0_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    Imagepath = 'test1.jpg'
    pytesseract_tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(Image.open(image_path))
    print(text)
tesseract()


# In[ ]:




