import cv2

image = cv2.imread('media/Leaves.jpg', 1) # Load a color image (1-color, 0-grayscale)
cv2.imshow('Image', image) # Show image
cv2.waitKey(0)
cv2.destroyAllWindows()