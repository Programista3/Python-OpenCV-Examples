import cv2

image = cv2.imread('media/Leaves.jpg', 1) # Load a color image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert image to grayscale
cv2.imshow('Image in grayscale', gray) # Show image
cv2.waitKey(0)
cv2.destroyAllWindows()