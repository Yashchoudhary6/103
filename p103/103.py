import time
import os
import shutil
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "Downloads"
to_dir =   "C:/Users/DELL LAPTOP/Downloads/Amazing folder"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name,ext = os.path.splitext(event.src_path)
        for key,value in dir_tree.items():
            if ext in value:
                file_name=os.path.basename(event.src_path)
                path1=from_dir+"/"+file_name
                path2=to_dir+"/"+key
                path3=to_dir+"/"+key+"/"+file_name
                time.sleep(3)
                if os.path.exists(to_dir+"/"+key):
                    print("moving"+file_name)
                    shutil.move(path1,path3)
                else:
                    os.makedirs(path2)
                    print("moving"+file_name)
                    shutil.move(path1,path3) 
        print(event)
        print(event.src_path)

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
       time.sleep(2)
       print("running...")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()
    