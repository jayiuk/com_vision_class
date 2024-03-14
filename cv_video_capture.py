# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:39:18 2024

@author: jayiu
"""

import cv2 as cv
import numpy as np
import sys
cap = cv.VideoCapture('C:/com_vision/source/video/jeju.mp4')
width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
print('width: %d, height: %d' %(width, height))

frames = []
if not cap.isOpened():
    sys.exit('비디오를 열 수 없습니다')
    
while cap.isOpened():
    ret, video = cap.read()
    if not ret:
        sys.exit('프레임획득에 실패하여 루프를 탈출')
        break
    cv.imshow('video file', video)
    key = cv.waitKey(25)
    if key==ord('c'):
        frames.append(video)
    if key==ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()

if len(frames) > 0:
    imgs = frames[0]
    for i in range(1, min(3, len(frames))):
        imgs = np.hstack((imgs, frames[i]))
    cv.imwrite('C:/com_vision/source/image/collected.jpg', imgs)
    cv.imshow('collected_images', imgs)
    cv.waitKey()
    cv.destroyAllWindows()