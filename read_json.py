import json
import datetime
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


# role = "Regular_Client"
# f = open('positions.json')
# data = json.load(f)
# value = {}
# def read_position():
#     for (k) in data:
#         if role == k.get('role_type'):
#             print(k.get('role_type'))
#             return k.get("operations")
#             break
#
# f.close()
#
# operations = (read_position())
# print(operations)
# for (i) in operations:
#     print(operations[i])
now = datetime.datetime.now()
print('Time is ', now)


business_hours_open = now.replace(hour=9, minute=0, second=0, microsecond=0)
business_hours_close = now.replace(hour=17, minute=0, second=0, microsecond=0)

if business_hours_open < now < business_hours_close:
    print('Valid')
else:
    print("Closed")
