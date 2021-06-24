
import os
import cv2
import pyautogui
import subprocess
from time import sleep
from threading import Thread
from core.AnnouncementSystem.AnnouncementSystem import Countdown

# ...\OBSAutomation\
project_folder = os.getcwd()

obs64_folder = "C:\\Program Files\\obs-studio\\bin\\64bit\\"
obs64_exe = "obs64.exe"
def OpenOBS():
    os.chdir(obs64_folder)
    obs_thread = Thread(target=os.system, args=(obs64_exe, ))
    obs_thread.start()

start_recording_path = "start_recording.png"
def StartRecording():
    os.chdir(project_folder)
    print("searching for start recording button...")
    start_recording_button = pyautogui.locateCenterOnScreen(start_recording_path)
    
    if not start_recording_button:
        raise FileNotFoundError("START recording button not found!")
    
    pyautogui.click(start_recording_button)
    
stop_recording_path = "stop_recording.png"
def StopRecording():
    os.chdir(project_folder)
    print("searching for stop recording button...")
    stop_recording_button = pyautogui.locateCenterOnScreen(stop_recording_path)
    
    if not stop_recording_button:
        raise FileNotFoundError("STOP recording button not found!")
    
    pyautogui.click(stop_recording_button)

obs_logo_path = "obs_logo.png"
obs_logo_active_path = "obs_logo_active.png"
def ClickOBSLogo():
    os.chdir(project_folder)
    obs_logo_button = pyautogui.locateCenterOnScreen(
        obs_logo_path,
        confidence=.7
    )
    
    if not obs_logo_button:
        obs_logo_button = pyautogui.locateCenterOnScreen(
            obs_logo_active_path,
            confidence=.7
        )
        
        if not obs_logo_button:
            raise FileNotFoundError("obs logo cant be found.")
            
    pyautogui.click(obs_logo_button)

obs_sources_path = "obs_sources_empty.png"
def OBSourcesEmptyVisible():
    os.chdir(project_folder)
    located = pyautogui.locateCenterOnScreen(
        obs_sources_path,
        confidence=.9
    )
    if located:
        return True
    return False
    
obs_window_bar_red_path = "obs_window_bar_red.png"
obs_window_bar_white_path = "obs_window_bar_white.png"
def OBSWindowBarVisible():
    os.chdir(project_folder)
    located = pyautogui.locateCenterOnScreen(
        obs_window_bar_red_path,
        confidence=.8
    )
    if located:
        return True
    
    tryagain = pyautogui.locateCenterOnScreen(
        obs_window_bar_white_path,
        confidence=.8
    )
    if tryagain:
        return True
        
    return False

kill_obs_command = "taskkill /F /IM obs64.exe"
obs_exit_button_path = "obs_exit_button.png"
def ExitOBS():
    os.chdir(project_folder)
    located = pyautogui.locateCenterOnScreen(
        obs_exit_button_path,
        confidence=.8
    )
    
    if not located:
        raise FileNotFoundError("obs exit button cant be found.")
        
    pyautogui.click(located)

def SimpleExecution():
    ClickOBSLogo()
    Countdown(5)
    StartRecording()
    Countdown(10)
    StopRecording()
    Countdown(3)
    ExitOBS()

if __name__ == '__main__':
    SimpleExecution()