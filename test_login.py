import unittest
from Code.enrol_users import *
from Code.login import *
import io
from contextlib import redirect_stdout


class TestCalc(unittest.TestCase):
    def test_check_user_password(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            check_user_password('John', '123456')
        self.assertEqual(text_trap.getvalue(), "Failed: Password is less than 8 characters\n")

    # def test_check_user_password_2(self):
    #     text_trap = io.StringIO()
    #     with redirect_stdout(text_trap):
    #         check_user_password('JohnJohn', 'JohnJohn')
    #     self.assertEqual(text_trap.getvalue(), "Failed: Password is Same as User Name\n")
    #
    # def test_login_verification_1(self):
    #     enrol_user("Tanvir", "abc123123!", "Premium_Client")
    #     permission1 = login_verification("Tanvir", "abc123123!")
    #     assert permission1 == "Access Granted"
    #
    # def test_login_verification_2(self):
    #     enrol_user("John", "123456", "Regular_Client")
    #     permission2 = login_verification("John", "123456")
    #     assert permission2 == "Access Granted"
    #
    # def test_login_verification_3(self):
    #     enrol_user("Bob", "abcdefgh!", "Teller")
    #     permission3 = login_verification("John", "abcdef")
    #     assert permission3 == "Login Failed"

    def test_verify_position(self):
        assert verify_position('Regular_Client') == True


if __name__ == '__main__':
    unittest.main()
