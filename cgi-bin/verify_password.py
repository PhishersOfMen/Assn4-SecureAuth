#!/usr/bin/env python3
import cgi
import json
import sys
from save_password import save_password

def validate(password, variants):   
    if password in variants['firstName']:
        return {'valid': False, 'error': "Invalid Password: Don't use your first name."}
    elif password in variants['lastName']:
        return {'valid': False, 'error': "Invalid Password: Don't use your last name."}
    elif password in variants['dob']:
        return {'valid': False, 'error': "Invalid Password: Don't use your birthdate."}
    elif password in variants['phone']:
        return {'valid': False, 'error': "Invalid Password: Don't use your phone number."}
    elif password in variants['street']:
        return {'valid': False, 'error': "Invalid Password: Don't use your street address."}
    elif variants['apt'] and password in variants['apt']:
        return {'valid': False, 'error': "Invalid Password: Don't use your apartment number."}
    elif variants['city']:
        return {'valid': False, 'error': "Invalid Password: Don't use your city."}
    elif variants['state']:
        return {'valid': False, 'error': "Invalid Password: Don't use your state."}
    elif variants['zipCode']:
        return {'valid': False, 'error': "Invalid Password: Don't use your zip code."}
    elif variants['userId']:
        return {'valid': False, 'error': "Invalid Password: Don't use your email address."}
    else:
        return {'valid': True}

data = json.load(sys.stdin)
variants = {}

stuff = []
with open("Enhanced2.txt", 'r') as f:
    for el in f:
        stuff.append(el.rstrip().strip(':'))
temp = []
for el in stuff:
    temp0 = ""
    temp1 = el[1].strip(',')
    for e in temp1:
        temp0 += e
    temp.append(temp0.split(' '))

variants['firstName'] = temp[0]
variants['lastName'] = temp[1]
variants['dob'] = temp[2]
variants['phone'] = temp[3]
variants['street'] = temp[4]
if len(temp == 10):
    variants['apt'] = temp[5]
variants['city'] = temp[-4]
variants['state'] = temp[-3]
variants['zipCode'] = temp[-2]
variants['userId'] = temp[-1]

return_data = validate(data['password'], variants)

if return_data['valid']:
    save_password(data['username'], data['password'])

print("Content-Type: application/json")
print()
print(json.dumps(return_data))