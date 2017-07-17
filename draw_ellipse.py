import numpy as np
import cv2

image = np.zeros((500, 500, 3), np.uint8)
cv2.ellipse(image, (250, 250), (100, 50), 0, 0, 360, 255, -1)
cv2.imshow('Ellipse', image)
cv2.waitKey(0)