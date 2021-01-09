from pathlib import Path
import datetime
import pyautogui
import time
import pygetwindow as gw
import keyboard
import sys
import subprocess
nid = None
npass = None
name = ""
zoompath = Path("path.txt")
zoompath = zoompath.read_text()
zoompath = Path(zoompath,"Zoom.exe")
info = Path("info.txt")
info = info.read_text()
info = info.split('\n')

def manualJoin(name):
    for i in range(0,len(info)):
        t = info[i].split(':')
        if name == t[0]:
            nid = t[1]
            npass = t[2]
    return nid,npass,name
def autoJoin():
    if datetime.date.today().weekday() == 0:
        cd = "monday"
    if datetime.date.today().weekday() == 1:
        cd = "tuesday"
    if datetime.date.today().weekday() == 2:
        cd = "wednesday"
    if datetime.date.today().weekday() == 3:
        cd = "thursday"
    if datetime.date.today().weekday() == 4:
        cd = "friday"
    if datetime.date.today().weekday() == 5:
        cd = "saturday"
    ch = datetime.datetime.now().hour

    timetable = Path('time_table.txt')
    timetable = timetable.read_text()
    timetable = timetable.split('\n')

    for i in range(0,len(timetable)):
        r = timetable[i].split(':')
        if cd == r[0]:
            if ch == int(r[1]):
                name = r[2]
    for i in range(0,len(info)):
        t = info[i].split(':')
        if name == t[0]:
            nid = t[1]
            npass = t[2]
    return nid,npass,name
userInput = input()
if userInput == "auto":
    
    nid , npass , name = autoJoin()
else :
    nid , npass , name = manualJoin(userInput)
print("joining class of " + name + " with id " + nid + " and pass " + npass)

time.sleep(3)



subprocess.Popen(zoompath)

time.sleep(4)
join = pyautogui.locateOnScreen("join_button.png")
join = pyautogui.center(join)

pyautogui.click(join.x,join.y)
time.sleep(2)

keyboard.write(str(nid))
pyautogui.press("enter")
time.sleep(3)
keyboard.write(str(npass))
pyautogui.press("enter")
sys.exit()
