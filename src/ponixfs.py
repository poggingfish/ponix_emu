import os, threading
from watchdog.observers import Observer
import watchdog.events
import time
root = "os"
awaitClose = False
checkCount = 0
open(root+"/dev/stdout","w").close()
def LockStdout():
    x = open(root+"/dev/out.lock","w")
    x.flush()
    x.close()
def Unlock():
    try:
        os.remove(root+"/dev/out.lock")
    except:
        pass
def IsLocked():
    global checkCount
    if checkCount >= 250:
        Unlock()
    x = os.path.exists(root+"/dev/out.lock")
    if x != True:
        checkCount = 0
    else:
        checkCount+=1
    return x
Unlock()
class outhandler:
    def dispatch(event):
        global awaitClose
        if type(event) == watchdog.events.FileModifiedEvent:
            x: watchdog.events.FileModifiedEvent = event # make the IDE happy
            awaitClose = True
        if type(event) == watchdog.events.FileClosedEvent:
            if awaitClose == True:
                print(open(event.src_path).read(),end="")
                Unlock()
def watch_stdout():
        observer = Observer()
        observer.schedule(path=root+"/dev/stdout", event_handler=outhandler, recursive=True)
        observer.start()
        observer.join()
def write(text):
    while IsLocked():
        time.sleep(0.01)
    with open(root+"/dev/stdout", "w") as writeobj:
        writeobj.write(text)
        writeobj.close()
    LockStdout()
threading.Thread(target=watch_stdout).start()