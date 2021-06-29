#!/usr/bin/python3
import subprocess
print("content-type: text/plain")
print()
output = subprocess.getoutput("sudo docker rmi -f $(sudo docker images)")
print(output)
