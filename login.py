from Code.control_mechanism import *
from Code.password_db import *
import hashlib
import datetime

#@TODO that Env thing
#@TODO randomize salt

def login_main():

    #user_name = input("Enter username: ")
    user_name = "Tanvir"
    #password_input = input("Enter password: ")
    password_input = "ABCabc123!"
    # Retrieves the role of the user from Database, role_types.txt
    role, env = read_record(user_name)
    login_verification(user_name.strip(), password_input.strip(), role, env)
    return 0


def login_verification(user_name, password_input, role, env):

    # Retrieve the hashed password and the salt value
    retrieved_password, retrieved_salt = read_password(user_name.strip())
    decoded_password = hashlib.sha256((str(password_input).strip()
                                       + str(retrieved_salt.strip())).encode()).hexdigest()
    if int(env) == 1:
        system_access = check_system_time_and_access()
    else:
        system_access = True

    # Check the Password
    if password_is_valid(decoded_password.strip(), retrieved_password.strip()) & system_access:
        result = "Access Granted"
        print(result)
        # Retrieves the role permissions and access right from Control Mechanism
        access_info = can_access(role.strip())
        print('The User ' + user_name + ' has access to following operations:')
        operations = access_info.get('operations')
        for (i) in operations:
            print(operations[i])
        return result
    else:
        result = "Login Failed"
        print(result + ' for ' + user_name + '. Access Denied')
        return result


def password_is_valid(decoded_password, retrieved_password):
    if decoded_password.strip() == retrieved_password.strip():
        return True
    else:
        return False

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

def check_system_time_and_access():
    now = datetime.datetime.now()
    print('Current Time is ', now)

    business_hours_open = now.replace(hour=9, minute=0, second=0, microsecond=0)
    business_hours_close = now.replace(hour=17, minute=0, second=0, microsecond=0)

    if business_hours_open < now < business_hours_close:
        return True
    else:
        print("Teller is not allowed at this time to access the system")
        return False
login_main()
