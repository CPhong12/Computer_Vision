import cv2 as cv

img = cv.imread('D:\Code\OpenCV\Project\Cat_detective\Cat1.jpg')
cat_cascade = cv.CascadeClassifier(
    r'D:\Code\OpenCV\Project\Cat_detective\frontalcatface.xml')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cat_faces = cat_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

for (x, y, w, h) in cat_faces:
    img = cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    cv.putText(img, 'lOrd', (x, y), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0))

cv.imshow('Cat', img)
cv.waitKey(0)
cv.destroyAllWindows()
