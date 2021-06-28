#!/usr/bin/python3
print("content-type: text/plain")
print()
import subprocess as sp
import cgi
form =   cgi.FieldStorage()
image = form.getvalue("remove_image")
cmd = "sudo docker rmi -f {}".format(image)
status,output = sp.getstatusoutput(cmd)
print(output)
