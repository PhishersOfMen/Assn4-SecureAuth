#!/usr/bin/env python3
import cgi
import json
import asyncio

async def info(stuff):
    # TODO: Call function to generate list for variations of personal info
    pass

form = cgi.FieldStorage()

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

with open("user_info.txt", "w+") as file:
    json.dump(data, file)

asyncio.run(info(data))

print("Content-Type: text/html\n\n")

redirectURL = "http://localhost:8000/create_password.html"
print('<html>')
print('  <head>')
print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
print('  </head>')
print('</html>')