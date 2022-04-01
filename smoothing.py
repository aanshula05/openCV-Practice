import cv2 as cv
img = cv.imread('Images/img1.jpg')
cv.imshow('Image',img)

#averaging
average = cv.blur(img,(3,3)) #(3,3)-> kernel size
cv.imshow('average blur', average)

#gaussian blur
gaussian = cv.GaussianBlur(img, (3,3), 0) #0-> standard deviation in x
cv.imshow('Gaussian blur', gaussian)

#median blur
median = cv.medianBlur(img, 3) #ksize has to be an integer
cv.imshow('Median blur', median)

#bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral img', bilateral)

cv.waitKey(0)