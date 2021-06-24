

from core.datetimex import *
from core.algorithm import *
from core.backtrack import *
from core.drive import *
from core.system import *
from core.image import *
from core.json_module import *
from core.numx import *
from core.pathx import *
from core.WindowsAPIX import *
from core.randomx import *
from core.symbols import *
from core.statistix import *
import webbrowser
from core.gui.GUIObjects import *
from core.gui.configurations import *


app_icon_path = "icons/exec.ico"

# database_path = "database/database.json"
# database_json = read_json_from_file(database_path)

websites_path = "database/websites.json"
websites_json = read_json_from_file(websites_path)

class Site:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url
        
websites_list = [
    Site(site["name"], site["url"]) for site in websites_json
]


background_color = seashell2
foreground_color = "dark orange"
green_color = forest_green
yellow_color = gold3


screen_width = 1920
screen_height = 1000
left_to_right = 0
up_to_down = 0
window_geometry = (screen_width, screen_height, left_to_right, up_to_down)


window_application = Tk()
window_application.title("MyInternet")
window_application.geometry("{}x{}+{}+{}".format(*window_geometry))
window_application.iconbitmap(app_icon_path)
window_application.resizable(0, 0)



canvas = Canvas(window_application)
canvas.pack(expand=YES, fill=BOTH, side=LEFT)

scrollbar = Scrollbar(window_application, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.config(yscrollcommand=scrollbar.set)
canvas.bind_all('<Configure>', lambda e: canvas.config(scrollregion=canvas.bbox("all")))

scroll_distance = 1

def mouse_movement(event: Event):
    # print(event)
    if event.delta == -120:
        canvas.yview_scroll(scroll_distance, "units")
    elif event.delta == 120:
        canvas.yview_scroll(-scroll_distance, "units")

canvas.bind_all('<MouseWheel>', mouse_movement)


second_frame = NewFrame(canvas, TOP)
canvas.create_window((0, 0), window=second_frame, anchor="nw")

# img = PhotoImage(file='database/test/f.png')
# img = img.subsample(1, 1)

from functools import partial

def OpenURL(url):
    webbrowser.open(url)

website_buttons = []

button_width = 58

dim = len(websites_list) // 2
for left_site, right_site in zip(websites_list[: dim], websites_list[dim :]):
    button_frame = NewFrame(second_frame, TOP)
    
    left_button = NewButton(button_frame, left_site.name, partial(OpenURL, left_site.url), LEFT)
    left_button.config(font=cascadia_code_20_bold, fore=foreground_color, back=background_color)
    left_button.config(width=button_width)
    
    right_button = NewButton(button_frame, right_site.name, partial(OpenURL, right_site.url), RIGHT)
    right_button.config(font=cascadia_code_20_bold, fore=foreground_color, back=background_color)
    right_button.config(width=button_width)
    
    website_buttons.append((left_button, right_button))

# for w_pair in websites_list:
#     # print(w_pair.url)
#     button = Button(second_frame, text=w_pair.name, width=70, command=partial(OpenURL, w_pair.url), font=cascadia_code_20_bold, fore=gray10, back=background_color)
    
#     button.pack(fill=BOTH, expand=YES)
    
#     website_buttons.append(button)
    
    

def BeforeQuiting():
    # code
        
    window_application.destroy()

window_application.protocol("WM_DELETE_WINDOW", BeforeQuiting)

window_application.mainloop()