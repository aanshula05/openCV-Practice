import cv2 as cv
import numpy as np

img= cv.imread('Images/img1.jpg')
cv.imshow('Image',img)

#to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#laplacian(it computes the gradients of the gray img)
lap = cv.Laplacian(gray, cv.CV_64F) #cv.CV_64F is data depth
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#sobel (creates gradients in x and y directions)
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) #dx=1, dy=0
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or( sobelx, sobely)

cv.imshow('SobelX', sobelx)
cv.imshow('SobelY', sobely)
cv.imshow('Combined sobel', combined_sobel)
cv.waitKey(0)
