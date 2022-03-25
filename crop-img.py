import cv2 as cv
img=cv.imread('Images/img1.jpg')
cv.imshow('image',img)

print("shape of the image is",img.shape)

crop = img[100:500, 100:300]
cv.imshow('cropped',crop)

cv.waitKey(0)