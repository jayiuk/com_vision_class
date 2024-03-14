# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:06:07 2024

@author: jayiu
"""

import cv2 as cv
import sys
img = cv.imread('C:/com_vision/source/image/girl_laughing.jpg')
if img is None:
    sys.exit('파일을 찾을 수 없습니다')
    
BrushSiz = 5
LColor, RColor = (0, 0, 0), (255, 255, 255)

def painting(event, x, y, flags, param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), BrushSiz, LColor, -1)
    elif event==cv.EVENT_RBUTTON:
        cv.circle(img, (x, y), BrushSiz, RColor, -1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        cv.circle(img, (x, y), BrushSiz, LColor, -1)
    elif event==cv.EVENT_MOUSEMOVE and flags--cv.EVENT_FLAG_RBUTTON:
        cv.circle(img, (x, y), BrushSiz, RColor, -1)
        
    cv.imshow('painting', img)

cv.namedWindow('painting')
cv.imshow('painting', img)
cv.setMouseCallback('painting', paint)

while True:
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break