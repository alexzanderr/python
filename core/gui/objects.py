
"""
    core/gui/objects.py

    easy creation of tkinter object

    author: @alexzander
"""


# python
from tkinter import *


def NewFrame(root, position=TOP, expand=YES, fill=BOTH):
    frame = Frame(root)
    frame.pack(side=position, expand=expand, fill=fill)
    return frame


def NewButton(root, text, function, position=TOP, expand=YES, fill=BOTH):
    button = Button(root, text=text, command=function)
    button.pack(side=position, expand=expand, fill=fill)
    return button


def NewLabel(root, text, position=TOP, expand=YES, fill=BOTH):
    label = Label(root, text=text)
    label.pack(side=position, expand=expand, fill=fill)
    return label


def NewLabelWithBorder(root, text, position=TOP, borderwidth=2,
                       relief="solid", expand=YES, fill=BOTH):
    label = Label(root, text=text, borderwidth=borderwidth, relief=relief)
    label.pack(side=position, expand=expand, fill=fill)
    return label


def NewTextBox(
    root,
    text="",
    position=TOP,
    expand=YES,
    fill=BOTH,
    foreground=None,
    background=None
):
    textbox = Text(root, text=text)
    if foreground:
        textbox.config(fore=foreground)
    if background:
        textbox.config(back=background)
    textbox.pack(side=position, expand=expand, fill=fill)