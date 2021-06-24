
import psutil, json
from time import sleep
from core.aesthetics import *
from core.system import WriteJSONToFile

TotalTimeJSON_path = r"VSCodeActivity\TotalTime.json"

vscode_question = any([True if p.name() == "Code.exe" else False for p in psutil.process_iter()])

'''
{
    "total_seconds": 4684,
    "total_hours": 1.301111111111111
}
'''

if vscode_question:
    TotalTimeJSON = json.loads(open(TotalTimeJSON_path).read())
    total_seconds = TotalTimeJSON["total_seconds"]
    total_hours = TotalTimeJSON["total_hours"]

    print(ConsoleColored("I'm measuring your vscode activity...", "yellow", bold=1))
    while True:
        vscode_question = any([True if p.name() == "Code.exe" else False for p in psutil.process_iter()])
        sleep(1)
        if vscode_question:
            total_seconds += 1

        WriteJSONToFile({
            "total_seconds": total_seconds,
            "total_hours": total_seconds / 60 / 60
        }, TotalTimeJSON_path)
else:
    print(ConsoleColored("vs code is not open", "red", bold=1))