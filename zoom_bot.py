# Importing useful modules
from pathlib import Path
from datetime import date,datetime
from pyautogui import center,locateOnScreen,click
from keyboard import press,write
from sys import exit
from time import sleep
from subprocess import Popen
# ------------------------
# Declaring the var for id , pass and teacher's name
nid = None  
npass = None
name = ""
# Reading path.txt and extracting the path in which zoom is installed
zoompath = Path("txts\\path.txt")
zoompath = zoompath.read_text()
zoompath = Path(zoompath,"Zoom.exe")
zoompath = str(zoompath)
zoompath = zoompath.replace("\\","\\\\")
# Reading info.txt and extracting the info about id and passes
info = Path("txts\\info.txt")
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
    if date.today().weekday() == 0:
        cd = "monday"
    if date.today().weekday() == 1:
        cd = "tuesday"
    if date.today().weekday() == 2:
        cd = "wednesday"
    if date.today().weekday() == 3:
        cd = "thursday"
    if date.today().weekday() == 4:
        cd = "friday"
    if date.today().weekday() == 5:
        cd = "saturday"
    #---------------------------------------
    ch = datetime.now().hour # which hour is it now 

    # Reads the time_table.txt and stores it in the var timetable as an Array
    timetable = Path('txts\\time_table.txt')
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
        exit()
        
else :
    nid , npass , name = manualJoin(userInput)
# --------------------------------------------
Popen(zoompath) # launching zoom

# checking if zoom has launched yet
while locateOnScreen("img\\join_button.png") == None and locateOnScreen("img\\join_a_meeting.png") == None:
    print("waiting for zoom to launch")
    
# checking if the user has signed in or not and locate the buttons accordingly
try:
    join = locateOnScreen("img\\join_button.png")
    join = center(join)
    click(join.x,join.y)
except Exception as e:
    join = locateOnScreen("img\\join_a_meeting.png")
    join = center(join)
    click(join.x,join.y)

# showing class name , id and pass to user for cross correction
print("joining class of " + name + " with id " + nid + " and pass " + npass)


# waiting for zoom to load
while locateOnScreen('img\\joining.png') == None:
    print("waiting...")


# entering id and pass 
write(str(nid))
press("enter")
while locateOnScreen('img\\passcode.png') == None:
    print("waiting...")
write(str(npass))
press("enter")
# --------------------
exit() # closing zoom-bot.py
