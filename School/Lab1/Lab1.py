import cv2 as cv
import numpy as np


def draw_rectangle(event, x, y, flags, params):
    global pt1, pt2, drawing

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        pt1 = (x, y)

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            pt2 = (x, y)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        pt2 = (x, y)
        cv.rectangle(img, pt1, pt2, (0, 0, 255), 2)


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])  # row,col = img,shape[:2]
    # biến đổi vị trí, tỷ lệ, hướng
    return cv.warpAffine(img, transMat, dimensions)


def rescaleFrame(frame, scale):
    # Work with Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


rec = cvRectangle()
cv.namedWindow('image')
cv.setMouseCallback('image', draw_rectangle)
while True:
    print("1. Create white board")
    print("2. Draw rectangle")
    print("3. Translation rectangle")
    print("4. Rotation rectangle")
    print("5. Scaling reactangle")
    choice = input("Enter your choice: ")

    if choice == "1":
        img = np.zeros((500, 500, 3), dtype='uint8')*255
        img.fill(255)
    elif choice == "2":
        while True:
            cv.imshow('image', img)
            k = cv.waitKey(1) & 0xFF
            if k == 27:
                break
    elif choice == "3":
        tx = int(input('Enter translation in x direction: '))
        ty = int(input('Enter translation in y direction: '))
        translate(img, tx, ty)
    elif choice == "4":
        theta = float(input('Enter rotation angle in degrees: '))
        rotate(img, theta)
    elif choice == "5":
        s = float(input('Enter scaling factor in direction: '))
        rescaleFrame(img, s)
    else:
        # Invalid choice
        print("Invalid choice. Please try again.")
        print("Exiting...")
        break
    cv.imshow('image', img)
    cv.waitKey(20)
