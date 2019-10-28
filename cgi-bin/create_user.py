import cgi

form = cgi.FieldStorage()

# Get each value from form
# value = form.getvalue("value_name")
# TODO: Call function to generate list for variations of personal info

userId = form.getvalue("emailid")

print("Content-Type: text/html\n\n")
# print("Content-Type: text/html")

redirectURL = "http://localhost:8000/create_password.html"
print('<html>')
print('  <head>')
print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
print('  </head>')
print('</html>')
# print()
# print(userId)