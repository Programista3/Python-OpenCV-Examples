import numpy as np
import cv2

image = np.zeros((500, 500, 3), np.uint8)
cv2.line(image, (0,250), (500,250), (255,0,0), 5)
cv2.imshow('Line', image)
cv2.waitKey(0)