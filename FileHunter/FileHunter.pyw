
# python imports

# 3rd party imports
import pyperclip # pip install pyperclip
from core.aesthetics import *
from core.system import *
from core.development import *
from core.gui.objects import *
from core.gui.configs import *
from core.drive import find_file_on_drive
from tkinter import messagebox
from core.path__ import *
from core.winapi__ import *
import threading
import re

background_color = seashell2
foreground_color = gray10
green_color = forest_green

screen_width = 1300
screen_height = 600
left_to_right = 200
up_to_down = 0
window_geometry = (screen_width, screen_height, left_to_right, up_to_down)


app_icon_path = "icons/exec.ico"

filehunter_window = Tk()
filehunter_window.title("File Hunter")
filehunter_window.geometry("{}x{}+{}+{}".format(*window_geometry))
filehunter_window.iconbitmap(app_icon_path)
filehunter_window.resizable(0, 0)
filehunter_window.config(back=background_color)


title_label = Label(filehunter_window, text="[ paste file name below ]")
title_label.config(back=background_color, fore=forest_green, height=2, font=cascadia_code_20_bold)
title_label.pack(fill=BOTH, side=TOP)


file_textbox = Text(filehunter_window, height=1, font=cascadia_code_20_bold)
file_textbox.config(back=background_color, fore=tomato2)
file_textbox.pack(fill=BOTH, side=TOP)
# file_textbox.insert(1.0, "FileHunter.pyw")


choose_drive_label = Label(filehunter_window, text="[ choose drive ]")
choose_drive_label.config(back=background_color, fore=forest_green, height=2, font=cascadia_code_20_bold)
choose_drive_label.pack(fill=BOTH, side=TOP)

selected_drive = "D:\\"

def ChangeDriveToC():
    global selected_drive

    selected_drive = "C:\\"
    drive_label.config(text="Selected Drive: [ {} ]".format(selected_drive))

def ChangeDriveToD():
    global selected_drive

    selected_drive = "D:\\"
    drive_label.config(text="Selected Drive: [ {} ]".format(selected_drive))


buttons_frame = Frame(filehunter_window, back=background_color)
buttons_frame.pack(side=TOP, fill=X)

c_drive_button = Button(buttons_frame, text="<=[ C ]=>", command=ChangeDriveToC, height=1, width=28)
c_drive_button.config(font=cascadia_code_30_bold, fore=gray10, back=background_color)
c_drive_button.pack(side=LEFT, fill=X)

d_drive_button = Button(buttons_frame, text="<=[ D ]=>", command=ChangeDriveToD, height=1, width=28)
d_drive_button.config(font=cascadia_code_30_bold, fore=gray10, back=background_color)
d_drive_button.pack(side=RIGHT, fill=X)

drive_label = Label(filehunter_window, text="Selected Drive: [ {} ]".format(selected_drive), height=2, width=44)
drive_label.config(back=background_color, fore=gray10, font=cascadia_code_20_bold)
drive_label.pack(fill=BOTH, side=TOP)

searching = 0

block = "█"

def UpdateSearchingLabel():
    global searching

    output_label.config(font=cascadia_code_30_bold, fore=gray10)
    while searching == 1:
        stop = False

        for i in range(20):
            t = block * i + block + block * i
            output_label.config(text=t)
            if searching == 0:
                stop = True
                break
            sleep(.3)
            if searching == 0:
                stop = True
                break

        if stop:
            output_label.config(fore=forest_green, font=cascadia_code_20_bold)
            break

from string import punctuation

def HuntFile():
    global searching
    # validating input file
    file = file_textbox.get(1.0, END)
    if file != "\n" and file != "":

        valid = True
        for p in punctuation.replace(".", ""):
            if p in file:
                valid = False
                messagebox.showerror("ERROR", "invalid file name")
                file_textbox.delete(1.0, END)
                break

        if valid:
            choice = messagebox.askquestion(
                "proceed action?",
                "this will run many threads to find\n DRIVE ({})\nFILE: {}".format(selected_drive, file), icon='warning'
            )

            if choice == "yes":
                hunt_button.config(state=DISABLED)
                c_drive_button.config(state=DISABLED)
                d_drive_button.config(state=DISABLED)

                file = file.strip()
                searching = 1
                searching_label_thread = threading.Thread(target=UpdateSearchingLabel, args=())
                searching_label_thread.start()

                result = find_file_on_drive(file, selected_drive, deep_level=2)
                # print(result)
                searching = 0


                if result:
                    if is_file(result) or is_folder(result):
                        sep = get_path_sep(result)
                        result = list(filter(lambda elem: (elem != ""), result.split(sep)))
                        result = sep.join(result)

                        output_label.config(text=result, font=cascadia_code_20_bold)
                        pyperclip.copy(result)

                        windows_notification(
                            "FileHunter",
                            "FOUND\ncopied to clipboard!",
                            3,
                            app_icon_path,
                            1
                        )

                        sleep(2)

                        hunt_button.config(state=NORMAL)
                        c_drive_button.config(state=NORMAL)
                        d_drive_button.config(state=NORMAL)

                        file_textbox.delete(1.0, END)
                        # output_label.config(text="")
                else:
                    output_label.config(text="FILE NOT FOUND", fore=tomato2)

                    threading.Thread(target=messagebox.showinfo, args=("INFO", "404 NOT FOUND")).start()

                    hunt_button.config(state=NORMAL)
                    c_drive_button.config(state=NORMAL)
                    d_drive_button.config(state=NORMAL)

                    file_textbox.delete(1.0, END)
                    output_label.config(text="")

    else:
        # error dialog
        messagebox.showerror("ERROR", "textbox is empty!!")


def HuntFileThread():
    hunt_file_thread = threading.Thread(target=HuntFile, args=())
    hunt_file_thread.start()


hunt_button = Button(filehunter_window, text="<==========[   HUNT   ]==========>", command=HuntFileThread, height=2, width=44)
hunt_button.config(font=cascadia_code_30_bold, fore=tomato2, back=gray32)
hunt_button.pack(side=TOP, fill=X)

output_label = Label(filehunter_window, text="", height=2, width=44)
output_label.config(back=background_color, fore=forest_green)
output_label.pack(fill=X, side=TOP)


def BeforeQuiting():
    # do stuff

    filehunter_window.destroy()

filehunter_window.protocol("WM_DELETE_WINDOW", BeforeQuiting)

filehunter_window.mainloop()