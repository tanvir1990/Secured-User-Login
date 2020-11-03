# Tanvir Hossain
# Id 101058988
# SYSC 4810 Assignment 3
#Problem 4

from Code.access_control_mechanism import *
from Code.password_control import *
import hashlib
import datetime

def login_main():

    user_name = input("Enter username: ")
    password_input = input("Enter password: ")

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
        access_info = getPositionInfo(role.strip())
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

