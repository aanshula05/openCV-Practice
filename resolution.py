#to change resolution of webcam (this only works for webcam and not imgs/vids)
import cv2 as cv
capture=cv.VideoCapture(0)

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)
while True:
    isTrue, frame= capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()