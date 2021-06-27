#!/usr/bin/python3
import subprocess
print("content-type: text/plain")
print()
image = subprocess.getoutput("sudo docker rm -f $(sudo docker ps -a -q)")
print(image)
