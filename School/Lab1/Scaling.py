import cv2
import numpy as np

# create a black image with a rectangle
img = np.zeros((512, 512, 3), np.uint8)
pt1 = (100, 100)
pt2 = (200, 200)
cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)

# display the original image
cv2.imshow('Original Image', img)
cv2.waitKey(0)
# get scaling factors from user
sx = float(input('Enter scaling factor in x direction: '))
sy = float(input('Enter scaling factor in y direction: '))

# create a scaling matrix
M = np.float32([[sx, 0, 0], [0, sy, 0]])

# apply the scaling transformation to the rectangle points
rect = np.array([[pt1[0], pt1[1], 1], [pt2[0], pt2[1], 1]])
rect_scaled = np.dot(M, rect.T).T.astype(int)

# create a new image with the scaled rectangle
pt1_scaled = (rect_scaled[0][0], rect_scaled[0][1])
pt2_scaled = (rect_scaled[1][0], rect_scaled[1][1])
cv2.rectangle(img, pt1_scaled, pt2_scaled, (0, 0, 255), 2)

# display the scaled image
cv2.imshow('Scaled Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
