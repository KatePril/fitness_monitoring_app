import unittest
from fitness_monitor_web_app.src.registration_login.password import get_password_hash, check_password_hash

class UnitTestRegistrationLogin(unittest.TestCase):
    def test_password_hash_generation(self):
        password = "something1234"
        password_hash = get_password_hash(password)
        self.assertNotEqual(password_hash, password)
        self.assertNotEqual(len(password_hash), len(password))

    def test_check_correct_password_hash(self):
        password = "something1234"
        password_hash = get_password_hash(password)
        self.assertTrue(check_password_hash(password_hash, password))

    def test_check_incorrect_password_hash(self):
        password = "something1234"
        password_hash = get_password_hash(password)
        self.assertFalse(check_password_hash(password_hash, "1234something"))


if __name__ == '__main__':
    unittest.main()
