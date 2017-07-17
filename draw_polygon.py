import numpy as np
import cv2

image = np.zeros((500, 500), np.uint8)
pts = np.array([[100, 150], [200, 300], [400, 150]], np.int32)
cv2.polylines(image, [pts], True, (255,0,0))
cv2.imshow('Polygon', image)
cv2.waitKey(0)