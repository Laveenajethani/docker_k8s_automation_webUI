#!/usr/bin/python3
import subprocess
import cgi
print("content-type: text/plain")
print()

form = cgi.FieldStorage()
ns = form.getvalue("ns_name")

cmd = "kubectl get pods -n {} --kubeconfig config".format(ns)

output = subprocess.getoutput(cmd)
print(output)

