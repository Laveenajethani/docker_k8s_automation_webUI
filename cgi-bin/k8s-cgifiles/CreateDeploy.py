#!/usr/bin/python3
import subprocess
import cgi
print("content-type: text/plain")
print()

form = cgi.FieldStorage()
ns = form.getvalue("CD_ns_name")
deploy = form.getvalue("CD_deploy_name")
image = form.getvalue("CD_image_name")

cmd = "kubectl create deploy {} --image={} -n {} --kubeconfig config".format(deploy,image,ns)

output = subprocess.getoutput(cmd)
print(output)

