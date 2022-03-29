#drawing contours on blank img
import cv2 as cv
import numpy as np
img= cv.imread('Images/img1.jpg')
cv.imshow('Image',img)

blank= np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

#canny=cv.Canny(img,125,175)
#cv.imshow('Canny',canny)

#threshold binarizes the image
contours, hierarchies= cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours(s) found')

cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow('Contours drawn', blank)
cv.waitKey(0)



