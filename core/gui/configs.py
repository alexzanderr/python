
"""
    core/gui/configs.py

    configurations 4 tkinter objects
    helpful in dev of guis

    author: @alexzander
"""


# python
from tkinter import *


# consolas
consolas_10_bold = ('Consolas', 10, 'bold')
consolas_20_bold = ('Consolas', 20, 'bold')
consolas_30_bold = ('Consolas', 30, 'bold')
consolas_40_bold = ('Consolas', 40, 'bold')
consolas_50_bold = ('Consolas', 50, 'bold')
consolas_60_bold = ('Consolas', 60, 'bold')


# cascadia code
cascadia_code_10 = ('Cascadia Code', 10)
cascadia_code_10_bold = ('Cascadia Code', 10, "bold")

cascadia_code_20 = ('Cascadia Code', 20)
cascadia_code_20_bold = ('Cascadia Code', 20, 'bold')

cascadia_code_30 = ('Cascadia Code', 30)
cascadia_code_30_bold = ('Cascadia Code', 30, 'bold')

cascadia_code_40 = ('Cascadia Code', 40)
cascadia_code_40_bold = ('Cascadia Code', 40, 'bold')

cascadia_code_50 = ('Cascadia Code', 50)
cascadia_code_50_bold = ('Cascadia Code', 50, 'bold')


# abadi
abadi_45_bold = ("Abadi", 45, 'bold')


# colors
red = "red"
white = "white"
yellow = "yellow"
blue = "blue"
black = "black"
lightgreen = 'lightgreen'
gray32 = "gray32"
light_golden_rod = "light goldenrod"
gold="gold"
state_blue = "state blue"
indian_red = "indian red"
green = "green"
green2 = "green2"
thistle2 = "thistle2"
gray63 = "gray63"
seashell2 = "seashell2"
gray10 = "gray10"
tomato2 = "tomato2"
pale_green = "pale green"
gold2 = "gold2"
spring_green = "spring green"
green_yellow = "green yellow"
forest_green = "forest green"
brown4 = "brown4"
dark_green = "dark green"
gold3 = "gold3"
DodgerBlue2 = "DodgerBlue2"
gray57 = "gray57"


def config_gui_obj(gui_obj, font: tuple, back=seashell2, fore=gray10,
                   text="", width=None, height=None):
    if height:
        gui_obj.config(height=height)
    if width:
        gui_obj.config(width=width)
    if text:
        gui_obj.config(width=width)
    gui_obj.config(font=font, back=back, fore=fore)