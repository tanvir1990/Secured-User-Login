# Tanvir Hossain
# Id 101058988
# SYSC 4810 Assignment 3
# Problem 1
import json


# This function takes the Role of a User and Returns the
# JSON object of that role. Later, the operations
# accessible to that role are retrieved and displayed in login.py
def can_access_roles_operations(role):
    f = open('positions.json')
    data = json.load(f)
    for (k) in data:
        if role.strip() == k.get('role_type').strip():
            return k
            break

    f.close()






