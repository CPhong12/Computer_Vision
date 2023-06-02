import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
blank.fill(255)
cv.imshow('Blank', blank)

cv.waitKey(0)
