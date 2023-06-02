import cv2
image = cv2.imread(
    r'C:\Code\OpenCV\Game\ZigZag-master\LineTests\572color_54-74_23_HitLeft.png')
# Load the image

# Check if the image was loaded successfully
if image is not None:
    # Display the image
    cv2.imshow('Image', image)
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()
else:
    print('Failed to load the image.')

    # C:\Code\OpenCV\Game\ZigZag-master\LineTests\2002color_251-269_23_HitRight.png
