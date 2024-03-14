# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:38:01 2024

@author: jayiu
"""

import cv2 as cv
import sys
cap = cv.VideoCapture(0, cv.CAP_DSHOW)
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
print('width: %d, height: %d' %(width, height))

if not cap.isOpened():
    sys.exit('비디오를 열 수 없습니다')
    
while cap.isOpened():
    ret, video = cap.read()
    if not ret:
        sys.exit('프레임획득에 실패하여 루프를 탈출')
        break
    cv.imshow('video file', video)
    key = cv.waitKey(25)
    if key==ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()