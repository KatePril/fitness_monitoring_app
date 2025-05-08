import unittest
from unittest.mock import Mock

from fitness_monitor_web_app.src.registration_login_edit.queries.retrieve_user import *
from fitness_monitor_web_app.src.registration_login_edit.password import get_password_hash

class TestCheckUserRetrieval(unittest.TestCase):
    def setUp(self):
        self.mock_cursor = Mock()

    def test_login_successful(self):
        password = "secret123"
        hashed_password = get_password_hash(password)

        self.mock_cursor.fetchone.return_value = (1, hashed_password)

        user_id = check_login("mark@example.com", password, self.mock_cursor)

        self.mock_cursor.execute.assert_called_once_with(
            SELECT_BY_EMAIL_QUERY,
            ("mark@example.com",)
        )
        self.assertEqual(user_id, 1)

    def test_login_wrong_password(self):
        hashed = get_password_hash("the_correct_password")

        self.mock_cursor.fetchone.return_value = (42, hashed)

        user_id = check_login("mark@example.com", "wrong_password", self.mock_cursor)
        self.assertIsNone(user_id)

    def test_login_email_not_found(self):
        self.mock_cursor.fetchone.return_value = None
        user_id = check_login("mark@example.com", "irrelevant", self.mock_cursor)
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
        fetched_user = retrieve_user(1, self.mock_cursor)
        self.assertEqual(fetched_user, user)

    def test_retrieve_user_not_found(self):
        self.mock_cursor.fetchone.return_value = None
        fetched_user = retrieve_user(1, self.mock_cursor)
        self.assertIsNone(fetched_user)

if __name__ == "__main__":
    unittest.main()
