
import os
import sys
import subprocess
import webbrowser
from tkinter import *
from json import loads
from time import sleep
from threading import Thread
from functools import partial
from core.json_module import *

# project_folder = "FacultyMenu"
classes_json_path = "database/classes.json"
icons_folder = "icons"

def NewFrame(tkinter_object, position, expand=YES, fill=BOTH):
    frame = Frame(tkinter_object)
    frame.pack(side=position, expand=expand, fill=fill)
    return frame

def NewButton(tkinter_object, button_text, function, position, expand=YES, fill=BOTH):
    button = Button(tkinter_object, text=button_text, command=function, activebackground="#ff5842")
    button.pack(side=position, expand=expand, fill=fill)
    return button

def NewLabel(tkinter_object, label_text, position, expand=YES, fill=BOTH):
    label = Label(tkinter_object, text=label_text)
    label.pack(side=position, expand=expand, fill=fill)
    return label


def ConvertSlashToBackSlash(path: str):
    items = path.split("/")
    return "\\".join(items)

# database
FacultyClassesJSON = read_json_from_file(classes_json_path)

font_style = ('Consolas', 20, 'bold')
font_style_big = ('Consolas', 30, 'bold')
font_style_very_big = ("Abadi", 45, 'bold')
background_color = "white"

window_application = Tk()
window_application.title("Faculty Menu")
window_application.iconbitmap("database/app_icons/app_icon.ico")

application_title_frame = NewLabel(window_application, "Blended Learning", TOP, NO)
application_title_frame.config(justify=CENTER)
application_title_frame.config(font=font_style_very_big)
application_title_frame.config(foreground="black", background=background_color)

title_labels_frame = NewFrame(window_application, TOP, NO)

# courses label
courses_label = NewLabel(title_labels_frame, "COURSES", LEFT)
courses_label.config(font=font_style_big)
courses_label.config(foreground="red", background=background_color)

sep = NewLabel(title_labels_frame, "", LEFT)
sep.config(foreground="white", background="white")

# seminaries label
seminaries_label = NewLabel(title_labels_frame, "SEMINARIES", LEFT)
seminaries_label.config(font=font_style_big)
seminaries_label.config(foreground="green", background=background_color)

# main farme
courses_seminaries_frame = NewFrame(window_application, TOP, NO)

# courses playground
courses_main_frame = NewFrame(courses_seminaries_frame, LEFT, NO)
# seminaries playground
seminaries_main_frame = NewFrame(courses_seminaries_frame, RIGHT, NO)

# modifying from slash to backlash
for faculty_class in FacultyClassesJSON:
    for c in faculty_class["classes"]:
        path = c["folder_path"]
        __items = path.split("/")
        path = "\\".join(__items)
        c["folder_path"] = path
  
# printing results      
# for faculty_class in FacultyClassesJSON:
#     for c in faculty_class["classes"]:
#         print(c["folder_path"])

# creating the actual window application
for faculty_class in FacultyClassesJSON:
    if faculty_class["class_name"] != "":
        for c in faculty_class["classes"]:
            button_name = faculty_class["class_name"]
            
            if c["class_type"] == "course":
                course_frame = NewFrame(courses_main_frame, TOP, NO)
                
                # blended learning url button
                blended_learning_course = NewButton(course_frame, button_name, partial(
                    webbrowser.open, c["ase_url"]
                ), LEFT)
                blended_learning_course.config(height=1, width=45)
                blended_learning_course.config(justify=LEFT)
                blended_learning_course.config(foreground="blue", background=background_color)
                blended_learning_course.config(font=font_style)
                
                # folder location button
                # folder_location_button = NewButton(course_frame, "Folder", partial(
                #     subprocess.Popen, r"explorer /startfile,\"{}\"".format(ConvertSlashToBackSlash(c["folder_path"]))
                # ), RIGHT)

                folder_location_button = NewButton(course_frame, "Folder", partial(
                    os.system, "explorer {}".format(c["folder_path"])
                ), RIGHT)
                
                # print(ConvertSlashToBackSlash(c["folder_path"]))
                
                folder_location_button.config(height=1, width=8)
                folder_location_button.config(justify=RIGHT)
                folder_location_button.config(foreground="blue", background=background_color)
                folder_location_button.config(font=font_style)
                
                # zoom url button
                zoom_url_course = NewButton(course_frame, "Zoom", partial(
                    webbrowser.open, c["zoom_url"]
                ), RIGHT)
                zoom_url_course.config(height=1, width=5)
                zoom_url_course.config(justify=RIGHT)
                zoom_url_course.config(foreground="blue", background=background_color)
                zoom_url_course.config(font=font_style)
                
            else:
                seminary_frame = NewFrame(seminaries_main_frame, TOP, NO)
                
                # blended learning url button
                blended_learning_seminary = NewButton(seminary_frame, button_name, partial(
                    webbrowser.open, c["ase_url"]
                ), RIGHT)
                blended_learning_seminary.config(height=1, width=45)
                # blended_learning_seminary.config(justify=LEFT)
                blended_learning_seminary.config(foreground="blue", background=background_color)
                blended_learning_seminary.config(font=font_style)
                
                # zoom url button
                zoom_url_seminary = NewButton(seminary_frame, "Zoom", partial(
                    webbrowser.open, c["zoom_url"]
                ), LEFT)
                zoom_url_seminary.config(height=1, width=5)
                # zoom_url_seminary.config(justify=RIGHT)
                zoom_url_seminary.config(foreground="blue", background=background_color)
                zoom_url_seminary.config(font=font_style)



# economy stuff
economy_documentationJSON = read_json_from_file("database/economy/documentation.json")

def OpenAllEconomyCourses():
    for course in economy_documentationJSON["courses"]:
        webbrowser.open("file:///{}".format(course["path"]))
        # sleep(0.3)

def OpenAllEconomyCoursesNewThread():
    economy_courses_thread = Thread(target=OpenAllEconomyCourses, args=())
    economy_courses_thread.start()
    del economy_courses_thread
    
# open all economy courses button
all_economy_courses = NewButton(window_application, "open ECONOMY courses", OpenAllEconomyCoursesNewThread, TOP, NO)
all_economy_courses.config(height=1, width=10)
all_economy_courses.config(foreground="blue", background=background_color)
all_economy_courses.config(font=font_style)

# economy stuff


# bco stuff
bco_documentationJSON = read_json_from_file("database/bco/documentation.json")
def OpenAllBCOCourses():
    for doc in bco_documentationJSON:
        if doc["path"] != "":
            webbrowser.open("file:///{}".format(doc["path"]))

def OpenAllBCOCoursesNewThread():
    bco_courses_thread = Thread(target=OpenAllBCOCourses, args=())
    bco_courses_thread.start()
    del bco_courses_thread

# open all bco courses button
all_bco_courses = NewButton(window_application, "open BCO courses", OpenAllBCOCoursesNewThread, TOP, NO)
all_bco_courses.config(height=1, width=10)
all_bco_courses.config(foreground="blue", background=background_color)
all_bco_courses.config(font=font_style)

# bco stuff




window_application.mainloop()