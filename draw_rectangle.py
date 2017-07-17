import numpy as np
import cv2

image = np.zeros((500, 500, 3), np.uint8)
cv2.rectangle(image, (150, 200), (350, 300), (255,0,0),3)
cv2.imshow('Rectangle', image)
cv2.waitKey(0)