
from core.gui.objects import *
from core.gui.configs import *
from time import sleep
import threading
from functools import partial
from core.winapi__ import *
from core.aesthetics import *
from core.json__ import *
from core.datetime__ import get_current_date, get_current_time

from pathlib import Path
remote_appdata_path = r"D:\Alexzander__\PythonApplicationsAppData\Stopwatch\metadata"
remote_appdata_folder = Path(remote_appdata_path)
remote_appdata_folder.mkdir(exist_ok=True, parents=True)


current_date = get_current_date()

current_date_appdata_folder = remote_appdata_folder / current_date
current_date_appdata_folder.mkdir(exist_ok=True)


app_icon_path = "icons/stopwatch.ico"

background_color = seashell2
foreground_color = gray10
green_color = forest_green


display_format = "[ {hours} : {minutes} : {seconds} ]"
zero_zero_zero = display_format.format(hours="00", minutes="00", seconds="00")

screen_width = 650
screen_height = 400
left_to_right = 550
up_to_down = 100
window_geometry = (screen_width, screen_height, left_to_right, up_to_down)


stopwatch_window = Tk()
stopwatch_window.title("Stopwatch")
stopwatch_window.geometry("{}x{}+{}+{}".format(*window_geometry))
stopwatch_window.iconbitmap(app_icon_path)
stopwatch_window.resizable(0, 0)


purpose_title_label = Label(stopwatch_window, height=1, font=cascadia_code_20_bold, text="Stopwatch Purpose")
purpose_title_label.config(back=background_color, fore=forest_green)
purpose_title_label.pack(fill=BOTH, expand=YES)

purpose_textbox = Text(stopwatch_window, height=1, font=cascadia_code_30_bold)
purpose_textbox.config(back=background_color, fore=forest_green)
purpose_textbox.pack_propagate(0)
purpose_textbox.pack(fill=BOTH, expand=YES)

stopwatch_label = NewLabel(stopwatch_window, zero_zero_zero, TOP)
config_gui_obj(stopwatch_label, back=background_color, fore=foreground_color, font=consolas_40_bold)
stopwatch_label.config(height=2)


reset_pressed = 0
stopwatch_active = 0
stopwatch_freezed = 0

def SaveMetadata(result_stopwatch_metadata, total_time, purpose):
    result_stopwatch_metadata_file = current_date_appdata_folder / f"stopwatch_{total_time}_{purpose}.json"
    if result_stopwatch_metadata_file.exists():
        existent_json = read_json_from_file(result_stopwatch_metadata_file)

        if isinstance(existent_json, list):
            existent_json.append(result_stopwatch_metadata)

            result_stopwatch_metadata = existent_json
            del existent_json

        elif isinstance(existent_json, dict):
            result_stopwatch_metadata = [existent_json, result_stopwatch_metadata]

    write_json_to_file(result_stopwatch_metadata, result_stopwatch_metadata_file)


seconds = 0
minutes = 0
hours = 0
time_started = None
purpose = None

def StopWatchIteration():
    global stopwatch_active, display_format, reset_pressed, \
    stopwatch_freezed, seconds, minutes, hours, time_started

    ResetHoursMinutesSeconds()

    time_started = get_current_time()
    while 1:
        if stopwatch_freezed == 1:
            sleep(0.1)
            continue

        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            seconds = 0
            minutes = 0
            hours += 1

        str_seconds = str(seconds)
        str_minutes = str(minutes)
        str_hours = str(hours)

        if minutes < 10:
            str_minutes = "0" + str_minutes
        if seconds < 10:
            str_seconds = "0" + str_seconds
        if hours < 10:
            str_hours = "0" + str_hours

        stopwatch_label.config(text=display_format.format(hours=str_hours, minutes=str_minutes, seconds=str_seconds))

        if stopwatch_active == 0:
            break

        sleep(1)

        if stopwatch_active == 0:
            break

        if reset_pressed:
            seconds = 0
            minutes = 0
            hours = 0
            reset_pressed = 0

        if stopwatch_active == 0:
            break

        seconds += 1

    # metadata
    time_finished = get_current_time()

    total_time = f"{hours}-{minutes}-{seconds}"
    result_stopwatch_metadata = {
        "purpose": purpose,
        "time_started": time_started,
        "time_finished": time_finished,
        "date": current_date,
        "stopwatch": total_time
    }

    SaveMetadata(
        result_stopwatch_metadata,
        total_time,
        purpose
    )



def ResetStopwatch():
    global display_format, stopwatch_active, reset_pressed
    reset_pressed = 1
    display_format = "[ {hours} : {minutes} : {seconds} ]"
    stopwatch_label.config(text=zero_zero_zero)


