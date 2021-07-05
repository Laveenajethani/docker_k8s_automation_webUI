#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/plain")
print()

form = cgi.FieldStorage()
ns = form.getvalue("create_ns_name")

cmd = "kubectl create ns {} --kubeconfig config".format(ns)

output = subprocess.getoutput(cmd)

print(output)

