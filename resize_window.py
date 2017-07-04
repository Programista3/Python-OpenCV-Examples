import cv2

image = cv2.imread('images/image01.jpg', 1)
cv2.namedWindow('Window', cv2.WINDOW_NORMAL) # Create new window
cv2.resizeWindow('Window', 368, 230) # Resize window
cv2.imshow('Window', image)
cv2.waitKey(0)
cv2.destroyAllWindows()