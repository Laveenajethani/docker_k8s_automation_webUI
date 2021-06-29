#!/usr/bin/python3
import subprocess
print("content-type: text/plain")
print()
cmd = "sudo docker ps"
status = subprocess.getoutput(cmd)
print(status)
#print("final")