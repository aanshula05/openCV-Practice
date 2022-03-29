import cv2 as cv

img= cv.imread('Images/img1.jpg')
cv.imshow('Image',img)

#BGR to Grayscale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR to HSV(hue saturation value)
hsv= cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

cv.waitKey(0)