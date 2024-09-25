import cv2 as cv

# contours are basically the boundaries of the objects
# helps in shape analysis, object detection and recognition

img = cv.imread("./h.jpeg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

canny = cv.Canny(img, 125, 175)
cv.imshow("edges", canny)

contours, heirarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# countours is the list of coordinates of all the contours that were found
# heirarchies is the representation of contours in heirarchy
# RETR_LIST returns all the contours discovered
# CHAIN_APPROX is used to approximate the contour : NONE does nothing and returns as it is
# we can use SIMPLE instead of NONE as it compresses all the contours are returns which makes the most sense

print(f'{len(contours)} contours found')

cv.waitKey(0)