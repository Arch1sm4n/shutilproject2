import os
import shutil
import time

path = "C:/Users/USER/Documents/testfolder"

days = time.time() - (30 * 24 * 60 * 60)

if path.st_ctime>=days:
    source = "C:/Users/USER/Documents/testfolder"
    destination = "C:/Users/USER/Documents/deletefolder"
    dest = shutil.move(source,destination)


