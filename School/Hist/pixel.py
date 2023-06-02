import cv2
import numpy as np

# Load the image
image = cv2.imread(r'C:\Code\OpenCV\34433426ce960f2ed33d13696c387e8b.jpg')

# Apply blur to the image
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Apply edge detection to the blurred image
edges = cv2.Canny(blurred_image, 50, 150)

# Resize the edges to match the size of the original image
edges = cv2.resize(edges, (image.shape[1], image.shape[0]))

# Convert the edges to 3 channels to match the number of channels in the original image
edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

# Add the edges back to the original image
sharp_image = cv2.addWeighted(image, 1.5, edges, 0.5, 0)

# Display the original and sharpened images
cv2.imshow('Original Image', image)
cv2.imshow('Sharpened Image', sharp_image)
cv2.waitKey(0)
