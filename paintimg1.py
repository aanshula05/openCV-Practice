#to paint a specific portion of the image
import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8') #dtype= data type, uint8 is the data type for images
#height, width and number of color channels

cv.imshow('Blank',blank)

#to paint the black box green
blank[200:300, 300:400]= 0,255,0
cv.imshow('Green', blank)

cv.waitKey(0)