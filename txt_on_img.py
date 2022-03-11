import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank',blank)

cv.putText(blank,'HELLO',(250,250),cv.FONT_HERSHEY_TRIPLEX, 2, (255,0,0), thickness=2)
cv.imshow('Text',blank)

cv.waitKey(0)