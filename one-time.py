import os
import time
from subprocess import Popen

batch = os.getcwd() + "/run.bat"
Popen(batch)
print("Opening server on port 7000")
time.sleep(10)
os.system("server.py")


