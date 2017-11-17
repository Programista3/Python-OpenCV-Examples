import cv2

image1 = cv2.imread('media/Leaves.jpg')
image2 = cv2.imread('media/Lion.jpg')

image3 = cv2.addWeighted(image1,0.3,image2,0.7,0)

cv2.imshow('Image', image3)
cv2.waitKey(0)
cv2.destroyAllWindows()