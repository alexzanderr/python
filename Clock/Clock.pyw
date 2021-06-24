
from core.datetime__ import *
from core.algorithms import *
from core.backtracking import *
from core.drive import *
from core.system import *
from core.image import *
from core.json__ import *
from core.numbers__ import *
from core.path__ import *
from core.winapi__ import *
from core.random__ import *
from core.statistics import *
from core.gui.configs import *
from core.gui.objects import *
import os
import subprocess
from core.timezone.timezone import *

background_color = seashell2
foreground_color = gray10
green_color = forest_green

screen_width = 650
screen_height = 1000
left_to_right = 550
up_to_down = 0
window_geometry = (screen_width, screen_height, left_to_right, up_to_down)


app_icon_path = "icons/exec.ico"

clock_window = Tk()
clock_window.title("Clock")
clock_window.geometry("{}x{}+{}+{}".format(*window_geometry))
clock_window.iconbitmap(app_icon_path)
clock_window.resizable(0, 0)
clock_window.config(back=background_color)


chosen_cities = [
    "Europe/Bucharest",
    "Europe/London",
    "Europe/Copenhagen",
    "Asia/Tokyo",
    "Asia/Shanghai",
    "Asia/Dubai",
    "America/New_York"
]

current_time_label = NewLabel(clock_window, "World Clock\n" + "=" * 40, TOP)
config_gui_obj(current_time_label, font=cascadia_code_30_bold, fore=forest_green, back=background_color)

timezones = []
for i in range(len(chosen_cities)):
    # label_text = chosen_cities[i].split("/")[1] + ":"
    # tz = get_current_timezone(chosen_cities[i])

    # label_text = label_text + " " * (21 - len(label_text) - 6) + tz + " (--)"

    time_label = NewLabel(clock_window, "", TOP)
    config_gui_obj(time_label, font=cascadia_code_30_bold, fore=gray10, back=background_color)
    timezones.append(time_label)


timezones_active = 0

def UpdateTimezones():
    global timezones_active

    while timezones_active == 1:
        h = get_current_timezone()
        h = int(h.split(":")[0])

        for city, timezone in zip(chosen_cities, timezones):
            label_text = city.split("/")[1] + ":"
            tz = get_current_timezone(city)

            diff = int(tz.split(":")[0]) - h
            if diff < 0:
                sign = "-"
            else:
                sign = "+"
            diff = abs(diff)

            label_text = label_text + " " * (21 - len(label_text) - 6) + tz + " ({}{})".format(sign, diff)

            timezone.config(text=label_text)

        # print("im active")

        sleep(1)

def UpdateTimezonesThread():
    global timezones_active
    timezones_active = 1

    update_timezones_thread = threading.Thread(target=UpdateTimezones, args=())
    update_timezones_thread.start()

timer_icon = PhotoImage(file='icons/timer.png')
timer_icon = timer_icon.subsample(2, 2)

stopwatch_icon = PhotoImage(file='icons/stopwatch.png')
stopwatch_icon = stopwatch_icon.subsample(2, 2)


from tkinter import messagebox

timer_path = get_python_path() + "/Timer/Timer.pyw"
def OpenTimer():
    if exists(timer_path):
        subprocess.Popen(["pythonw", timer_path])
    else:
        messagebox.showerror("ERROR", "timer.pyw is not located on {}".format(timer_path))


timer_button = NewButton(clock_window, " Timer", OpenTimer, TOP)
config_gui_obj(timer_button, fore=forest_green, back=background_color, font=cascadia_code_30_bold)
timer_button.config(image=timer_icon, compound=LEFT)

stopwatch_path = get_python_path() + "/Stopwatch/Stopwatch.pyw"
def OpenStopwatch():
    if exists(stopwatch_path):
        subprocess.Popen(["pythonw", stopwatch_path])
    else:
        messagebox.showerror("ERROR", "timer.pyw is not located on {}".format(stopwatch_path))


stopwatch_button = NewButton(clock_window, " Stopwatch", OpenStopwatch, TOP)
config_gui_obj(stopwatch_button, fore=forest_green, back=background_color, font=cascadia_code_30_bold)
stopwatch_button.config(image=stopwatch_icon, compound=LEFT)


def BeforeQuiting():
    global timezones_active

    # we need to make sure that the timer thread is closed
    # otherwise we have a lot of bugs
    if timezones_active == 1:
        timezones_active = 0
        sleep(1)

    clock_window.destroy()

UpdateTimezonesThread()
clock_window.protocol("WM_DELETE_WINDOW", BeforeQuiting)
clock_window.mainloop()