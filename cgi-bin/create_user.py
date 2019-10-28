#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()

# Get each value from form
# value = form.getvalue("value_name")
# TODO: Call function to generate list for variations of personal info

print("Status: 303")
print("Location: /create_password.html")
print()