import cv2 as cv
import numpy as np

img = cv.imread("./h.jpeg")

# translation : the image will be shifted in a direction
def translation(img, x, y):
    transMAT = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMAT, dimensions)

# -x ---> translating the img to left
# x ---> translating to right
# -y ---> translating to up
# y ---> translating to down

translated = translation(img, 100, -100) # 200, 300 are pixels here
cv.imshow("translated", translated)


# rotating an image
def rotate(img, angle, point=None):
    (height, width) = img.shape[:2]
    
    if point is None:
        point = (width//2, height//2)
    rotMAT = cv.getRotationMatrix2D(point, angle, 0.5) # 0.5 is the scale value
    dimensions = (width, height)
    return cv.warpAffine(img, rotMAT, dimensions)
    
rotated = rotate(img, 90)
cv.imshow("rotated", rotated)

# flipping an image
flip = cv.flip(rotated, 0)
# 0 ---> flipping vertically
# 1 ---> flipping horizontally
# -1 ---> flipping on both axis
cv.imshow("flip", flip)


cv.waitKey(0)