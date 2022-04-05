import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img  = cv.imread('Images/img1.jpg')
cv.imshow('Image',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale',gray)

blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank,(img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Mask',mask)

#grayscale histogram
#gray_hist = cv.calcHist([gray], [0], None, [256], [0,256]) #256 is no of bins
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256]) #256 is no of bins
plt.figure()
plt.title('Grayscale histogram')
plt.xlabel('Bins') #represents intervals of pixel intensities
plt.ylabel('no of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()



cv.waitKey(0)