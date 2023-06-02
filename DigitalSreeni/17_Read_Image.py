
# * Read img with Pillow

import glob
from apeer_ometiff_library import io
import czifile
from matplotlib import pyplot as plt
import cv2 as cv
from skimage import io, img_as_float, img_as_ubyte
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import numpy as np

img = Image.open("C:\Code\OpenCV\DigitalSreeni\Hubble_ultra_deep_field.jpg")
print(type(img))  # !not numpy array

# img.show() #show img in laptop
print(img.format)

#!Convert to np array
img1 = np.asarray(img)
print(type(img1))


# * Read img with matplotlib

img = mpimg.imread("C:\Code\OpenCV\DigitalSreeni\Hubble_ultra_deep_field.jpg")
print(type(img))
print(img.shape)
plt.imshow(img)

plt.colorbar()
plt.show()

# * Read img with scikit-image (same to matplotlib)

# astype(np.float) #not between 0-1 just float
img = io.imread("C:\Code\OpenCV\DigitalSreeni\Hubble_ultra_deep_field.jpg")
print(type(img))  # numpy array
plt.imshow(img)
plt.show()
img_float = img_as_float(img)  # to 0-1
print(img_float)
img_ubyte = img_as_ubyte(img)
print(img_as_ubyte)

# * Read img with OpenCV


img = cv.imread(r'C:\Code\OpenCV\DigitalSreeni\Hubble_ultra_deep_field.jpg', 0)
# 0 - gray
# 1 - color
cv.imshow('Image', img)
cv.waitKey()
cv.destroyAllWindows()

# * Czifile File
# pip install czifile

img = czifile.imread('path.czi')
print(img.shape)

# * OME-TIFF
# pip install apeer-ometiff-library

(pic2, omexml) = io.read_ometiff('path.ome.tif')
print(pic2.shape)
# (time series, number dimension, color(RGB), x ,y)
print(pic2)  # numpy array
print(omexml)  # html file

# * Reading all image in file
# glob


path = 'path\*'

for file in glob.glob(path):
    print(file)
    a = cv.imread(file)
    print(a)
    c = cv.cvtColor(a, cv.COLOR_BGR2RGB)
    cv.imshow('Color Image', c)
    cv.waitKey(0)
    cv.destroyAllWindows()
