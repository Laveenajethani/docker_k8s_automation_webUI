#!/usr/bin/python3
print("content-type: text/plain")
print()
import subprocess as sp
import cgi
form =   cgi.FieldStorage()
container = form.getvalue("exec_container")
command = form.getvalue("exec_command")
cmd = "sudo docker exec {} {}".format(container,command)
output1 = sp.getstatusoutput(cmd)
status1 = output1[0]
out1 = output1[1]
if status1 == 0:
        print(out1)
else:
        print("Error occured during exec {}".format(out1))
