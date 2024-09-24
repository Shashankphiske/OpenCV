import cv2 as cv

img = cv.imread("./scene.jpg") # this is an BGR image, three chanel blue,green and red

#we will convert this bgr image to grey scale
grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def rescaleIMG(img, scale=0.2):
    width = int(img.shape[0] * scale)
    height = int(img.shape[1] * scale)
    dimensions = (width, height)
    
    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
resized = rescaleIMG(grey_img) # grey scale image

cv.imshow("resize", resized)

# we will blur an image
# we will apply blur to reduce the noise in the image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# 3,3 here is the blur size, we can increase it by increasing these numbers
cv.imshow("blur", blur)

# how to find edge cascades in the img
canny = cv.Canny(img, 125, 175) # this will return the image with only the edges found in it
# the edges can be reduced by applying blur
resized_canny = rescaleIMG(canny)
cv.imshow("edges", resized_canny)

# dilating an image
dilated = cv.dilate(resized_canny, (7,7), iterations=3)
cv.imshow("dilated", dilated)

# we can erode this dilated image back to our original image of edges
eroded = cv.erode(dilated, (7,7), iterations=3) # this erosion doesnt help in all of the cases
cv.imshow("eroded", eroded)

# Resize image
resized = cv.resize(img, (250,250), interpolation=cv.INTER_AREA)
cv.imshow("resize", resized)

#cropping an image
cropped = resized[50:100, 100:200] # first value is for y axis of img and other is for x axis
cv.imshow("cropped", cropped)
cv.waitKey(0)