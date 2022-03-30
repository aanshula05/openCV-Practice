import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Images/img1.jpg')
cv.imshow('Image',img)
#matplotlib displays imgs in rgb format
plt.imshow(img)
plt.show()

#BGR to Grayscale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR to HSV(hue saturation value)
hsv= cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

#BGR to RGB
rgb= cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

plt.imshow(rgb)
plt.show()

#hsv to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV->BGR', hsv_bgr)
cv.waitKey(0)