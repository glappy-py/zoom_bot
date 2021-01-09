# Importing useful modules
import pathlib
import datetime
import pyautogui
import pygetwindow as gw
import keyboard
import sys
from time import sleep
import subprocess
# ------------------------
# Declaring the var for id , pass and teacher's name
nid = None  
npass = None
name = ""
# Reading path.txt and extracting the path in which zoom is installed
zoompath = pathlib.Path("txts\\path.txt")
zoompath = zoompath.read_text()
zoompath = pathlib.Path(zoompath,"Zoom.exe")
zoompath = str(zoompath)
zoompath = zoompath.replace("\\","\\\\")
# Reading info.txt and extracting the info about id and passes
info = pathlib.Path("txts\\info.txt")
info = info.read_text()
info = info.split('\n')

# Takes in the teacher's name and returns their id and pass
def manualJoin(name):
    for i in range(0,len(info)):
        t = info[i].split(':')
        if name == t[0]:
            nid = t[1]
            npass = t[2]
    return nid,npass,name
# Reads the time_table.txt and and returns id , pass and teacher's name
# according to the time table
def autoJoin():
    # Checking which day is today 
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
    #---------------------------------------
    ch = datetime.datetime.now().hour # which hour is it now 

    # Reads the time_table.txt and stores it in the var timetable as an Array
    timetable = pathlib.Path('txts\\time_table.txt')
    timetable = timetable.read_text()
    timetable = timetable.split('\n')

    # Extracting the id and pass
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
        # --------------------------
        return nid,npass,name
    # except :
    #     print("there's no class right now !")


# Asking the user for manual join or auto join
userInput = input()
if userInput == "auto":
    try :
        nid , npass , name = autoJoin()
    except :
        print("you don't have any class right now")
        sleep(3)
        sys.exit()
        
else :
    nid , npass , name = manualJoin(userInput)
# --------------------------------------------
subprocess.Popen(zoompath) # launching zoom

# checking if zoom has launched yet
while pyautogui.locateOnScreen("img\\join_button.png") == None and pyautogui.locateOnScreen("img\\join_a_meeting.png") == None:
    print("waiting for zoom to launch")
    
# checking if the user has signed in or not and locate the buttons accordingly
try:
    join = pyautogui.locateOnScreen("img\\join_button.png")
    join = pyautogui.center(join)
    pyautogui.click(join.x,join.y)
except Exception as e:
    join = pyautogui.locateOnScreen("img\\join_a_meeting.png")
    join = pyautogui.center(join)
    pyautogui.click(join.x,join.y)

# showing class name , id and pass to user for cross correction
print("joining class of " + name + " with id " + nid + " and pass " + npass)


# waiting for zoom to load
while pyautogui.locateOnScreen('img\\joining.png') == None:
    print("waiting...")


# entering id and pass 
keyboard.write(str(nid))
pyautogui.press("enter")
while pyautogui.locateOnScreen('img\\passcode.png') == None:
    print("waiting...")
keyboard.write(str(npass))
pyautogui.press("enter")
# --------------------

sys.exit() # closing zoom-bot.py
