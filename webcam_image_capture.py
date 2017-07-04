import cv2

cap = cv2.VideoCapture(0) # Create VideoCapture object with default camera (0)

ret, frame = cap.read() # Capture first frame
ret, frame = cap.read() # Capture second frame - sometimes first frame is empty
cap.release() # Release capture when finished
if ret: # ret is False when frame is empty
    cv2.imshow('Webcam', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Frame is empty!')