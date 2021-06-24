
from core.json__ import *
from core.gui.objects import *
from core.gui.configs import *
from time import sleep
import threading
from functools import partial
from core.winapi__ import *
from core import datetime__
from core import system

operating_system = system.get_operating_system()
windows = operating_system == "windows"
linux = operating_system == "linux"
macos = operating_system == "darwin"


from pathlib import Path
remote_appdata_path = r"D:\Alexzander__\PythonApplicationsAppData\Timer\metadata"
remote_appdata_folder = Path(remote_appdata_path)
remote_appdata_folder.mkdir(exist_ok=True)

current_date = datetime__.get_current_date()

current_date_appdata_folder = remote_appdata_folder / current_date
current_date_appdata_folder.mkdir(exist_ok=True)


hours = 0
minutes = 0
seconds = 0

timer_active = 0
timer_freezed = 0


app_icon_path = "icons/timer.ico"

background_color = seashell2
foreground_color = gray10
green_color = forest_green
yellow_color = gold3


display_format = "[ {hours} : {minutes} : {seconds} ]"
zero_zero_zero = display_format.format(hours="00", minutes="00", seconds="00")

timer_window = Tk()
timer_window.title("Timer")
timer_window.geometry("{}x{}+{}+{}".format(
    650,
    700,
    500,
    100
))
timer_window.iconbitmap(app_icon_path)
timer_window.resizable(0, 0)


purpose_title_label = Label(timer_window, height=1, font=cascadia_code_20_bold, text="Timer Purpose")
purpose_title_label.config(back=background_color, fore=forest_green)
purpose_title_label.pack(fill=BOTH, expand=YES)

purpose_textbox = Text(timer_window, height=1, font=cascadia_code_30_bold)
purpose_textbox.config(back=background_color, fore=forest_green)
purpose_textbox.pack_propagate(0)
purpose_textbox.pack(fill=BOTH, expand=YES)




decrement_frame = NewFrame(timer_window, TOP)


# ========== decrement buttons ==================

def decrement_hours():
    global hours

    if timer_active == 0:
        hours -= 1

        if hours < 0:
            hours = 99

        str_seconds = str(seconds)
        str_minutes = str(minutes)
        str_hours = str(hours)

        if minutes < 10:
            str_minutes = "0" + str(minutes)
        if seconds < 10:
            str_seconds = "0" + str(seconds)
        if hours < 10:
            str_hours = "0" + str(hours)

        timer_label.config(text=display_format.format(hours=str_hours, minutes=str_minutes, seconds=str_seconds))


def decrement_minutes():
    global minutes

    if timer_active == 0:

        minutes -= 1

        if minutes < 0:
            minutes = 59

        str_seconds = str(seconds)
        str_minutes = str(minutes)
        str_hours = str(hours)

        if minutes < 10:
            str_minutes = "0" + str(minutes)
        if seconds < 10:
            str_seconds = "0" + str(seconds)
        if hours < 10:
            str_hours = "0" + str(hours)

        timer_label.config(text=display_format.format(hours=str_hours, minutes=str_minutes, seconds=str_seconds))

def decrement_seconds():
    global seconds

    if timer_active == 0:
        seconds -= 1

        if seconds < 0:
            seconds = 59

        str_seconds = str(seconds)
        str_minutes = str(minutes)
        str_hours = str(hours)

        if minutes < 10:
            str_minutes = "0" + str(minutes)
        if seconds < 10:
            str_seconds = "0" + str(seconds)
        if hours < 10:
            str_hours = "0" + str(hours)

        timer_label.config(text=display_format.format(hours=str_hours, minutes=str_minutes, seconds=str_seconds))


hours_decrement_button = NewButton(decrement_frame, "H--", decrement_hours, LEFT)
config_gui_obj(hours_decrement_button, font=cascadia_code_20, fore=foreground_color, back=background_color)

minutes_decrement_button = NewButton(decrement_frame, "M--", decrement_minutes, LEFT)
config_gui_obj(minutes_decrement_button, font=cascadia_code_20, fore=foreground_color, back=background_color)

