import cv2

player = cv2.VideoCapture('media/Bee.mp4')
length = int(player.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
i = 0

while i <= length:
    ret, frame = player.read()
    i += 1
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
player.release()
cv2.waitKey(0)
cv2.destroyAllWindows()