import os
import shutil
import time

from jarvis import speak

startup_jarvis = "C:\\Users\\Dr.Wael\\AppData\\Local\\Temp\\e8a12a95fa\\1startupjarvis.pyw"
startup_jarvis2 = "C:\\Users\\Dr.Wael\\AppData\\Local\\Temp\\e8a12a95fa\\2startupjarvis.pyw"
files = "C:\\Users\\Dr.Wael\\PycharmProjects\\The talking project\\jarvis.py"

if os.path.exists("C:\\Users\\Dr.Wael\\AppData\\Local\\Temp\\e8a12a95fa\\startupjarvis.pyw"):
    os.remove("C:\\Users\\Dr.Wael\\AppData\\Local\\Temp\\e8a12a95fa\\startupjarvis.pyw")
else:
    speak("couldn't find startupjarvis.pyw")

if os.path.exists(startup_jarvis):
    speak('1startupjarvis is there. will rename to 2 instead ')
    os.remove("C:\\Users\\Dr.Wael\\AppData\\Local\\Temp\\e8a12a95fa\\1startupjarvis.pyw")
    time.sleep(1)
    shutil.copy(files, "C:\\Users\\Dr.Wael\\AppData\\Local\\Temp\\e8a12a95fa")
    os.rename("C:\\Users\\Dr.Wael\\AppData\\Local\\Temp\\e8a12a95fa\\jarvis.py", startup_jarvis2)
    speak('added the new file')
    quit()
speak('added the new file')


shutil.copy(files, "C:\\Users\\Dr.Wael\\AppData\\Local\\Temp\\e8a12a95fa")
os.rename("C:\\Users\\Dr.Wael\\AppData\\Local\\Temp\\e8a12a95fa\\jarvis.py", startup_jarvis)
speak('added 1 startup')
quit()
