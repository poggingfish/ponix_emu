import os, threading
from watchdog.observers import Observer
import watchdog.events
import time
root = "os"
awaitClose = False
class outhandler:
    def dispatch(event):
        global awaitClose
        if type(event) == watchdog.events.FileModifiedEvent:
            x: watchdog.events.FileModifiedEvent = event # make the IDE happy
            awaitClose = True
        if type(event) == watchdog.events.FileClosedEvent:
            if awaitClose == True:
                print(open(event.src_path).read(),end="")
def watch_stdout():
        observer = Observer()
        observer.schedule(path=root+"/dev/stdout", event_handler=outhandler, recursive=True)
        observer.start()
        observer.join()
def write(text):
    with open(root+"/dev/stdout", "w") as writeobj:
        writeobj.write(text)
        writeobj.close()
    time.sleep(0.1)
threading.Thread(target=watch_stdout).start()