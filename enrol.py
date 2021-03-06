# Tanvir Hossain
# Id 101058988
# SYSC 4810 Assignment 3
# Problem 3
from Code.password_control import *
import hashlib
import re
import json
import random


def take_user_input():
    # Taking user name and password inputs from the User
    print("First Name and Last name can only be separated by '_' ")
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")

    while not check_user_password(username_input, password_input):
        print("Enrolment was not successful. Please try again")
        username_input = input("\nEnter username: ")
        password_input = input("Enter password: ")

    # Taking Position Input
    position_type = input("Enter Position: ")
    # position_type = "Employee_Teller"
    flag_position = verify_position(position_type)

    while not flag_position:
        print("Please Try Again")
        position_type = input("Enter Position: ")
        flag_position = verify_position(position_type)

    if flag_position & check_user_password(username_input, password_input):
        enrol_user(username_input, password_input, position_type)
        print("Enrolment is successful\n")


def check_user_password(username_input, password_input):

    flag = - 1
    while flag == -1:
        if len(password_input) < 8 or len(password_input) > 12:
            flag = -1
            error = "Failed: Password must be between 8-12 characters"
            print(error.strip())
            return False
            break

        if username_input == password_input:
            flag = -1
            error = "Failed: Password is Same as User Name"
            print(error.strip())
            return False
            break
        elif not re.search("[a-z]", password_input):
            flag = -1
            print("Failed: Password should have at least one character between a-z")
            return False
            break
        elif not re.search("[A-Z]", password_input):
            flag = -1
            print("Failed: Password should have at least one character between A-Z, capital case")
            return False
            break
        elif not re.search("[0-9]", password_input):
            flag = -1
            print("Password must contain at least one Number, 0-9")
            return False
            break
        elif not re.search("[@$!#%?*]", password_input):
            flag = -1
            print("Password must contain at least one special character among @$!#%?*")
            return False
            break
        elif re.search("Password", password_input):
            flag = -1
            print("Password is too easy to guess. You can't have the word Password in your Password")
            return False
            break

        elif re.search("password", password_input):
            flag = -1
            print("Password is too easy to guess. You can't have the word Password in your Password")
            return False
            break
        elif re.search("Qwerty", password_input):
            flag = -1
            print("Password is too easy to guess. It can't be a commonly guessed.")
            return False
            break

        elif re.search("Qaz123wsx", password_input):
            flag = -1
            print("Password is too easy to guess. You have characters in common sequence")
            return False
            break

        elif re.search("123", password_input):
            flag = -1
            print("Password is too easy to guess. You have characters in common sequence")
            return False
            break
        elif re.search("abc", password_input):
            flag = -1
            print("Password is too easy to guess. You have characters in common sequence")
            return False
            break
        elif re.search("ABC", password_input):
            flag = -1
            print("Password is too easy to guess. You have characters in common sequence")
            return False
            break

        elif re.search(username_input, password_input):
            flag = -1
            print("Password is too easy to guess. You have characters in common sequence")
            return False
            break
        else:
            flag = 0
            print("Password Accepted")
            return True
            break


def enrol_user(username_input, password_input, position_type):

    salt = random.randint(100000, 1000000000)
    hash_object = hashlib.sha256((password_input + str(salt)).encode())
    password = open("password.txt", "a")
    password.write(username_input + ' ' + (hash_object.hexdigest()) + ' ' + str(salt) + "\n")
    password.close()

    # Write username and position type in roles_types.txt
    if position_type.strip() == "Employee_Teller":
        env = str(1)
    else:
        env = str(0)
    add_record(username_input, position_type, env)


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




