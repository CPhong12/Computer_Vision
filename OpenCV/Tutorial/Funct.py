import cv2 as cv

img = cv.imread('D:\Code\OpenCV\Resources\Photos\cat.jpg')
cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade (tìm các cạnh của ảnh)
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image (mở rộng viền)
dilated = cv.dilate(canny, (3, 3), iterations=1,
                    borderValue=cv.BORDER_CONSTANT)
cv.imshow('Dialated', dilated)

# Eroding (xói mòn viền)
eroded = cv.erode(canny, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)
