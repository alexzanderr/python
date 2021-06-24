
from MonitorUserLogon.imports import *


def MouseMove(x, y, listener, user_active):
    user_active[0] = True


def MouseScroll(x, y, dx, dy, listener, user_active):
    user_active[0] = True


def MouseClick(x, y, button, pressed, listener, user_active):
    user_active[0] = True


def GetMouseListener(user_active):
    mouse_listener = mouse.Listener()
    mouse_listener.on_click = lambda x, y, button, pressed: MouseClick(
        x, y, button, pressed, listener=mouse_listener, user_active=user_active
    )
    mouse_listener.on_scroll = lambda x, y, dx, dy: MouseScroll(
        x, y, dx, dy, mouse_listener, user_active=user_active
    )
    mouse_listener.on_move = lambda x, y: MouseMove(
        x, y, listener=mouse_listener, user_active=user_active
    )
    return mouse_listener



if __name__ == '__main__':
    # before = time.time()

    # GetMouseListener().start()

    # MainThread()

    # execution_time = time.time() - before
    # execution_time = numbers__.fixed_set_precision_float(execution_time, 2)
    # print(f"computer active time: {execution_time} seconds")
    # print(f"user inactivity: {user_inactivity}")
    # print(f"user active time on computer: {execution_time - user_inactivity:.2f}")
    pass
