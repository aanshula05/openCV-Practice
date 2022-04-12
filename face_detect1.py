import cv2 as cv

img= cv.imread('Images/group.jpg')
#cv.imshow('Image',img)

resized_img = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized img', resized_img)
gray = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
#detects only 3 out of the 6 faces since haar cascades is sensitive to noise in imgs
print(f'Number of faces found: {len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(resized_img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected faces', resized_img)
cv.waitKey(0)