import unittest
from unittest.mock import Mock

from fitness_monitor_web_app.src.entities.user import User
from fitness_monitor_web_app.src.registration_login_edit.queries.select_user import UserSelector
from fitness_monitor_web_app.src.registration_login_edit.password import PasswordHasher

class TestCheckUserRetrieval(unittest.TestCase):
    def setUp(self):
        self.mock_cursor = Mock()
        self.user_selector = UserSelector(self.mock_cursor)

    def test_login_successful(self):
        password = "secret123"
        hashed_password = PasswordHasher.get_password_hash(password)

        self.mock_cursor.fetchone.return_value = (1, hashed_password)

        user_id = self.user_selector.check_login("mark@example.com", password)

        self.mock_cursor.execute.assert_called_once_with(
            self.user_selector.SELECT_BY_EMAIL_QUERY,
            ("mark@example.com",)
        )
        self.assertEqual(user_id, 1)

    def test_login_wrong_password(self):
        hashed = PasswordHasher.get_password_hash("the_correct_password")

        self.mock_cursor.fetchone.return_value = (42, hashed)

        user_id = self.user_selector.check_login("mark@example.com", "wrong_password")
        self.assertIsNone(user_id)

    def test_login_email_not_found(self):
        self.mock_cursor.fetchone.return_value = None
        user_id = self.user_selector.check_login("mark@example.com", "irrelevant")
        self.assertIsNone(user_id)

    def test_retrieve_user_successful(self):
        fetched_data = (1, "mark", "mark@example.com", "<PASSWORD>", 80.2, 185.1)
        user = User(
            username=fetched_data[1],
            email=fetched_data[2],
            password=fetched_data[3],
            weight=fetched_data[4],
            height=fetched_data[5],
            user_id=fetched_data[0]
        )

        self.mock_cursor.fetchone.return_value = fetched_data
        fetched_user = self.user_selector.select_user(1)
        self.assertEqual(fetched_user, user)

    def test_retrieve_user_not_found(self):
        self.mock_cursor.fetchone.return_value = None
        fetched_user = self.user_selector.select_user(1)
        self.assertIsNone(fetched_user)

    def test_select_username(self):
        username = "Ann"
        self.mock_cursor.fetchone.return_value = (username,)

        result = self.user_selector.select_username(1)
        self.mock_cursor.execute.assert_called_once_with(
            self.user_selector.SELECT_USERNAME_QUERY,
            (1,)
        )
        self.assertEqual(result, username)

if __name__ == "__main__":
    unittest.main()