seconds_decrement_button = NewButton(decrement_frame, "S--", decrement_seconds, LEFT)
config_gui_obj(seconds_decrement_button, font=cascadia_code_20, fore=foreground_color, back=background_color)


# ========== decrement buttons ==================

timer_label = NewLabel(timer_window, zero_zero_zero, TOP)
config_gui_obj(timer_label, back=background_color, fore=foreground_color, font=consolas_50_bold)


increment_frame = NewFrame(timer_window, TOP)

# ========== increment buttons =================
def increment_hours():
    global hours

    if timer_active == 0:

        hours += 1

        if hours > 99:
            hours = 0

        str_hours = str(hours)
        str_minutes = str(minutes)
        str_seconds = str(seconds)

        if minutes < 10:
            str_minutes = "0" + str(minutes)
        if seconds < 10:
            str_seconds = "0" + str(seconds)
        if hours < 10:
            str_hours = "0" + str(hours)

        timer_label.config(text=display_format.format(hours=str_hours, minutes=str_minutes, seconds=str_seconds))


def increment_minutes():
    global minutes

    if timer_active == 0:
        minutes += 1

        if minutes > 59:
            minutes = 0

        str_seconds = str(seconds)
        str_minutes = str(minutes)
        str_hours = str(hours)

        if minutes < 10:
            str_minutes = "0" + str(minutes)
        if seconds < 10:
            str_seconds = "0" + str(seconds)
        if hours < 10:
            str_hours = "0" + str(hours)

        timer_label.config(text=display_format.format(hours=str_hours, minutes=str_minutes, seconds=str_seconds))

def increment_seconds():
    global seconds
    if timer_active == 0:

        seconds += 1

        if seconds > 59:
            seconds = 0

        str_seconds = str(seconds)
        str_minutes = str(minutes)
        str_hours = str(hours)

        if minutes < 10:
            str_minutes = "0" + str(minutes)
        if seconds < 10:
            str_seconds = "0" + str(seconds)
        if hours < 10:
            str_hours = "0" + str(hours)

        timer_label.config(text=display_format.format(hours=str_hours, minutes=str_minutes, seconds=str_seconds))

hours_increment_button = NewButton(increment_frame, "H++", increment_hours, LEFT)
config_gui_obj(hours_increment_button, font=cascadia_code_20, fore=foreground_color, back=background_color)

minutes_increment_button = NewButton(increment_frame, "M++", increment_minutes, LEFT)
config_gui_obj(minutes_increment_button, font=cascadia_code_20, fore=foreground_color, back=background_color)

seconds_increment_button = NewButton(increment_frame, "S++", increment_seconds, LEFT)
config_gui_obj(seconds_increment_button, font=cascadia_code_20, fore=foreground_color, back=background_color)


# ========== increment buttons ==================



