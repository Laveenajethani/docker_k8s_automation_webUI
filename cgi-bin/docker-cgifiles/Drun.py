#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
container = mydata.getvalue("Launch_container")
image = mydata.getvalue("Launch_container_image")

cmd = "sudo docker run -dit --name {} {}".format(container,image)

status , output = subprocess.getstatusoutput(cmd)
if status == 0: 
  print("container {} launched with ID :\n{} ".format(container,output))
else:
  print(output)
#print("final")
