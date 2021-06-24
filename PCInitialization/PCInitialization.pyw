
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
import subprocess
from collections import namedtuple
from multiprocessing import Process

code_exe_path = "D:/Applications/Microsoft Visual Studio Code/Microsoft VS Code/Code.exe"

class Application:
    def __init__(self, name, path, has_notification=False):
        self.name = name
        self.path = path
        self.has_notification = has_notification

class CodeWorkspace(Application):
    pass

class PythonApplication(Application):
    pass


def open_application(application: Application):
    if isinstance(application, CodeWorkspace):
        subprocess.Popen([code_exe_path, application.path])
    
    elif isinstance(application, PythonApplication):
        app_process = Process(target=os.startfile, args=(application.path, ))
        app_process.start()
        
    elif isinstance(application, Application):
        subprocess.Popen([application.path])
        

notepads_workspace = CodeWorkspace("Noteads__ workspace", "D:/Alexzander__/Notepads__/Notepads__.code-workspace")
    
python_workspace = CodeWorkspace("python workspace", "D:/Alexzander__/programming/python/python.code-workspace")

cplusplus_workspace = CodeWorkspace("cplusplus workspace", "D:/Alexzander__/programming/cplusplus/cplusplus.code-workspace")



# applications

applications = [
    notepads_workspace,
    python_workspace
]

taskbar = PythonApplication("taskbar", "C:/Windows/System32/Taskmgr.exe")
applications.append(taskbar)

game_center = Application("game_center", "C:/Program Files (x86)/ASUSTeK COMPUTER INC/ROG Gaming Center/ROGGamingCenter.exe", True)
applications.append(game_center)

clock = PythonApplication("clock python app", "C:/Users/dragonfire/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Applications[shortcuts]/Clock.lnk")
applications.append(clock)


rule_202020 = PythonApplication("202020_rule python app", "C:/Users/dragonfire/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Applications[shortcuts]/202020_rule.lnk")
applications.append(rule_202020)


brave_browser = Application("brave browser", "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe")
applications.append(brave_browser)


windows_terminal = Application("windows terminal", "C:/Program Files/WindowsApps/Microsoft.WindowsTerminal_1.5.10271.0_x64__8wekyb3d8bbwe/wt.exe")
applications.append(windows_terminal)


explorer = Application("file explorer", "C:/Windows/explorer.exe")
applications.append(explorer)


# seconds
pause_interval = 10


exec_ico_path = "icons/exec.ico"

def InitializePC():
    Windows10Notification(
        "__INIT__",
        "PC IS INITIALIZING...",
        pause_interval - 1,
        exec_ico_path,
        1
    )
    
    for app in enumerate(applications):
        sleep(pause_interval)
        open_application(app)
        
        Windows10Notification(
            app.name,
            "OPENED successfully",
            pause_interval - 1,
            exec_ico_path,
            1
        )
    
    sleep(pause_interval)
    Windows10Notification(
        "PC INITIALIZATION",
        "SUCCESSFUL",
        pause_interval,
        exec_ico_path,
        1
    )

if __name__ == '__main__':
    InitializePC()