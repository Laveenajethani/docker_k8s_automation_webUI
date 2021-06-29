#!/usr/bin/python3
print("content-type: text/plain")
print()
import subprocess as sp
import cgi
form =   cgi.FieldStorage()
container = form.getvalue("remove_container")
cmd = "sudo docker rm -f {}".format(container)
status,output = sp.getstatusoutput(cmd)
if status == 0:
        print("{} has removed".format(output))
else:
        print(output)
#print("final")