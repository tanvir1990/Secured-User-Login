import unittest
from Code.enrol import *
from Code.login import *
from Code.access_control_mechanism import *
from Code.password_control import *
import io
from contextlib import redirect_stdout
import warnings


class TestCalc(unittest.TestCase):
    def test_check_user_password(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            check_user_password('John', '123456')
        self.assertEqual(text_trap.getvalue(), "Failed: Password must be between 8-12 characters\n")

    def test_check_user_password_2(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            check_user_password('JohnJohn', 'JohnJohn')
        self.assertEqual(text_trap.getvalue(), "Failed: Password is Same as User Name\n")

    def test_login_verification_1(self):
        enrol_user("Tanvir", "abc123123!", "Premium_Client")
        permission1 = login_verification("Tanvir", "abc123123!", "Regular_Client", 0)
        assert permission1 == "Access Granted"


    def test_login_verification_2(self):
        enrol_user("John", "123456", "Regular_Client")
        permission2 = login_verification("John", "123456", "Regular_Client", 0)
        assert permission2 == "Access Granted"

    def test_login_verification_3(self):
        enrol_user("Bob", "abcdefgh!", "Teller")
        permission3 = login_verification("John", "abcdef", "Employee_Teller", 1)
        assert permission3 == "Login Failed"

    def test_verify_position(self):
        assert verify_position('Regular_Client') == True

    def test_check_password(self):
        assert check_user_password('Ron', 'afgA1!@A9') == True

    def test_check_password(self):
        assert check_user_password('Ron', 'afgAbc!123') == False

    def test_check_password(self):
        assert check_user_password('Ron', 'Password!12') == False

    def test_check_password(self):
        assert check_user_password('Ron', 'abc12!34AC') == False

    def test_check_password(self):
        assert check_user_password('Ron', 'Ron!34AC') == False

    def test_can_access_role_operations(self):

        result = {
            "role_Id": "02",
            "role_type": "Premium_Client",
            "operations": {
                "1": "View-Account Balance",
                "2": "Modify-Investment Portfolio",
                "3": "View-Contact Details of Financial Planner and Investment Analyst"
            }
        }
        assert can_access_roles_operations("Premium_Client") == result

    def test_password_file(self):
        user_name = "Mischa_Lowery"
        position = "Regular_Client"
        add_record(user_name.strip(), position.strip(), '0')
        returned_uname, returned_env = read_role(user_name)
        self.assertEqual(position, returned_uname, 'Check User Name in the Record')

    def test_enrol_user(self):
        user_name = "Willow_Garza"
        position = "Teller"
        add_record(user_name.strip(), position.strip(), '0')
        returned_uname, returned_env = read_role(user_name)
        self.assertEqual(position, returned_uname, 'Check User Name in the Record')


if __name__ == '__main__':
    unittest.main()

