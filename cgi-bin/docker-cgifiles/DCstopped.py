#!/usr/bin/python3
import subprocess
print("content-type: text/plain")
print()
output = subprocess.getoutput("sudo docker ps -a")
print(output)
#print("final")

