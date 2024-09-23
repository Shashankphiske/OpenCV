import cv2 as cv

# resizing is done to reduce computational power needed to process the large media files
capture = cv.VideoCapture("C:\\Users\\shash\\Videos\\Valorant\\rizz.mp4")



def rescaleFrame(frame, scale=0.75): # this func will take frame and scale value (default = 0.75)
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read() 
    frame_resized = rescaleFrame(frame, 0.5)
    cv.imshow("Video", frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
# same can be done for images

# to rescale live video :
# def changeRes(width, height):
#     live_vid.set(3, width)
#     live_vid.set(4, height)