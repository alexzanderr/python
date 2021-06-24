

from core import datetime__
from core import json__
from win32 import win32evtlog as windows_logs
from pathlib import Path


server = "localhost"


type_system = 'System'
type_application = "Application"
type_security = "Security"
type_setup = "Setup"

hand = windows_logs.OpenEventLog(server, type_application)
flags = windows_logs.EVENTLOG_BACKWARDS_READ | windows_logs.EVENTLOG_SEQUENTIAL_READ
total = windows_logs.GetNumberOfEventLogRecords(hand)



events = windows_logs.ReadEventLog(hand, flags, 0)
print(f"total {type_system} events: {len(events)}")
if events: # type(event) == list
    for event in events:
        event_metadata = {}

        attributes = dir(event)
        for att in attributes:
            if not att.__contains__("_"):
                dict_update = f"event_metadata['{att}'] = event.{att}"
                exec(dict_update)

        event_metadata["TimeGenerated"] = datetime__.datetime_object_to_str(
            event_metadata["TimeGenerated"]
        )
        event_metadata["TimeWritten"] = datetime__.datetime_object_to_str(
            event_metadata["TimeWritten"]
        )
        if isinstance(event_metadata["Data"], bytes):
            event_metadata["Data"] = event_metadata["Data"].decode("utf-8")

        py_sid_object = {}
        for att in dir(event_metadata["Sid"]):
            if not att.__contains__("_"):
                dict_update = f"py_sid_object['{att}'] = event_metadata['Sid'].{att}()"
                try:
                    exec(dict_update)
                except TypeError:
                    pass
        event_metadata["Sid"] = py_sid_object

        # print(event)
        # json__.pretty_print(event_metadata)
        # print("~" * 50)
        # print(windows_logs.EventMetadataEventID())

        # break


windows_logs.CloseEventLog(hand)