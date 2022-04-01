import cv2 as cv

img = cv.imread('Images/scenery.jpg')
#cv.imshow('OG img',img)

#resize
#resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized', resized)
b,g,r = cv.split(img)
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
cv.waitKey(0)
