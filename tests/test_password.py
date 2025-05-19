import unittest
from fitness_monitor_web_app.src.registration_login_edit.password import PasswordHasher


class UnitTestRegistrationLogin(unittest.TestCase):
    def test_password_hash_generation(self):
        password = "something1234"
        password_hash = PasswordHasher.get_password_hash(password)
        self.assertNotEqual(password_hash, password)
        self.assertNotEqual(len(password_hash), len(password))

    def test_check_correct_password_hash(self):
        password = "something1234"
        password_hash = PasswordHasher.get_password_hash(password)
        self.assertTrue(PasswordHasher.check_password(password, password_hash))

    def test_check_incorrect_password_hash(self):
        password = "something1234"
        password_hash = PasswordHasher.get_password_hash(password)
        self.assertFalse(PasswordHasher.check_password("1234something", password_hash))


if __name__ == '__main__':
    unittest.main()
