import cv2

image = cv2.imread('media/Leaves.jpg')
height, width, channels = image.shape

M = cv2.getRotationMatrix2D((width/2,height/2),90,1)
dst = cv2.warpAffine(image,M,(width,height))
cv2.imshow('Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()