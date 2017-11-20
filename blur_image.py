import cv2

image = cv2.imread('media/Leaves.jpg')
blur = cv2.blur(image, (10,10))
cv2.imshow('Blur Image', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()