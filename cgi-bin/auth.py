#!/usr/bin/env python3
import json
import sys
import hashlib

data = json.load(sys.stdin)

user = data["username"]
pwd = data["password"]

s = {}
with open("salt.txt", "r") as f:
    for line in f:
        (key, val) = line.split()
        s[key] = val

p = {}
with open("password.txt", "r") as f:
    for line in f:
        (key, val) = line.split()
        p[key] = val

salt = s[user]

phash = p[user]

m = hashlib.sha256()
m.update(str(pwd + salt).encode("utf-8"))
hashed_password = m.hexdigest()

payload = {}

payload["match"] = phash == hashed_password

print("Content-Type: application/json")
print()
print(json.dumps(payload))