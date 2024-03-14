# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:48:17 2024

@author: jayiu
"""

import cv2 as cv
import sys
img = cv.imread('C:/com_vision/source/image/girl_laughing.jpg')
if img is None:
    sys.exit('파일을 찾을 수 없습니다')

cv.rectangle(img, (830, 30), (1000, 200), (0, 0, 255), 2)
cv.putText(img, 'laugh', (830, 24), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
cv.imshow('laughing', img)
cv.waitKey()
cv.destroyAllWindows()