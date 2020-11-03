# Tanvir Hossain
# Id 101058988
# SYSC 4810 Assignment 3
# Problem 1
import json


def getPositionInfo(role):
    f = open('positions.json')
    data = json.load(f)
    for (k) in data:
        if role.strip() == k.get('role_type').strip():
            return k
            break

    f.close()






