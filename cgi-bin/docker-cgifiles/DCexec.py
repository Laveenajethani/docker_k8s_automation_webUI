#!/usr/bin/python3
print("content-type: text/plain")
print()
import subprocess as sp
import cgi
form =   cgi.FieldStorage()
container = form.getvalue("exec_container")
command = form.getvalue("exec_command")
cmd = "sudo docker exec {} {}".format(container,command)
output = sp.getoutput(cmd)
print(output)
#print("final")