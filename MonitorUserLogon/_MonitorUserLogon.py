
"""
    timer for activity (keys are pressed or mouse is clicked or mouse is moved or mouse is scrolled)
    timer for inactivity (keys are not pressed and mouse mouse is not clicked and mouse is not moved)

    key listener
    mouse listener
    both from pynput

    total time at pc == activity - inactivity
"""

from MonitorUserLogon.imports import *
from MonitorUserLogon.MouseActivity import GetMouseListener
from MonitorUserLogon.KeyboardActivity import GetKeyboardListener
from MonitorUserLogon.analytics import SubprocessPlot



__appname__ = "MonitorUserLogon"


logger_MonitorUserLogon = logging__.Loggerr(
    name="_MonitorUserLogon.py",
    file_handler=file_handler_MonitorUserLogon,
    stream_handler=stream_handler_MonitorUserLogon
)
logger_MonitorUserLogon.info(f"application {__appname__} loaded.")



delay = 3

user_activity = 0
user_inactivity = 0
user_active = [False]


def CountInactivity():
    global user_active, user_inactivity

    for second in range(delay):
        print(f"inactivity: {second}")
        time.sleep(1)
        if user_active[0]:
            print("user active")
            return

    user_active[0] = False
    # user inactivity only activates after 5 seconds of inactivity
    print()
    while True:
        if user_active[0]:
            break
        user_inactivity += 0.1
        print(f"user inactivity: {user_inactivity}", end="\r")
        time.sleep(0.1)

    print()
    user_active[0] = False


results_folder = Path("results")
if not results_folder.exists():
    results_folder.mkdir()


remote_results_folder = Path(r"D:\Alexzander__\PythonApplicationsAppData\MonitorUserLogon\results")
if not remote_results_folder.exists():
    remote_results_folder.mkdir()


def SaveMetadata(result_metadata_file, metadata):
    if not result_metadata_file.exists():
        result_metadata_file.write_text(json.dumps(
            metadata,
            indent=4
        ))
        print(f"file: {result_metadata_file.as_posix()} created with:\n")
        json__.pretty_print(metadata)

    else:
        existent_metadata = json.loads(result_metadata_file.read_text())
        existent_metadata["total"] += metadata["total"]
        existent_metadata["total"] = numbers__.fixed_set_precision_float(existent_metadata["total"], 2)

        existent_metadata["online"] += metadata["online"]
        existent_metadata["online"] = numbers__.fixed_set_precision_float(existent_metadata["online"], 2)

        existent_metadata["offline"] += metadata["offline"]
        existent_metadata["offline"] = numbers__.fixed_set_precision_float(existent_metadata["offline"], 2)

        existent_metadata["closed_at"] = metadata["closed_at"]

        result_metadata_file.write_text(json.dumps(
            existent_metadata,
            indent=4
        ))

        print(f"file: {result_metadata_file.as_posix()} updated with:\n")
        json__.pretty_print(existent_metadata)



def MonitorUserLogon():
    before = time.time()

    global user_active, user_inactivity

    mouse_listener = GetMouseListener(user_active)
    keyboard_listener = GetKeyboardListener(user_active)


    mouse_listener.start()
    keyboard_listener.start()
    while True:
        try:
            if not user_active[0]:
                CountInactivity()
            user_active[0] = False

            time.sleep(0.2)


        except KeyboardInterrupt:
            mouse_listener.stop()
            keyboard_listener.stop()
            break


    after = time.time()
    execution_time = after - before
    execution_time = numbers__.fixed_set_precision_float(execution_time, 2)

    system.clearscreen()
    print(f"\n\ncomputer active time: [ {execution_time} ] seconds")

    user_inactivity = numbers__.fixed_set_precision_float(user_inactivity, 2)
    print(f"user inactivity: [ {user_inactivity} ] seconds")

    user_active_time = numbers__.fixed_set_precision_float(execution_time - user_inactivity, 2)
    print(f"user active time on computer: [ {user_active_time:.2f} ] seconds")

    metadata = {
        "started_at": datetime__.timestamp_to_datetime(before),
        "closed_at": datetime__.timestamp_to_datetime(after),

        "total": execution_time,
        "online": user_active_time,
        "offline": user_inactivity,
        "unit": "seconds"
    }

    file_name = datetime__.get_current_date() + "_metadata.json"

    # local storage
    result_metadata_file = results_folder / file_name
    SaveMetadata(result_metadata_file, metadata)

    # remote storage
    remote_result_metadata_file = remote_results_folder / file_name
    SaveMetadata(remote_result_metadata_file, metadata)

    SubprocessPlot()

    
if __name__ == "__main__":
    MonitorUserLogon()
