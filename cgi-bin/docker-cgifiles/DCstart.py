#!/usr/bin/python3
print("content-type: text/plain")
print()
import subprocess as sp
import cgi
form =   cgi.FieldStorage()
container = form.getvalue("start_container")
cmd = "sudo docker start {}".format(container)
status,output = sp.getstatusoutput(cmd)
print(output)