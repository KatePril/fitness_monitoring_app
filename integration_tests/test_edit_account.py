import unittest
from unittest.mock import Mock

from fitness_monitor_web_app.src.registration_login_edit.queries.update_user import *
from fitness_monitor_web_app.src.entities.user import User

class TestEditAccount(unittest.TestCase):
    def setUp(self):
        self.mock_cursor = Mock()
        self.mock_conn = Mock()

        self.user = User(
            username='mark',
            email='mark@example.com',
            password='scrypt:32768:8:1$7nzOB8PIG8dlIPYc$92d5d57a3074f9f4aadeff323761d84c28884ffb653c099c312a56551313a95f36f79c5d99e8bcb5cfa55876a37ebbce93b3dec6c6b74962cbd9ab46ab42f4c1',
            weight=90.2,
            height=188.1
        )

    def test_update_user_successful(self):
        result = update_user(self.user, self.mock_cursor, self.mock_conn)

        self.mock_cursor.execute.assert_called_once()
        self.mock_conn.commit.assert_called_once()
        self.mock_conn.rollback.assert_not_called()
        self.assertTrue(result)

    def test_update_user_failure(self):
        self.mock_cursor.execute.side_effect = Exception("DB error")
        result = update_password(self.user, self.mock_cursor, self.mock_conn)

        self.mock_conn.rollback.assert_called_once()
        self.mock_conn.commit.assert_not_called()
        self.assertFalse(result)

    def test_update_password_successful(self):
        result = update_password(self.user, self.mock_cursor, self.mock_conn)

        self.mock_cursor.execute.assert_called_once()
        self.mock_conn.commit.assert_called_once()
        self.mock_conn.rollback.assert_not_called()
        self.assertTrue(result)

    def test_update_password_failure(self):
        self.mock_cursor.execute.side_effect = Exception("DB error")
        result = update_password(self.user, self.mock_cursor, self.mock_conn)

        self.mock_conn.rollback.assert_called_once()
        self.mock_conn.commit.assert_not_called()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
