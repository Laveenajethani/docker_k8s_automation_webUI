#!/usr/bin/python3
import subprocess
print("content-type: text/plain")
print()
stoppedContainer = subprocess.getoutput("sudo docker ps -a")
print(stoppedContainer)

