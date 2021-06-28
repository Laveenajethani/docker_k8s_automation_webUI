#!/usr/bin/python3
print("content-type: text/plain")
print()
import subprocess as sp
import cgi
form =   cgi.FieldStorage()
container = form.getvalue("remove_container")
cmd = "sudo docker rm -f {}".format(container)
output1 = sp.getstatusoutput(cmd)
status1 = output1[0]
out1 = output1[1]
if status1 == 0:
        print("OS name {} has been removed".format(container))
else:
        print("Error occured during removing is {}".format(out1))
