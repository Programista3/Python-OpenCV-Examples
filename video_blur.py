import cv2

player = cv2.VideoCapture('media/Bee.mp4')
length = int(player.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
i = 0

while i <= length:
    ret, frame = player.read()
    i += 1
    if ret:
        blur = cv2.blur(frame, (10, 10))
        cv2.imshow('Video', blur)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
player.release()
cv2.waitKey(0)
cv2.destroyAllWindows()