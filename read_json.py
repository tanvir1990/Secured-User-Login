import json

# role = "Teller"
# available_positions = []
# f = open('positions.json')
# data = json.load(f)
# for (k) in data:
#     available_positions.append(k.get('role'))
#
#
# if role in available_positions:
#     print("Position input is valid")
# else:
#     print("Position input is InValid")
#
# print("Available Positions in the system are: ", available_positions)


role = "Regular_Client"
f = open('positions.json')
data = json.load(f)
value = {}
def read_position():
    for (k) in data:
        if role == k.get('role_type'):
            return k.get('operations')
            break

f.close()

operations = (read_position())

for (i) in operations:
    print(operations[i])