def TimerIteration(pause_interval=1):
    global seconds, minutes, hours, timer_label, display_format, timer_active

    time_started = datetime__.get_current_time()
    current_date = datetime__.get_current_date()

    while timer_active == 1:
        if timer_freezed == 1:
            sleep(0.1)
            continue

        str_seconds = str(seconds)
        str_minutes = str(minutes)
        str_hours = str(hours)

        if minutes < 10:
            str_minutes = "0" + str(minutes)
        if seconds < 10:
            str_seconds = "0" + str(seconds)
        if hours < 10:
            str_hours = "0" + str(hours)

        timer_label.config(text=display_format.format(hours=str_hours, minutes=str_minutes, seconds=str_seconds))

        if seconds == 0:
            if minutes > 0:
                minutes -= 1
                seconds = 60
            elif minutes == 0:
                if hours > 0:
                    hours -= 1
                    minutes = 59
                    seconds = 60

        elif minutes == 0:
            if hours > 0 and seconds == 0:
                hours -= 1
                minutes = 59

        sleep(pause_interval)

        seconds -= 1


        if seconds == 0 and minutes == 0 and hours == 0:

            time_finished = datetime__.get_current_time()

            timer_label.config(text=zero_zero_zero)
            start_button.config(text="START", fore=green_color)

            orig_hours = str(original_values[0])
            orig_minutes = str(original_values[1])
            orig_seconds = str(original_values[2])

            if original_values[0] < 10:
                orig_hours = "0" + orig_hours
            if original_values[1] < 10:
                orig_minutes = "0" + orig_minutes
            if original_values[2]  < 10:
                orig_seconds = "0" + orig_seconds


            purpose = purpose_textbox.get(1.0, END)
            purpose = purpose.strip()
            if purpose != "\n" and purpose != "":
                windows_notification(
                    "Timer",
                    "PURPOSE:\n{}\n{}:{}:{} => FINISHED!".format(purpose, orig_hours, orig_minutes, orig_seconds),
                    5,
                    "icons/timer.ico",
                    1)
            else:
                purpose = None
                windows_notification(
                    "Timer",
                    "{}:{}:{} => FINISHED!".format(orig_hours, orig_minutes, orig_seconds),
                    5,
                    "icons/timer.ico",
                    1)

            # metadata
            purpose = purpose.replace("_", "").strip()
            countdown = f"{orig_hours}-{orig_minutes}-{orig_seconds}"
            result_timer_metadata = {
                "purpose": purpose,
                "time_started": time_started,
                "time_finished": time_finished,
                "date": current_date,
                "countdown": countdown
            }

            result_timer_metadata_file = current_date_appdata_folder / f"timer_{countdown}_{purpose}.json"
            if result_timer_metadata_file.exists():
                existent_json = read_json_from_file(result_timer_metadata_file)

                if isinstance(existent_json, list):
                    existent_json.append(result_timer_metadata)

                    result_timer_metadata = existent_json
                    del existent_json

                elif isinstance(existent_json, dict):
                    result_timer_metadata = [existent_json, result_timer_metadata]


            write_json_to_file(result_timer_metadata, result_timer_metadata_file)


            # saving to app data remote location

            timer_active = 0
            pause_button.pack_forget()

    purpose_title_label.config(text="Timer Purpose")
    purpose_textbox.config(state=NORMAL)
    purpose_textbox.delete(1.0, END)

    hours = 0
    seconds = 0
    minutes = 0







def ClearTimer():
    global timer_active, timer_label, hours, seconds, minutes

    if timer_active == 0:
        hours = 0
        minutes = 0
        seconds = 0
        timer_label.config(text=zero_zero_zero)


clear_frame = NewFrame(timer_window, TOP)


def ClearHours():
    global hours, timer_active

    if timer_active == 0:
        hours = 0

        str_minutes = str(minutes)
        if minutes < 10:
            str_minutes = "0" + str_minutes

        str_seconds = str(seconds)
        if seconds < 10:
            str_seconds = "0" + str_seconds

        timer_label.config(text=display_format.format(hours="00", minutes=str_minutes, seconds=str_seconds))


def ClearMinutes():
    global minutes, timer_active

    if timer_active == 0:
        minutes = 0

        str_hours = str(hours)
        if hours < 10:
            str_hours = "0" + str_hours

        str_seconds = str(seconds)
        if seconds < 10:
            str_seconds = "0" + str_seconds


        timer_label.config(text=display_format.format(hours=str_hours, minutes="00", seconds=str_seconds))

def ClearSeconds():
    global seconds, timer_active

    if timer_active == 0:
        seconds = 0

        str_minutes = str(minutes)
        if minutes < 10:
            str_minutes = "0" + str_minutes

        str_hours = str(hours)
        if hours < 10:
            str_hours = "0" + str_hours

        timer_label.config(text=display_format.format(hours=str_hours, minutes=str_minutes, seconds="00"))


# ================= clear butons ========================
clear_hours = NewButton(clear_frame, "clear\n hours ", ClearHours, LEFT)
config_gui_obj(clear_hours, font=cascadia_code_20, fore=yellow_color, back=background_color)

clear_minutes = NewButton(clear_frame, "clear\nminutes", ClearMinutes, LEFT)
config_gui_obj(clear_minutes, font=cascadia_code_20, fore=yellow_color, back=background_color)

