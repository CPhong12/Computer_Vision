from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float

img = io.imread(r"C:\Code\OpenCV\DigitalSreeni\Hubble_ultra_deep_field.jpg")
# print(img)  # matrix
print(img.shape)
print(img.min(), img.max())  # in ra min max của giá trị pixel ảnh
plt.imshow(img)

# img[0:200, 0:200, :] = [255, 255, 255] đổi màu 1 phần ảnh
plt.imshow(img)
plt.show()

# !Convert pixel (0-255) to float (0-1)
float_img = img_as_float(img)
print(float_img.min(), float_img.max())
plt.imshow(float_img)
plt.show()

# !Create random img
random_img = np.random.random([500, 500])
plt.imshow(random_img)
print(random_img.min(), random_img.max())
plt.show()

# !Pixel*2
dark_img = img*2
plt.imshow(dark_img)
plt.show()
print(dark_img)

# !Draw rectangle

img[10:200, 10:200, :] = [255, 0, 0]
plt.imshow(img)
plt.show()
