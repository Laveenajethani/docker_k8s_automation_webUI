#!/usr/bin/python3
import subprocess
print("content-type: text/plain")
print()
cmd = "sudo docker rmi -f $(sudo docker images)"
output = subprocess.getoutput(cmd)
print(output)
#print("final")