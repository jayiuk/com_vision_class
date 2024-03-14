# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:54:23 2024

@author: jayiu
"""

import cv2 as cv
import sys
img = cv.imread('C:/com_vision/source/image/girl_laughing.jpg')
if img is None:
    sys.exit('파일을 찾을 수 없습니다')
    
def draw(event, x, y, flags, param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img, (x, y), (x*200, y*200), (0, 0, 0), 2)
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.rectangle(img, (x, y), (x*100, y*100), (255, 255, 255), 2)
    cv.imshow('Drawing', img)
    
cv.namedWindow('Drawing')
cv.imshow('Drawing', img)
cv.setMouseCallback('Drawing', draw)

while True:
    if cv.waitKey(1)==ord('q'):
        cv.destroyAllWindows()
        break