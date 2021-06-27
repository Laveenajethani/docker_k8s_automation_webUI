#!/usr/bin/python3
print("content-type: text/plain")
print()
import subprocess as sp
import cgi
form =   cgi.FieldStorage()
osimage = form.getvalue("i")
cmd = "sudo docker pull {}".format(osimage)
output1 = sp.getstatusoutput(cmd)
status1 = output1[0]
out1 = output1[1]
if status1 == 0:
        print("Image name {} has been pulled".format(osimage))
else:
        print("Error occured during pulling is {}".format(osimage))
