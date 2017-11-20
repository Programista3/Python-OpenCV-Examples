import cv2

image = cv2.imread('media/hsv.jpg')
bgr = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
cv2.imshow('BGR', bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()