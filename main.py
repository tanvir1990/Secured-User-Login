from Code.password_control import *
from  Code.login import *
from  Code.access_control_mechanism import *
from Code.enrol import *

while True:
    print("\n\nType: \n"
          "1 - To Enrol a User \n"
          "2 - To Login \n"
          "0 - To exit the program")
    opcode = int(input("What would you like to do?\nInput: "))

    if opcode == 1:
        print('Register by typing a Username, Password, and Role.')
        take_user_input()
    elif opcode == 2:
        login_main()
    elif opcode == 0:
        print('Exiting The Program')
        break
    else:
        print ("Invalid Input. Try Again")