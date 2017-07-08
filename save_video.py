import cv2

cap = cv2.VideoCapture(0)

writer = cv2.VideoWriter('media/video.avi', -1, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        writer.write(frame)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print('Frame is empty!')
cap.release()
writer.release()
cv2.destroyAllWindows()