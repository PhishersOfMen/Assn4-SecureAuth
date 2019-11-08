#!/usr/bin/env python3
import sys
import cgi
import json

form = cgi.FieldStorage()

filename = "user_info.txt"
data = {}

data['firstName'] = form.getvalue('firstname')
data['lastName'] = form.getvalue('lastname')
data['dob'] = form.getvalue('dob')
data['phone'] = form.getvalue('phone')
data['street'] = form.getvalue('streetname')
data['apt'] = form.getvalue('aptnumber')
data['city'] = form.getvalue('city')
data['state'] = form.getvalue('state')
data['zipCode'] = form.getvalue('zipcode')
data['userId'] = form.getvalue("emailid")

with open(filename, "w+") as file:
    json.dump(data, file)

import wordPlay2

print("Content-Type: text/html\n\n")

redirectURL = "http://localhost:8000/create_password.html"
print('<html>')
print('  <head>')
print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
print('  </head>')
print('</html>')