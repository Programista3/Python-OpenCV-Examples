import cv2

image = cv2.imread('media/Leaves.jpg', 0) # Load image in grayscale
cv2.imwrite('media/gray.jpg', image) # Save image to file
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()