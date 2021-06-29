#!/usr/bin/python3
print("content-type: text/plain")
print()
import subprocess as sp
import cgi
form =   cgi.FieldStorage()
container = form.getvalue("stop_container")
cmd = "sudo docker stop {}".format(container)
output = sp.getoutput(cmd)
print(output)