#!/usr/bin/python3
print("content-type: text/plain")
print()
import subprocess as sp
import cgi
form =   cgi.FieldStorage()
container = form.getvalue("stop_container")
cmd = "sudo docker stop {}".format(container)
status , output = sp.getstatusoutput(cmd)
if status==0:
    print("{} has stopped".format(output))
else:
    print(output)
#print("final")