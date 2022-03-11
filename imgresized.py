#resize images

import cv2 as cv

img= cv.imread('Images/img1.jpg')
cv.imshow('img1',img)

def rescaleFrame(frame, scale=0.5):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)

    dimensions= (width,height)

    return cv.resize(frame, dimensions, interpolation =cv.INTER_AREA)

resized_image=rescaleFrame(img)
cv.imshow('Img resized', resized_image)

cv.waitKey(0)