
import os
import json
from time import sleep
from core.gui.objects import *
from core.gui.configs import *

__appname__ = "WorkoutCounter"

# app data
python_applications_appdata_path = r"D:\Alexzander__\PythonApplicationsAppData"
workout_counter_app_data_path = os.path.join(python_applications_appdata_path, __appname__)

# creating the folder of this project
if not os.path.exists(workout_counter_app_data_path):
    os.makedirs(workout_counter_app_data_path)


bike_data_path = os.path.join(workout_counter_app_data_path, "bike_data.json")
workout_data_path = os.path.join(workout_counter_app_data_path, "workout_data.json")

bike_data = json.loads(open(bike_data_path).read())
workout_data = json.loads(open(workout_data_path).read())

def UpdateBikeData():
    with open(bike_data_path, "w+", encoding="utf-8") as file:
        file.truncate(0)
        file.write(json.dumps(bike_data, indent=4))

def UpdateWorkoutData():
    with open(workout_data_path, "w+", encoding="utf-8") as file:
        file.truncate(0)
        file.write(json.dumps(workout_data, indent=4))

app_icon_path = "icons/exec.ico"

# window configs
window_application = Tk()
window_application.title("Workout-Counter")
window_application.geometry("{}x{}+{}+{}".format(
    500 + 300,
    500 + 200,
    100,
    100
))
window_application.iconbitmap(app_icon_path)

# ====================== workouts =================================
workout_label = NewLabelWithBorder(
    window_application,
    "Workout_Sessions: {}".format(workout_data["sessions"]),
    TOP
)
config_gui_obj(workout_label, font=consolas_50_bold, fore=gold, back=gray32)

workouts_frame = NewFrame(window_application, TOP)

def IncremenetWorkouts():
    workout_data["sessions"] += 1
    UpdateWorkoutData()
    workout_label.config(text="Workout_Sessions: {}".format(workout_data["sessions"]))

increment_workouts_button = NewButton(
    workouts_frame,
    "sessions++",
    IncremenetWorkouts,
    LEFT
)
config_gui_obj(increment_workouts_button, font=consolas_30_bold, fore=gold, back=gray32)

def DecrementWorkouts():
    workout_data["sessions"] -= 1
    UpdateWorkoutData()
    workout_label.config(text="Workout_Sessions: {}".format(workout_data["sessions"]))

decrement_workouts_button = NewButton(
    workouts_frame,
    "sessions--",
    DecrementWorkouts,
    RIGHT
)
config_gui_obj(decrement_workouts_button, font=consolas_30_bold, fore=gold, back=gray32)
# ===================== workouts =================================



# ====================== rides =================================
rides_label = NewLabelWithBorder(
    window_application,
    "Bike_Rides: {}".format(bike_data["rides"]),
    TOP

)
config_gui_obj(rides_label, font=consolas_50_bold, fore=gold, back=gray32)

rides_frame = NewFrame(window_application, TOP)

def IncrementRides():
    bike_data["rides"] += 1
    UpdateBikeData()
    rides_label.config(text="Bike_Rides: {}".format(bike_data["rides"]))

increment_rides_button = NewButton(
    rides_frame,
    "rides++",
    IncrementRides,
    LEFT
)
config_gui_obj(increment_rides_button, font=consolas_30_bold, fore=gold, back=gray32)

def DecrementRides():
    bike_data["rides"] -= 1
    UpdateBikeData()
    rides_label.config(text="Bike_Rides: {}".format(bike_data["rides"]))

decrement_rides_button = NewButton(
    rides_frame,
    "rides--",
    DecrementRides,
    RIGHT
)
config_gui_obj(decrement_rides_button, font=consolas_30_bold, fore=gold, back=gray32)
# ====================== rides =================================


# ====================== crashes =================================
crashes_label = NewLabelWithBorder(
    window_application,
    "Bike_Crashes: {}".format(bike_data["crashes"]),
    TOP
)
config_gui_obj(crashes_label, font=consolas_50_bold, fore=indian_red, back=gray32)

crashes_frame = NewFrame(window_application, TOP)

def IncrementCrashes():
    bike_data["crashes"] += 1
    UpdateBikeData()
    crashes_label.config(text="Bike_Crashes: {}".format(bike_data["crashes"]))

increment_crashes_button = NewButton(
    crashes_frame,
    "crashes++",
    IncrementCrashes,
    LEFT
)
config_gui_obj(increment_crashes_button, font=consolas_30_bold, fore=indian_red, back=gray32)

def DecrementCrashes():
    bike_data["crashes"] -= 1
    UpdateBikeData()
    crashes_label.config(text="Bike_Crashes: {}".format(bike_data["crashes"]))

decrement_crashes_button = NewButton(
    crashes_frame,
    "crashes--",
    DecrementCrashes,
    RIGHT
)
config_gui_obj(decrement_crashes_button, font=consolas_30_bold, fore=indian_red, back=gray32)
# ====================== rides =================================

# run
window_application.mainloop()