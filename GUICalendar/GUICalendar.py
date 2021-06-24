
import calendar
from tkinter import *

cal = calendar.calendar(2021)
# print(cal.__repr__())

dim = 1000
window = Tk()
window.geometry("{}x{}".format(dim, dim))
window.title("GUI Calendar")
window.wm_resizable(0, 0)

label = Label(window, text="CALENDAR", bg="dark gray", font=("times", 28, 'bold'))
label.grid(row=1, column=1)
window.configure(bg="white")

calendar_ = Label(window, text=cal, font=("Consolas 15 bold"))
calendar_.grid(row=2, column=1, padx=30)
window.mainloop()