import hashlib
import re
import json
# def enrol_users():
import io
from contextlib import redirect_stdout


def take_user_input():
    uname_input = input("Enter username: ")
    pword_input = input("Enter password: ")
    #uname_input = "Tanvir"
    #pword_input = "A123456a!"


    # Taking user name and password
    flag = check_user_password(uname_input, pword_input)
    while flag == False:
        print("Enrolment was not successful. Please try again")
        uname_input = input("\nEnter username: ")
        pword_input = input("Enter password: ")
        flag = check_user_password(uname_input, pword_input)

    # Taking Position Input
    position_type = "Teller"
    position_type = input("Enter Position: ")
    flag_position = verify_position(position_type)
    while flag_position == False:
        print("Please Try Again")
        position_type = input("Enter Position: ")
        flag_position = verify_position(position_type)
    if flag_position & flag:
        enrol_user(uname_input, pword_input, position_type)
        print("Enrolment is successful")

    return 0

def check_user_password(uname_input, pword_input):
    flag = - 1
    while flag == -1:
        if len(pword_input) < 8 or len(pword_input) > 12:
            flag = -1
            error = "Failed: Password is less than 8 characters"
            print(error.strip())
            return False
            break

        if uname_input == pword_input:
            flag = -1
            error = "Failed: Password is Same as User Name"
            print(error.strip())
            return False
            break
        elif not re.search("[a-z]", pword_input):
            flag = -1
            print("Failed: Password should have at least one character between a-z")
            return False
            break
        elif not re.search("[A-Z]", pword_input):
            flag = -1
            print("Failed: Password should have at least one character between A-Z, capital case")
            return False
            break
        elif not re.search("[0-9]", pword_input):
            flag = -1
            print("Password must contain at least one Number, 0-9")
            return False
            break
        elif not re.search("[@$!#%?*]", pword_input):
            flag = -1
            print("Password must contain at least one special character among @$!#%?*")
            return False
            break

        #elif re.search("\s", pword_input):
        #  break
        else:
            flag = 0
            print("Password Accepted")
            return True
            break

def enrol_user(uname_input, pword_input, position_type):
    # @Todo store the user name and password into password.txt
    # @TODO add the following into password_db.py, in the add_record function
    users = {}
    salt = str(123456)
    hash_object = hashlib.sha256((pword_input + salt).encode())
    pswd = open("password.txt", "a")
    pswd.write(uname_input + ' ' + (hash_object.hexdigest()) + ' ' + salt + "\n")
    pswd.close()

    # Write username and position type in roles_types.txt
    role_database = open("role_types.txt", "a")
    role_database.write(uname_input + ' ' + position_type + "\n")
    role_database.close()

def verify_position(position_type):
    available_positions = []
    f = open('positions.json')
    data = json.load(f)
    for (k) in data:
        available_positions.append(k.get('role_type'))

    f.close()
    if position_type in available_positions:
        print("Position input is valid")
        return True
    else:
        print("Position input is InValid")
        print("Available Positions are", available_positions)
        return False

take_user_input()





