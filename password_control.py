# Tanvir Hossain
# Id 101058988
# SYSC 4810 Assignment 3
# Problem 2
import warnings


def add_record(username_input, position_type, env):
    role_database = open("role_types.txt", "a")
    role_database.write(username_input + ' ' + position_type + ' ' + env + "\n")
    role_database.close()


# Reads Record from a "Database" called role_types.txt
def read_record(user_name):
    password_file = open("role_types.txt")
    user_list = {}             # One for complete Info
    user_env = {}
    user_array = []            # One for Verification
    for line in password_file:
        record = line.split(' ')
        user = record[0]
        user_array.append(record[0])
        role_type = record[1]
        role_env = record[2]
        user_list.update({user: role_type})
        user_env.update({user: role_env.strip()})
    password_file.close()

    if user_name in user_array:
        # Basically retrieves the roletype for the given user
        return user_list.get(user_name), user_env.get(user_name),
    else:
        warnings.warn("User name not Found")


def read_password(user_name):
    password_file = open("password.txt")
    # One for complete Info
    user_list = {}
    # One for Verification
    user_array = []

    for line in password_file:
        record = line.split(' ')
        user = record[0]
        user_array.append(record[0])
        password = record[1]
        salt = record[2]
        user_list.update({user: password})
        if user == user_name:
            break
    password_file.close()

    if user_name in user_array:
        return user_list.get(user), salt  # Basically retrieves the hashed password for the given user
    else:
        warnings.warn("User name not Found")

