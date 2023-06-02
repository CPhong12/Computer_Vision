import cv2 as cv
import numpy as np

# create a black image with a rectangle
img = np.zeros((512, 512, 3), np.uint8)
pt1 = (100, 100)
pt2 = (200, 200)
cv.rectangle(img, pt1, pt2, (0, 255, 0), -1)

# display the original image
cv.imshow('Original Image', img)
cv.waitKey(0)
# get rotation angle from user
theta = float(input('Enter rotation angle in degrees: '))


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, theta)

cv.imshow('Rotated Image', rotated)
cv.waitKey(0)
cv.destroyAllWindows()


def Choose():
    choice = input("Enter your choice: ")

    if choice == "1":
        # Code for option 1
        print("Option 1 selected")
    elif choice == "2":
        # Code for option 2
        print("Option 2 selected")
    elif choice == "3":
        # Code for option 3
        print("Option 3 selected")
    elif choice == "4":
        # Exit the menu
        print("Exiting...")
        break
    else:
        # Invalid choice
        print("Invalid choice. Please try again.")


def Menu():
    print('1. Draw a white board')


while True:
    Menu()
