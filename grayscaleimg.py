import cv2 as cv
img=cv.imread('Images/img1.jpg')
#cv.imshow('Image',img)

#resize
resized=cv.resize(img,(500,500), interpolation= cv.INTER_CUBIC)
cv.imshow('resized',resized)

#convert BGR to gray
gray=cv.cvtColor(resized,cv.COLOR_BGRA2GRAY)
cv.imshow('Gray',gray)

#blur an img
blur=cv.GaussianBlur(resized,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#edge cascade
canny=cv.Canny(resized,125,175)
cv.imshow('Canny edges',canny)

#dilating image
dilated=cv.dilate(canny, (7,7), iterations=1)
cv.imshow('Dilated img',dilated)

#eroded
eroded=cv.erode(dilated, (3,3), iterations=1)
cv.imshow('eroded img',eroded)





cv.waitKey(0)