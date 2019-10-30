#!/usr/bin/env python3
import cgi
import json
import sys
from save_password import save_password

def validate():
    return 123

data = json.load(sys.stdin)

valid = False
# TODO: Call function to see if personal info variant exists

return_data = validate()

if valid:
    save_password(data['username'], data['password'])

print("Content-Type: application/json")
print(json.dumps(return_data))