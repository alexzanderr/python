
from core.gui.objects import *
from core.gui.configs import *
import pyperclip
from core.system import *
from time import sleep
import threading
from concurrent.futures import ThreadPoolExecutor

background = seashell2
foreground = brown4


appicon_path = "icons/exec.ico"

window_application = Tk()
window_application.title("AutoQuotes")
window_application.geometry("{}x{}+{}+{}".format(
    1600,
    900,
    200,
    100
))
window_application.iconbitmap(appicon_path)
# window_application.resizable(0, 0)

information_label = Label(window_application, text="PASTE TEXT TO INSERT QUOTES")
# information_label.pack_propagate(0)
information_label.config(height=2, width=100)
config_gui_obj(information_label, font=cascadia_code_20, back=background, fore=forest_green)
information_label.pack()


textbox = Text(window_application, width=100, height=20, font=cascadia_code_20)
textbox.config(back=background)
textbox.pack_propagate(0)
textbox.pack(pady=20)

# print(textbox)

def ClearTextbox():
    textbox.delete(1.0, END)



clear_button = NewButton(window_application, "CLEAR", ClearTextbox, LEFT)
clear_button.pack_propagate(0)
config_gui_obj(clear_button, font=cascadia_code_20, fore=foreground, back=background)


app_active = 0

def Clear():
    global information_label, textbox
    while 1:
        sleep(3)
        if information_label.cget("text") != "":
            information_label.config(text="")
        # text = textbox.get(1.0, END)
        # if text != "" or text != "\n":
        #     ClearTextbox()


def ClearLabelThread():
    clear_thread = threading.Thread(target=Clear, args=())
    clear_thread.start()

def ConvertCode():
    global textbox, information_label
    text = textbox.get(1.0, END)
    if text == "" or text == "\n":
        information_label.config(text="ERROR", fore=indian_red)
        return

    lines = text.split("\n")

    lines = list(filter(lambda x: (x != '' or x != "\n"), lines))

    # if line contains " -> should be escaped \"
    for i in range(len(lines)):
        line = list(lines[i])
        j = 0
        while j < len(line):
            if line[j] == '"':

                # insert before \
                line.insert(j, "\\")
                j += 1

            j += 1

        lines[i] = "".join(list(line))

    lines = [f'"{line}",' for line in lines]

    lines[-2] = lines[-2][:-1]
    del lines[-1]

    # print("\n".join(lines))

    result = "\n".join(lines)

    textbox.delete(1.0, END)
    textbox.insert(1.0, result)

    pyperclip.copy(result)

    information_label.config(text="conversion copied to clipboard!", fore=forest_green)

def BackgroundCheck():
    global ConvertCode, textbox
    while 1:
        text = textbox.get(1.0, END)
        if text != "\n":
            ConvertCode()
            sleep(.1)
            ClearTextbox()
        else:
            information_label.config(text="PASTE TEXT TO INSERT QUOTES")
        sleep(.5)

def BackGroundCheckThread():
    background_check_thread = threading.Thread(target=BackgroundCheck, args=())
    background_check_thread.start()

convert_button = NewButton(window_application, "CONVERT", ConvertCode, RIGHT)
convert_button.pack_propagate(0)
config_gui_obj(convert_button, font=cascadia_code_20, back=background, fore=dark_green)


BackGroundCheckThread()
ClearLabelThread()
window_application.mainloop()