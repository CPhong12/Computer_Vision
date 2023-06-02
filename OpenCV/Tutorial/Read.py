import cv2 as cv

# Read image
img = cv.imread('D:\Code\OpenCV\Resources\Photos\cat.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)  # Ấn phím bất kỳ để tiếp tục
# Read video
capture = cv.VideoCapture('D:\Code\OpenCV\Resources\Videos\dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):  # Hết video or nhấn d để đóng
        break

capture.release()
cv.destroyAllWindows()
