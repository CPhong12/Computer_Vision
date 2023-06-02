import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # Work with Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Work with Live video
    capture.set(3, width)
    capture.set(4, height)


# Rescale Image
img = cv.imread("D:\Code\OpenCV\Resources\Photos\cat.jpg")
cv.imshow('Cat', img)

resized_image = rescaleFrame(img)
cv.imshow('Img-resized', resized_image)

cv.waitKey(0)

# Rescale Videos
capture = cv.VideoCapture('D:\Code\OpenCV\Resources\Videos\dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
