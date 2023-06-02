import cv2 as cv

img = cv.imread('C:\Code\OpenCV\Resources\Photos\park.jpg')
cv.imshow('Cats', img)

# Averaging
average = cv.blur(img, (5, 5))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (5, 5), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 5)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral Filter', bilateral)

cv.waitKey(0)
