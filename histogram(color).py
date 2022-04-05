import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread('Images/img1.jpg')
cv.imshow('Image',img)

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank,(img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mask',masked)
colors = ('b', 'g', 'r')
plt.figure()
plt.title('Color histogram')
plt.xlabel('Bins') #represents intervals of pixel intensities
plt.ylabel('no of pixels')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()


cv.waitKey(0)