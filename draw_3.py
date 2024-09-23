import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")# create a blank image for size 500 x 500 and uint8 is basically image
# 3 is used to specify the number of color channels
cv.imshow("blank", blank)

# painting the image certain color :
blank[:] =  0, 255, 0
cv.imshow('Green', blank)

blank[200:300, 300:400] = 0,0,255
cv.imshow("red", blank)

#drawing a rectangle:
cv.rectangle(blank, (0,0), (250,250), (255,255,255), thickness=2)
#(0,0) is pt1 which is origin, 250,250 is pt2, 255,255,255 is the color of the rectangle
# if we do cv.filled then it will fill the entire reactangle with the specified color
cv.imshow("rect", blank)

#drawing a circle
cv.circle(blank, (250, 250), 40, (255,255,255), thickness=3)
# center is at 250, 250 and the radius of 40 pixels : 250,250 is the midpoint here of the window or image
# we can fill in the image by giving thickness = -1
cv.imshow("circle", blank)

#draw a line :
cv.line(blank, (0,0), (250,250), (255,255,255), thickness=4)
# (0,0) is the starting pt of the line and (250, 250) is the second pt of the line
cv.imshow("line", blank)

# writing text on an image
cv.putText(blank, "ShashankPhiske", (200,200), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,0), thickness=2)
# (255,255) is the start from where the text will start, 1.0 is the scale of the text
cv.imshow("text", blank)
cv.waitKey(0)