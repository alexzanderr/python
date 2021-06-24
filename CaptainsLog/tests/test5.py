

import cv2


camera = cv2.VideoCapture(0)

camera.set(3, 1280)
camera.set(4, 720)



for _ in range(30000000):
    ret, frame = camera.read()

    cv2.imshow("camera", frame)
    cv2.waitKey(1)


camera.release()
# video_writer.release()
cv2.destroyAllWindows()