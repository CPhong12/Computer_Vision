import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageOps
import numpy as np

img = Image.open(r'C:\Code\OpenCV\Resources\Photos\flower.jpg')
""" 
print('Format:', img.format)
print('Size:', img.size)
print('Mode:', img.mode)  # kênh màu

plt.imshow(img)
plt.show()

#!
img_gray = ImageOps.grayscale(img)

print('Mode:', img_gray.mode)
# img_gray.quantize(2) #giảm số lượng màu sắc trong một hình ảnh
# img_gray.save('Gray_Flower.jpg')  # save ảnh

plt.imshow(img_gray)
plt.show()

#!
r, g, b = img.split()

r_gray = ImageOps.grayscale(r)

plt.imshow(r_gray)
plt.show() """

#!
array = np.array(img)
print(array)
