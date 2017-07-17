import numpy as np
import cv2

image = np.zeros((500, 500, 3), np.uint8)
cv2.circle(image, (250, 250), 50, (255,0,0), -1)
cv2.imshow('Circle', image)
cv2.waitKey(0)