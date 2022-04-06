import cv2 as cv

img= cv.imread('Images/img1.jpg')
cv.imshow('Image',img)

#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresh', thresh)
threshold, thresh_inverse = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresh inverse', thresh_inverse)

#adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive thresholding', adaptive_thresh)
cv.waitKey(0)