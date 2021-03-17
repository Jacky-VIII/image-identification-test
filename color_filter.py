import cv2 as cv
import numpy as np

test01 = cv.imread("source/test01.jpg")
img = test01.copy()


def nothing(x):
    pass


#name = ['Main Image', 'Image', 'mask', 'res', 'Tracking']

cv.namedWindow('Tracking', cv.WINDOW_NORMAL)
cv.resizeWindow('Tracking', 600, 300)
cv.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv.createTrackbar('HH', 'Tracking', 255, 255, nothing)
cv.createTrackbar('HS', 'Tracking', 255, 255, nothing)
cv.createTrackbar('HV', 'Tracking', 255, 255, nothing)


while True:
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    l_h = cv.getTrackbarPos('LH', 'Tracking')
    l_s = cv.getTrackbarPos('LS', 'Tracking')
    l_v = cv.getTrackbarPos('LV', 'Tracking')
    h_h = cv.getTrackbarPos('HH', 'Tracking')
    h_s = cv.getTrackbarPos('HS', 'Tracking')
    h_v = cv.getTrackbarPos('HV', 'Tracking')

    l_b = np.array([l_h, l_s, l_v])  # low value
    u_b = np.array([h_h, h_s, h_v])  # high value

    mask = cv.inRange(hsv, l_b, u_b)  # color filter

    res = cv.bitwise_and(img, img, mask=mask)  # result

    cv.imshow('Image', img)
    #cv.imshow('mask', mask)
    cv.imshow('res', res)

    key = cv.waitKey(1)
    if key == 27:
        cv.destroyAllWindows()
        break


