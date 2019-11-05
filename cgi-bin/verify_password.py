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
        return {'valid': True, 'error': ""}

data = json.load(sys.stdin)

# TODO: Call function to see if personal info variant exists
variants = {'firstName': "", 'lastName': "", 'dob': "", 'phone': "", 'street': "", 'city': "", 'state': "", 'zipCode': "", 'userId': ""}

return_data = validate(data['password'], variants)

if return_data['valid']:
    save_password(data['username'], data['password'])

print("Content-Type: application/json")
print(json.dumps(return_data))