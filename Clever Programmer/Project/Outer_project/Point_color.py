import cv2 as cv


def event(event, x, y, flag, para):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.putText(img, str(x)+',' + str(y), (x, y),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 222, 0), 2)
        cv.imshow('image', img)
    if event == cv.EVENT_RBUTTONDOWN:
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv.putText(img, str(b)+','+str(g)+','+str(r), (x, y),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 222, 0), 2)
        cv.imshow('image', img)


if __name__ == "__main__":
    img = cv.imread('D:\Code\OpenCV\Resources\Photos\cat.jpg', 1)
    cv.imshow('image', img)
    cv.setMouseCallback('image', event)
    cv.waitKey(0)
    cv.destroyAllWindows()
