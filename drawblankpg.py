#to draw a blank black page
import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8') #dtype= data type, uint8 is the data type for images
#height, width and number of color channels
cv.imshow('Blank',blank)

cv.waitKey(0)