

# python
import threading
from time import sleep
from pathlib import Path
from datetime import datetime


# pypi
import cv2
import numpy as np
from numba import jit
from PIL import Image, ImageDraw


@jit
def DrawTextOnFrame(frame, text_y, text_x, position_diff, duration,
                    video_number, username, datetime, video_id, font, color):
    cv2_im_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(cv2_im_rgb)
    drawer = ImageDraw.Draw(pil_image)

    drawer.text(
        (text_y, text_x),
        "Datetime: " + datetime,
        font=font,
        fill=color
    )
    drawer.text(
        (text_y, text_x + position_diff),
        "Video Number: " + str(video_number),
        font=font,
        fill=color
    )
    drawer.text(
        (text_y, text_x + position_diff * 2),
        "Username: " + username,
        font=font,
        fill=color
    )
    drawer.text(
        (text_y, text_x + position_diff * 3),
        "Total Time: " + str(duration) + " seconds",
        font=font,
        fill=color
    )
    drawer.text(
        (text_y, text_x + position_diff * 4),
        "Video ID: " + video_id,
        font=font,
        fill=color
    )
    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)



class VideoRecorder:
    def __init__(self, save_destination, remote_save_destination, stop_flag,
                 video_number, video_id, username, font, color, text_x, text_y,
                 stop_all, overlay_image=None, show_live=False):
        if isinstance(save_destination, Path):
            self.save_destination = save_destination.as_posix()
        else:
            self.save_destination = save_destination

        if isinstance(remote_save_destination, Path):
            self.remote_save_destination = save_destination.as_posix()
        else:
            self.remote_save_destination = save_destination

        self.stop_flag = stop_flag
        self.stop_all = stop_all

        self.video_number = video_number
        self.video_id = video_id
        self.username = username
        self.font = font
        self.color = color
        self.show_live = show_live

        if overlay_image:
            if isinstance(overlay_image, np.ndarray):
                self.overlay_image = overlay_image

            elif isinstance(overlay_image, str):
                self.overlay_image = cv2.imread(overlay_image, cv2.IMREAD_UNCHANGED)

            elif isinstance(overlay_image, Path):
                self.overlay_image = cv2.imread(overlay_image.as_posix(), cv2.IMREAD_UNCHANGED)

            self.overlay_image_height, self.overlay_image_width, _ = self.overlay_image.shape


            # setting up location for overlay image
            self.center_y = self.frame_height // 2
            self.center_x = self.frame_width // 2
            self.top_y = self.center_y - (self.overlay_image_height // 2)
            self.top_x = self.center_x - (self.overlay_image_width // 2)
            self.bottom_y = self.top_y + self.overlay_image_height
            self.bottom_x = self.top_x + self.overlay_image_width


        self.camera = cv2.VideoCapture(0)
        self.resolution = (
            int(self.camera.get(3)),
            int(self.camera.get(4))
        )

        self.frame_width = self.resolution[0]
        self.frame_height = self.resolution[1]

        # this is affecting the performance of the video
        # setting the max physical camera resolution to virtual camera
        # self.camera.set(3, self.resolution[0])
        # self.camera.set(4, self.resolution[1])

        self.video_code = cv2.VideoWriter_fourcc(*'XVID')
        self.output = cv2.VideoWriter(
            self.save_destination,
            self.video_code,
            30.0,
            self.resolution
        )
        self.record = True
        self.video_thread = threading.Thread(target=self.record_video)

        self.active_timer = True
        self.timer_thread = threading.Thread(target=self.timer)

        self.text_y = text_y
        self.text_x = text_x
        self.position_diff = 25


    def timer(self):
        self.duration = 0
        while self.active_timer:
            sleep(1)
            self.duration += 1


    def __start_timer_thread(self):
        self.timer_thread.start()


    def join_video_thread(self):
        self.video_thread.join()


    def record_video(self):
        self.__start_timer_thread()

        while self.record:
            _, frame = self.camera.read()

            if not self.record:
                break

            frame = DrawTextOnFrame(
                frame,
                self.text_y,
                self.text_x,
                self.position_diff,
                self.duration,
                self.video_number,
                self.username,
                datetime.now().strftime("%d.%m.%Y-%H:%M:%S"),
                self.video_id,
                self.font,
                self.color
            )

            if not self.record:
                break

            self.output.write(frame)


            if self.show_live:
                # cv2.namedWindow(live_log_window_name, cv2.WINDOW_GUI_EXPANDED)

                # its making the video very slow, I FIXED THE PROBLEM
                cv2.imshow("live feed", frame)
                result = cv2.waitKey(1)

                if result == 27:
                    # ESC was pressed
                    # close the log
                    self.stop_all[0] = True
                    print("log stopped from ESC")
                    break
            else:
                cv2.waitKey(1)


        self.camera.release()
        self.output.release()
        cv2.destroyAllWindows()

        self.stop_flag[0] = True


    def start_thread(self):
        self.video_thread.start()


    def stop_video_thread(self):
        self.record = False
        self.active_timer = False



if __name__ == '__main__':

    pass