#!/usr/bin/python3
import subprocess
print("content-type: text/plain")
print()
image = subprocess.getoutput("sudo docker rmi -f $(sudo docker images)")
print("All images has been removed successfully..")
