#to draw a circle
import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank',blank)

cv.circle(blank, (250,250), 40, (255,0,0), thickness=cv.FILLED)
cv.imshow('Circle', blank)


#to draw line
cv.line(blank,(0,0),(250,250),(0,0,255),thickness=2)
cv.imshow('Line', blank)
cv.waitKey(0)