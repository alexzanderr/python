

from MonitorUserLogon.imports import *


def KeyPress(key, listener, user_active):
    user_active[0] = True


def KeyRelease(key, listener, user_active):
    user_active[0] = True


def GetKeyboardListener(user_active):
    keyboard_listener = keyboard.Listener()
    keyboard_listener.on_press = lambda key: KeyPress(
        key, keyboard_listener, user_active
    )
    keyboard_listener.on_release = lambda key: KeyRelease(
        key, keyboard_listener, user_active
    )
    return keyboard_listener


if __name__ == '__main__':
    # before = time.time()

    # GetKeyboardListener().start()
    # MainThread()

    # execution_time = time.time() - before
    # execution_time = numbers__.fixed_set_precision_float(execution_time, 2)
    # print(f"computer active time: {execution_time} seconds")
    # print(f"user inactivity: {user_inactivity}")
    # print(f"user active time on computer: {execution_time - user_inactivity:.2f}")
    pass