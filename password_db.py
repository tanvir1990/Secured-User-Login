import warnings
def add_record():
    return 0


# Reads Record from a "Database" called role_types.txt
def read_record(user_name):
    password_file = open("role_types.txt")
    user_list = {}             #One for complete Info
    user_array = []            #One for Verification
    for line in password_file:
        record = line.split(' ')
        user = record[0]
        user_array.append(record[0])
        role_type = record[1]
        user_list.update({user: role_type})
    password_file.close()

    if user_name in user_array:
        return user_list.get(user_name)     #Basically retrieves the roletype for the given user
    else:
        warnings.warn("User name not Found")




