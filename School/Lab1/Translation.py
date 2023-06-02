import cv2 as cv
import numpy as np

# create a black image with a rectangle
img = np.zeros((512, 512, 3), dtype='uint8')
pt1 = (100, 100)
pt2 = (200, 200)
cv.rectangle(img, pt1, pt2, (0, 255, 0), 2)

# display the original image
cv.imshow('Original Image', img)
cv.waitKey(0)
# get translation information from user
tx = int(input('Enter translation in x direction: '))
ty = int(input('Enter translation in y direction: '))

# create a translation matrix
M = np.float32([[1, 0, tx], [0, 1, ty]])

# apply the translation transformation to the rectangle points
rect = np.array([[pt1[0], pt1[1], 1], [pt2[0], pt2[1], 1]])
rect_translated = np.dot(M, rect.T).T.astype(int)

# create a new image with the translated rectangle
pt1_translated = (rect_translated[0][0], rect_translated[0][1])
pt2_translated = (rect_translated[1][0], rect_translated[1][1])
cv.rectangle(img, pt1_translated, pt2_translated, (0, 0, 255), 2)

# display the translated image
cv.imshow('Translated Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
