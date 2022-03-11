import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8') #dtype= data type, uint8 is the data type for images
#height, width and number of color channels

cv.imshow('Blank',blank)

#to fill rectangle
cv.rectangle(blank,(25,25), (200,350) ,( 255,0,0) ,thickness=cv.FILLED) #or thickness=-1
cv.imshow('Rectangle', blank)

cv.waitKey(0)