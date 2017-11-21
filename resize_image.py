import cv2

image = cv2.imread('media/Leaves.jpg')
height, width, channels = image.shape
resize = cv2.resize(image,(int(0.5*width), int(0.5*height)),interpolation=cv2.INTER_CUBIC)
cv2.imshow('Image', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()