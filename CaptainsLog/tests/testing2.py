
import os
import cv2

cap = cv2.VideoCapture(0)

# Get the Default resolutions
frame_width = int(cap.get(3))
print(frame_width)
frame_height = int(cap.get(4))
print(frame_height)

# Define the codec and filename.
out = cv2.VideoWriter(
    'output.mkv',
    cv2.VideoWriter_fourcc(*"XVID"),
    30.0,
    (frame_width,frame_height)
)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        # write the  frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

# os.system("vlc {}".format('output.avi'))