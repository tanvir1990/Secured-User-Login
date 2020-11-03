import json

def can_access(role):
    f = open('positions.json')
    data = json.load(f)
    for (k) in data:
        if role == k.get('role_type'):
            return k
            break

    f.close()






