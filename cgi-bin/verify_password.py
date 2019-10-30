#!/usr/bin/env python3
import cgi
import json
import sys

data = json.load(sys.stdin)

# TODO: Call function to see if personal info variant exists

print("Content-Type: application/json")
print(json.dumps(return_data))