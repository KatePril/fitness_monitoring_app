import unittest
from unittest.mock import Mock

from fitness_monitor_web_app.src.registration_login.check_login import check_login
from fitness_monitor_web_app.src.registration_login.password import get_password_hash

class TestCheckUserRetrieval(unittest.TestCase):
    def setUp(self):
        self.cursor = Mock()

    def test_login_successful(self):
        password = "secret123"
        hashed_password = get_password_hash(password)

        self.cursor.fetchone.return_value = (1, hashed_password)

        user_id = check_login("mark@example.com", password, self.cursor)

        self.cursor.execute.assert_called_once_with(
            "\n    SELECT user_id, password\n    FROM app_user\n    WHERE email = %s\n",
            ("mark@example.com",)
        )
        self.assertEqual(user_id, 1)

    def test_login_wrong_password(self):
        hashed = get_password_hash("the_correct_password")

        self.cursor.fetchone.return_value = (42, hashed)

        user_id = check_login("mark@example.com", "wrong_password", self.cursor)
        self.assertIsNone(user_id)

    def test_login_email_not_found(self):
        self.cursor.fetchone.return_value = None

        user_id = check_login("mark@example.com", "irrelevant", self.cursor)
        self.assertIsNone(user_id)

if __name__ == "__main__":
    unittest.main()
