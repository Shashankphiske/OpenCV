import cv2 as cv

img = cv.imread('./h.jpeg') #takes path of the image an returns that img as a matrix of pixels
cv.imshow("pic", img) #displays the img as a new window

#reading vids :
capture = cv.VideoCapture("C:\\Users\\shash\\Videos\\Valorant\\rizz.mp4") # takes integer arguments or a path to the video file
# integer arguments will be used when we use a camera module
# capture variable is an instance of the class VideoCapture
# for reading videos we use a while loop and read the video frame by frame
while True:
    isTrue, frame = capture.read() #.read() reads the vid frame by frame and returns the frame in frame variable and a boolean val
                                   # in isTrue to indicate that if the frame was read or not
    cv.imshow("Video", frame)
    if cv.waitKey(20) & 0xFF==ord('d'): # to stop video repeating in a loop, if d is pressed then break
        break
capture.release()
cv.destroyAllWindows()
#cv.waitKey(0) : keyboard binding function, waits for certain milliseconds for a keypress (0:infinite time)
# opencv does not have ways to deal with images larger than your computer screen