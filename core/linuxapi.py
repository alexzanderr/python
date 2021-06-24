

import subprocess
from string import Template

notify_send_template = Template(
    "notify-send '${title}' '${message}' --icon=${icon_path}"
)

notify_send_without_icon_template = Template(
    "notify-send '${title}' '${message}'"
)



# notify-send '202020Rule' 'ITS TIME NOW !!!' --icon=/home/alexzander/Alexzander__/programming/python/202020_order/assets/icons/202020-order-icon.png

def linux_notification(title, message, icon_path=None):
    if icon_path:
        subprocess.call(notify_send_template.safe_substitute(
            title=title,
            message=message,
            icon_path=icon_path
        ), shell=True)
    else:
        subprocess.call(notify_send_without_icon_template.safe_substitute(
            title=title,
            message=message,
        ), shell=True)



if __name__ == '__main__':
    linux_notification(
        "title from code",
        "message from code",
        "/home/alexzander/Alexzander__/programming/python/202020_order/assets/icons/202020-order-icon.png"
    )