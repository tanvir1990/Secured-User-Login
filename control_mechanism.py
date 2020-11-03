import json

def can_access(role):
    f = open('positions.json')
    data = json.load(f)
    for (k) in data:
        if role.strip() == k.get('role_type').strip():
            return k
            break

    f.close()






