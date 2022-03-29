import cv2 as cv

img=cv.imread('Images/img1.jpg')
cv.imshow('Images',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny=cv.Canny(img,125,175)
cv.imshow('Canny',canny)

contours, hierarchies= cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours(s) found')
cv.waitKey(0)
