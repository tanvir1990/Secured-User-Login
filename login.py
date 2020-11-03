from Code.control_mechanism import *
from Code.password_db import *
import hashlib

#@TODO that Env thing
#@TODO randomize salt
#@TODO User Name Chek
#@TODO Json for role types and Access info

def login_main():

    #user_name = input("Enter username: ")
    user_name = "Ron"
    #password_input = input("Enter password: ")
    password_input = "abc123ABC!"
    login_verification(user_name.strip(), password_input.strip())
    return 0

def login_verification(user_name, password_input):

    # Retrieve the hashed password and the salt value
    retrieved_password, retrieved_salt = read_password(user_name.strip())
    decoded_password = hashlib.sha256((str(password_input).strip()
                                       + str(retrieved_salt.strip())).encode()).hexdigest()
    # Check the Password
    if decoded_password.strip() == retrieved_password.strip():
        result = "Access Granted"
        print(result)
        # Retrieves the role of the user from Database, role_types.txt
        role = read_record(user_name)
        # Retrieves the role permissions and access right from Control Mechanism
        access_info = can_access(role.strip())
        print(access_info)
        print('The User ' + user_name + ' has access to following operations:')
        print(access_info.get("operations"))
        return result
    else:
        result = "Login Failed"
        print(result + ' for ' + user_name + '. Access Denied')
        return result


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

login_main()
