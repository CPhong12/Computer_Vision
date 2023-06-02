import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('meme.jpg')

print('Type:', type(img))
print('Shape:', img.shape)

cv.imshow('img', img)

rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(rgb_img)
plt.show()

b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)
cv.waitKey(0)
