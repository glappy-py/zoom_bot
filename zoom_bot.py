import pathlib
from time import sleep
from sys import exit
from os import startfile
import webbrowser, psutil

id = None  
npass = None
name = ""

zoompath = pathlib.Path("txts\\path.txt")
zoompath = zoompath.read_text()
zoompath = pathlib.Path(zoompath,"Zoom.exe")
zoompath = str(zoompath)
zoompath = zoompath.replace("\\","\\\\")

info = pathlib.Path("txts\\info.txt")
info = info.read_text()
info = info.split('\n')

def manualJoin(name):
    for i in range(0,len(info)):
        t = info[i].split(':')
        if name == t[0] and t[3] == "zoom":
            id = t[1]
            npass = t[2]
    return id, npass, name

def checkIfProcessRunning(processName):
	for proc in psutil.process_iter():
		try:
			if processName.lower() in proc.name().lower():
				return True
		except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
			pass
	return False

userInput = input("Meeting name : ")

id , npass , name = manualJoin(userInput)

if not(checkIfProcessRunning('zoom')):
		startfile(zoompath)

sleep(1)

webbrowser.open(f"zoommtg://zoom.us/join?zc=0&confno={id}&pwd={npass}")

sleep(3)
exit()