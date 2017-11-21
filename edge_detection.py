import cv2

image = cv2.imread('media/Leaves.jpg')
edges = cv2.Canny(image,100,200)
cv2.imshow('Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()