def StartButtonFunction(self):
    global stopwatch_active, reset_button, purpose

    if stopwatch_active == 0:
        stopwatch_active = 1

        purpose = purpose_textbox.get(1.0, END).strip()
        text = purpose[:]
        if text != "\n" and text != "":
            len_text = len(text)
            if len_text > 28:
                text = text[:29]

            text = text.strip()
            if 1 <= len_text <= 25:
                text = " " + text.strip() + " "
                text = text.center(28, "_")
            elif len_text < 28:
                text = text.strip()
                text = text.center(28)

            purpose_textbox.delete(1.0, END)
            purpose_textbox.insert(0.0, text)

        else:
            purpose_title_label.config(text="Stopwatch Purpose (None)")
            text = "None"

        windows_notification(
            "Stopwatch",
            "JUST STARTED!\n\nPURPOSE:\n{}".format(text),
            5,
            "icons/stopwatch.ico",
            1
        )

        purpose_textbox.config(state=DISABLED)

        stopwatch_label.config(font=consolas_40_bold)

        stopwatch_thread = threading.Thread(target=StopWatchIteration, args=())
        stopwatch_thread.start()

        self.config(text="STOP", font=consolas_40_bold, fore=indian_red)
        reset_button.pack(fill=BOTH, expand=YES)
        pause_button.pack(fill=BOTH, expand=YES)

        stopwatch_window.geometry("{}x{}".format(screen_width, screen_height + 200))

        reset_button.pack()
        pause_button.pack()


    elif stopwatch_active == 1:
        text = purpose_textbox.get(1.0, END).strip()
        text = text.replace("_", "").strip()
        stopwatch_active = 0



        stopwatch_label.config(text=zero_zero_zero, font=consolas_40_bold)
        self.config(text="START", fore=green_color)

        purpose_textbox.config(state=NORMAL)
        purpose_textbox.delete(1.0, END)
        purpose_title_label.config(text="Stopwatch Purpose")

        stopwatch_window.geometry("{}x{}".format(screen_width, screen_height))

        reset_button.pack_forget()
        pause_button.pack_forget()

        sleep(1)


def ResetHoursMinutesSeconds():
    global hours, minutes, seconds
    hours = 0
    minute = 0
    seconds = 0


def PauseStopwatch():
    global stopwatch_freezed, pause_button
    if stopwatch_freezed == 1:
        stopwatch_freezed = 0
        pause_button.config(text="PAUSE")
    else:
        stopwatch_freezed = 1
        pause_button.config(text="CONTINUE")


buttons_frame = NewFrame(stopwatch_window, BOTTOM)
buttons_frame.config(back=background_color)
buttons_frame.pack(fill=BOTH, expand=YES)

start_button = NewButton(buttons_frame, "START", "", TOP)
config_gui_obj(start_button, back=background_color, fore=green_color, font=consolas_40_bold)
start_button.config(command=partial(StartButtonFunction, start_button))
start_button.pack(fill=BOTH, expand=YES)

reset_button = NewButton(buttons_frame, "RESET", ResetStopwatch, TOP)
config_gui_obj(reset_button, back=background_color, fore=gold2, font=consolas_40_bold)
reset_button.pack(fill=BOTH, expand=YES)

reset_button.pack_forget()

pause_button = NewButton(buttons_frame, "PAUSE", PauseStopwatch, TOP)
config_gui_obj(pause_button, back=background_color, fore=gold2, font=consolas_40_bold)
pause_button.pack(fill=BOTH, expand=YES)
pause_button.pack_forget()


def BeforeQuiting():
    global stopwatch_active

    # we need to make sure that the timer thread is closed
    # otherwise we have a lot of bugs
    if stopwatch_active == 1:
        stopwatch_active = 0
        sleep(1)

        # time_finished = get_current_time()


        # total_time = f"{hours}-{minutes}-{seconds}"
        # result_stopwatch_metadata = {
        #     "purpose": purpose,
        #     "time_started": time_started,
        #     "time_finished": time_finished,
        #     "date": current_date,
        #     "stopwatch": total_time
        # }

        # SaveMetadata(
        #     result_stopwatch_metadata,
        #     total_time,
        #     purpose
        # )

        # ResetHoursMinutesSeconds()




    stopwatch_window.destroy()

stopwatch_window.protocol("WM_DELETE_WINDOW", BeforeQuiting)


stopwatch_window.config(background=background_color)


def EnterEvent(event_data=None):
    StartButtonFunction(start_button)

purpose_textbox.bind("<Return>", EnterEvent)

stopwatch_window.mainloop()