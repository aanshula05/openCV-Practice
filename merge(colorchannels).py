import cv2 as cv
import numpy as np

img = cv.imread('Images/scenery.jpg')
#cv.imshow('OG img',img)

#resize
#resized = cv.resize(img,(250,250), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized', resized)

blank = np.zeros(img.shape[:2], dtype='uint8') #dtype=>data type
b,g,r = cv.split(img)
blue = cv.merge([b,blank,blank]) #list
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#gives us the og img
merged = cv.merge([b,g,r])
cv.imshow('merged',merged)
cv.waitKey(0)