clear_seconds = NewButton(clear_frame, "clear\nseconds", ClearSeconds, LEFT)
config_gui_obj(clear_seconds, font=cascadia_code_20, fore=yellow_color, back=background_color)


clear_timer = NewButton(clear_frame, "CLEAR", ClearTimer, LEFT)
config_gui_obj(clear_timer, font=cascadia_code_40, fore=yellow_color, back=background_color)

# ================= clear butons ========================




import threading

pause_interval = 1

original_values = None

def StartTimer(self):
    global timer_active, seconds, minutes, hours, timer_freezed, original_values

    if seconds < 0:
        seconds = 0
    if minutes < 0:
        minutes = 0
    if hours < 0:
        hours = 0

    if seconds == 0 and minutes == 0 and hours == 0:
        return

    if timer_active == 0:
        timer_active = 1

        text = purpose_textbox.get(1.0, END)
        text = text.strip()
        if text != "\n" and text != "":
            len_text = len(text)
            if len_text > 28:
                text = text[:29]

            purpose = text.strip()
            if 1 <= len_text <= 25:
                text = " " + text.strip() + " "
                text = text.center(28, "_")
            elif len_text < 28:
                text = text.strip()
                text = text.center(28)

            purpose_textbox.delete(1.0, END)
            purpose_textbox.insert(0.0, text)

        else:
            purpose_title_label.config(text="Timer Purpose (None)")
            purpose = "None"

        purpose_textbox.config(state=DISABLED)


        pause_button.pack()
        # clear_frame.pack_forget()

        # print(hours, minutes, seconds)

        original_values = (hours, minutes, seconds)

        countdown_thread = threading.Thread(target=TimerIteration, args=(pause_interval, ))
        countdown_thread.start()

        self.config(text="STOP", font=cascadia_code_40, fore=indian_red)

        if seconds < 0:
            seconds = 0
        if minutes < 0:
            minutes = 0
        if hours < 0:
            hours = 0

    elif timer_active == 1:
        # print(hours, minutes, seconds)
        timer_active = 0
        # clear_frame.pack/()
        hours = 0
        minutes = 0
        seconds = 0

        purpose_textbox.config(state=NORMAL)
        purpose_title_label.config(text="Timer Purpose")
        purpose_textbox.delete(1.0, END)

        original_values = None

        if timer_freezed == 1:
            timer_freezed = 0

        timer_label.config(text=zero_zero_zero)
        self.config(text="START", font=cascadia_code_40, fore=green_color)
        pause_button.pack_forget()
        continue_button.pack_forget()


start_button = NewButton(timer_window, "START", "", LEFT)
config_gui_obj(start_button, font=cascadia_code_40, fore=forest_green, back=background_color)
start_button.config(command=partial(StartTimer, start_button))

def PauseTimer():
    global timer_freezed
    timer_freezed = 1
    pause_button.pack_forget()
    continue_button.pack()

def ContinueTimer():
    global timer_freezed
    timer_freezed = 0
    continue_button.pack_forget()
    pause_button.pack()


pause_button = NewButton(timer_window, "PAUSE", PauseTimer, RIGHT)
config_gui_obj(pause_button, font=cascadia_code_40, fore=yellow_color, back=background_color)
pause_button.pack_forget()

continue_button = NewButton(timer_window, "CONTINUE", ContinueTimer, RIGHT)
config_gui_obj(continue_button, font=cascadia_code_40, fore=yellow_color, back=background_color)
continue_button.pack_forget()


def BeforeQuiting():
    global timer_active, timer_freezed

    # we need to make sure that the timer thread is closed
    # otherwise we have a lot of bugs
    if timer_active == 1:
        timer_freezed = 0
        timer_active = 0
        sleep(1)

    timer_window.destroy()

timer_window.protocol("WM_DELETE_WINDOW", BeforeQuiting)


def EnterEvent(event_data=None):
    StartTimer(start_button)

purpose_textbox.bind("<Return>", EnterEvent)

timer_window.mainloop()