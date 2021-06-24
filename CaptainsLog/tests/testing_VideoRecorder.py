
from time import sleep

import cv2


camera = cv2.VideoCapture(0)
resolution = (int(camera.get(3)), int(camera.get(4)))



# setting the max physical camera resolution to virtual camera
# camera.set(3, resolution[0])
# camera.set(4, resolution[1])

video_code = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter(
    "testing.mkv",
    video_code,
    30.0,
    resolution
)

print("smile :), CTRL+C to stop")
try:
    while True:
        ret, frame = camera.read()
        if ret:

            output.write(frame)

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
except KeyboardInterrupt:
    pass



output.release()
camera.release()

cv2.destroyAllWindows()