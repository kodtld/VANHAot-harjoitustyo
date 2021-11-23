import unittest
from Login_Screen import *
from src.Login_Screen import Login, User_name, User_password


class TestLogin(unittest.TestCase):

    def test_register_username(self):
        Login()
        self.assertEqual(str(Login()), "Wrong username or password")


