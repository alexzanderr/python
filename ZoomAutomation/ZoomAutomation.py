
import os
import json
import pyautogui
import subprocess
from time import sleep, time
from threading import Thread
from core.WindowsAPIX import Windows10Notification

level_of_confidence = .8

class IterationOverflow:
    """ this classed is used to compare objects found
        by pyautogui with failed iterations by pyautogui 
        trying to find stuff on the screen 
    """
    def __NE__(self, other_instance):
        if type(self) != type(other_instance):
            return True
        return False
    
def ScanTillLocate(image_path: str, scan_time=10, confidence=level_of_confidence):
    """ tries to find the item on the screen as 
        fast as possible in a given time limit.
        if finding fails then returns IterationOverflow instance.
    """
    start_time = time()
    while True:
        print("searching 4 {} ...".format(image_path))
        item_on_the_screen = pyautogui.locateCenterOnScreen(
            image_path,
            confidence=confidence
        )
        
        if item_on_the_screen:
            print("{} found.".format(item_on_the_screen))
            return item_on_the_screen
        
        iteration_time = int(time() - start_time)
        if iteration_time > scan_time:
            print("{} seconds have passed and still no appearance.".format(scan_time))
            print("IterationOverflow()")
            return None
        
def ClickPoint(point_object):
    pyautogui.click(point_object)
    
def DoubleClickPoint(point_object):
    pyautogui.doubleClick(point_object)
    
def WriteToPoint(point_object, content: str):
    pyautogui.click(point_object)
    pyautogui.write(content)

def ZoomNotification(message):
    Windows10Notification(
        "Zoom",
        message,
        5,
        "icons/1.ico",
        True
    )

class ZoomBot:
    
    def __init__(self):
        subprocess.Popen(self.zoom_app_path)
        Windows10Notification(
            "ZoomBot",
            "opening zoom",
            1,
            "icons/1.ico",
            True
        )

    def JoinMeeting(self, meeting_id):
        join_button = ScanTillLocate("images/join_button.png")
        if join_button:
            ClickPoint(join_button)
            
        meeting_id_query = ScanTillLocate("images/meeting_id.png")
        if meeting_id_query:
            WriteToPoint(meeting_id_query, meeting_id)
        
        turn_off_video_button = ScanTillLocate("images/turn_off_video.png")
        if turn_off_video_button:
            ClickPoint(turn_off_video_button)
        
        join_meeting_button = ScanTillLocate("images/join_button_meeting.png")
        if join_meeting_button:
            ClickPoint(join_meeting_button)
            Windows10Notification(
                "Zoom",
                "Entering Clim Personal Meeting Room",
                5,
                "icons/1.ico",
                True
            )
            
    def NewMeeting(self):
        new_meeting_button = ScanTillLocate("images/new_meeting_button.png")
        if new_meeting_button:
            ClickPoint(new_meeting_button)
        
        zoom_meeting_bar_white = ScanTillLocate("images/zoom_meeting_icon_white.png")
        if zoom_meeting_bar_white:
            DoubleClickPoint(zoom_meeting_bar_white)
        else:
            zoom_meeting_bar_red = ScanTillLocate("images/zoom_meeting_icon_red.png")
            if zoom_meeting_bar_red:
                DoubleClickPoint(zoom_meeting_bar_red)
            else:
                ZoomNotification("error")
        
        
        sleep(2)
        pyautogui.doubleClick()
        
        
    
    def CloseZoom(self):
        os.system("taskkill /F /IM Zoom.exe")

if __name__ == '__main__':
    try:
    #     database_json_path = "database.json"
    #     database_json = json.loads(open(database_json_path).read())
    #     clim_meeting = database_json[0]
        
        zoombot = ZoomBot()
        zoombot.NewMeeting()
        # sleep(10)
        # zoombot.CloseZoom()
        
    except Exception as error:
        print(error)
        print("zoom closed by force.")
        os.system("taskkill /F /IM Zoom.exe")