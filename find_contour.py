import cv2 as cv
import numpy as np

test01 = cv.imread("source/test01.jpg")


def nothing(x):
    pass


cv.namedWindow('Tracking')
cv.resizeWindow('Tracking', 600, 100)
cv.createTrackbar('maxValue', 'Tracking', 255, 255, nothing)
cv.createTrackbar('C', 'Tracking', 1, 255, nothing)


while True:
    img = test01.copy()
    gray = cv.cvtColor(test01, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 5)
    maxValue = cv.getTrackbarPos('maxValue', 'Tracking')
    C = cv.getTrackbarPos('C', 'Tracking')
    thresh = cv.adaptiveThreshold(blur, maxValue, 1, 1, 5, C)

    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    cv.drawContours(img, contours, -1, (0, 255, 0), 3)
    #cnt = contours[4]
    #cv.drawContours(img, [cnt], 0, (0, 255, 0), 3)

    cv.imshow('Image', test01)
    cv.imshow('res', img)

    key = cv.waitKey(1)
    if key == 27:
        cv.destroyAllWindows()
        break

