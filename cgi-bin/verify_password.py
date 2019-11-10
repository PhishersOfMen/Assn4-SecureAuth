#!/usr/bin/env python3
import cgi
import json
from save_password import save_password

def validate(password, variants): 
    if password == "":
        return {'valid': False, 'error': "Must have a password."}
    elif password in variants['firstName']:
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
    elif password in variants['city']:
        return {'valid': False, 'error': "Invalid Password: Don't use your city."}
    elif password in variants['state']:
        return {'valid': False, 'error': "Invalid Password: Don't use your state."}
    elif password in variants['zipCode']:
        return {'valid': False, 'error': "Invalid Password: Don't use your zip code."}
    elif password in variants['userId']:
        return {'valid': False, 'error': "Invalid Password: Don't use your email address."}
    elif password in variants['dictionary']:
        return {'valid': False, 'error': "Invalid Password: Don't use a password that is commonly used."}
    else:
        return {'valid': True}

data = cgi.FieldStorage()

username = data.getvalue("username", default="")
password = data.getvalue("password", default="")

variants = {}

stuff = []
with open("Enhanced2.txt", 'r') as f:
    for el in f:
        stuff.append(el.rstrip().split(':'))
temp = []
for el in stuff:
    temp0 = ""
    temp1 = el[1].split(',')
    for e in temp1:
        temp0 += e
    temp.append(temp0.split(' ')[:-1])

stuff2 = []
with open("cgi-bin/Enhanced.txt", 'r') as f:
    for el in f:
        stuff2.append(el.rstrip().split(':'))
temp2 = []
for el in stuff2:
    temp3 = ""
    temp4 = el[1].split(',')
    for e in temp4:
        temp3 += e
    temp4 = temp3.split(' ')[:-1]
    for i in temp4:
        temp2.append(i)

variants['firstName'] = temp[0]
variants['lastName'] = temp[1]
variants['dob'] = temp[2]
variants['phone'] = temp[3]
variants['street'] = temp[4]
if len(temp) == 10:
    variants['apt'] = temp[5]
variants['city'] = temp[-4]
variants['state'] = temp[-3]
variants['zipCode'] = temp[-2]
variants['userId'] = temp[-1]
variants['dictionary'] = temp2


return_data = validate(password, variants)

if return_data['valid']:
    save_password(username, password)

print("Content-type: application/json")
print()
print(json.dumps(return_data, separators=(',', ':')))