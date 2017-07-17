import numpy as np
import cv2

image = np.zeros((400, 600, 3), np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'Text on image', (50, 200), font, 2, (255, 255, 255), 2)
cv2.imshow('Text', image)
cv2.waitKey(0)