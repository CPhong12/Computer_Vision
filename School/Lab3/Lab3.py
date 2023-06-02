import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread(r'C:\Code\OpenCV\School\Lab3\mang_cut.png')
cv.imshow("Original Image", image)


def plot_image(image_1, image_2, title_1="Orignal", title_2="New Image"):
    plt.figure(figsize=(10, 10))
    plt.subplot(1, 2, 1)
    plt.imshow(cv.cvtColor(image_1, cv.COLOR_BGR2RGB))
    plt.title(title_1)
    plt.subplot(1, 2, 2)
    plt.imshow(cv.cvtColor(image_2, cv.COLOR_BGR2RGB))
    plt.title(title_2)
    plt.show()


def plot_hist(old_image, new_image, title_old="Orignal", title_new="New Image"):
    intensity_values = np.array([x for x in range(256)])
    plt.subplot(1, 2, 1)
    plt.bar(intensity_values, cv.calcHist(
        [old_image], [0], None, [256], [0, 256])[:, 0], width=5)
    plt.title(title_old)
    plt.xlabel('intensity')
    plt.subplot(1, 2, 2)
    plt.bar(intensity_values, cv.calcHist(
        [new_image], [0], None, [256], [0, 256])[:, 0], width=5)
    plt.title(title_new)
    plt.xlabel('intensity')
    plt.show()


# Q0
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

plot_image(image, gray_image,
           title_1="Original Image", title_2="Gray Image")

# Q1
alpha = 1  # contrast
beta = 100  # brightness
new_image = cv.convertScaleAbs(gray_image, alpha=alpha, beta=beta)

plot_image(gray_image, new_image, title_1="Orignal",
           title_2="brightness control")

# Q2
e_hist = cv.equalizeHist(gray_image)

plot_image(gray_image, e_hist, "Gray_Image", "Histogram Equalization")

plt.figure(figsize=(10, 5))

plot_hist(gray_image, e_hist, "Gray_Image", "Histogram Equalization")

# Q3 - 4 - 5
# Plus noise
rows, cols, _ = image.shape
noise = np.random.normal(0, 15, (rows, cols)).astype(np.uint8)
noisy_image = gray_image + noise
plot_image(gray_image, noisy_image, title_1="Orignal",
           title_2="Image Plus Noise")

# Filtering noise

image_filtered = cv.medianBlur(src=noisy_image, ksize=5)
plot_image(image_filtered, noisy_image,
           title_1="Filtered image", title_2="Image Plus Noise")

kernel = np.ones((4, 4))/16
image_filtered = cv.blur(src=noisy_image, ksize=(5, 5))
plot_image(image_filtered, noisy_image,
           title_1="filtered image", title_2="Image Plus Noise")

# Gaussian smooth

image_filtered = cv.GaussianBlur(noisy_image, (5, 5), sigmaX=4, sigmaY=4)
plot_image(image_filtered, noisy_image,
           title_1="Filtered image", title_2="Image Plus Noise")

image_filtered = cv.GaussianBlur(noisy_image, (11, 11), sigmaX=10, sigmaY=10)
plot_image(image_filtered, noisy_image,
           title_1="filtered image", title_2="Image Plus Noise")

cv.destroyAllWindows()
