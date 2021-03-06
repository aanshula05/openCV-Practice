#webcam resized (similiarly resize video)

import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)

    dimensions= (width,height)

    return cv.resize(frame, dimensions, interpolation =cv.INTER_AREA)

capture=cv.VideoCapture(0)

while True:
    isTrue, frame= capture.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('f'):
        break

capture.release()
cv.destroyAllWindows()


