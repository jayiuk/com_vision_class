# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:42:32 2024

@author: jayiu
"""

import cv2 as cv
import sys
img = cv.imread('C:/com_vision/source/image/soccer.jpg')
if img is None:
    sys.exit('파일을 찾을 수 없습니다')
cv.imshow('Image Display', img)
cv.waitKey()
cv.destroyAllWindows()

print(type(img))
print(img.shape) #실제 좌표 인식할 때 x는 컬럼, y는 행
print(img[0,0,0], img[0,0,1], img[0,0,2])
print(img[0,1,0], img[0,1,1], img[0,1,2])