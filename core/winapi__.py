
"""
    core/__winapi.py
    useful windows api file

    author:@alexzander
"""

import platform
operating_system = platform.system().lower()
windows = operating_system == "windows"

# 3rd party
if windows:
    from win10toast import ToastNotifier  # pip install win10toast




def windows_notification(
    title,
    message,
    duration,
    icon,
    threaded=True
):
    ToastNotifier().show_toast(
        title=title,
        msg=message,
        duration=duration,
        icon_path=icon,
        threaded=threaded
    )



# TESTING
if __name__ == '__main__':
    pass