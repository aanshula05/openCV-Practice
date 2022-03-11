import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8') #dtype= data type, uint8 is the data type for images
#height, width and number of color channels

cv.imshow('Blank',blank)

#draws a blue rectangle using the rectangle method
cv.rectangle(blank,(25,25), (200,350) ,( 255,0,0) ,thickness=2) #only border shown
#(0,0)= start point ie origin , (200,200)= end point

cv.imshow('Rectangle', blank)

cv.waitKey(0)