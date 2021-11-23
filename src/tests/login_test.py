import unittest
from Login_Screen import *

class TestLogin(unittest.TestCase):
    def setUp(self):
        pass

    def test_register_username(self):
        Usna = "testi"
        Uspa = "testisalasana"
        reader = ["kodtld","salasana"]
        Login()
        self.assertEqual(str(Login()), "Wrong username or password")