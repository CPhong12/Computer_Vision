import cv2 as cv

img = cv.imread('D:\Code\OpenCV\Resources\Photos\cats.jpg')
cv.imshow('cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY)
# Giá trị ngưỡng được áp dụng và ảnh đã thresh
cv.imshow('Simple thresholding', thresh)
cv.waitKey(0)

# Inverse
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholding Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 1)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)
