# from https://docs.opencv.org/3.4.0/df/d9d/tutorial_py_colorspaces.html
import cv2 as cv

# define range of blue color in HSV
lower_blue = (110, 50, 50)
upper_blue = (130, 255, 255)

cap = cv.VideoCapture(0)

while True:
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
