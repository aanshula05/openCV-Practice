#read images
import cv2 as cv

img= cv.imread('Images/img1.jpg')
cv.imshow('img1',img)

cv.waitKey(0)