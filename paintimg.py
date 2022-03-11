
import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8') #dtype= data type, uint8 is the data type for images
#height, width and number of color channels

cv.imshow('Blank',blank)

#to paint the black box green
blank[:]= 0,255,0
cv.imshow('Green', blank)

#to paint the box red
blank[:]= 0,0,255
cv.imshow('Red', blank)

#to paint the box blue
blank[:]= 255,0,0
cv.imshow('Blue', blank)
cv.waitKey(0)