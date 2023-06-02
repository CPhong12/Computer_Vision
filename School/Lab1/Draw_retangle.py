import cv2
import numpy as np
# callback function for mouse events


def draw_rectangle(event, x, y, flags, params):
    global pt1, pt2, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        pt1 = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            pt2 = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        pt2 = (x, y)
        cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)


# create a black image
img = np.zeros((512, 512, 3), np.uint8)

# create a named window and set mouse callback
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

# main loop
while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # press Esc to exit
        break

cv2.destroyAllWindows()
