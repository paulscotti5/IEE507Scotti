#!/usr/bin/env python3

import cgitb
import os

cgitb.enable()

print("Content-Type: text/html;charset=utf-8")
print("Content-Type:text/html\r\n")
for param in os.environ.keys():
	print("<b>%20s</b>: %s<\br>" % (param, os.environ[param]))
