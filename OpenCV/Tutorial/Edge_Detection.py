import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Code\OpenCV\34433426ce960f2ed33d13696c387e8b.jpg')
cv.imshow('cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Laplacian
# (phát hiện cạnh, biên độc lập, và giảm nhiễu ảnh)
# tăng cường độ tương phản và trích xuất đặc trưng của các khu vực quan trọng trong ảnh
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow('Laplacian', lap)

# Sobel (Output là gradient của ảnh)
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)
edges = cv.resize(combined_sobel, (img.shape[1], img.shape[0]))

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combine Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

sharp_image = cv.addWeighted(img, 1.5, edges, 0.5, 0)

cv.waitKey(0)
