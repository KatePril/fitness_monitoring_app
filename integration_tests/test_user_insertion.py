import unittest
from unittest.mock import Mock

from fitness_monitor_web_app.src.entities.user import User
from fitness_monitor_web_app.src.registration_login_edit.queries.create_user import create_user

class TestInsertUser(unittest.TestCase):
    def setUp(self):
        self.mock_cursor = Mock()
        self.mock_conn = Mock()

        self.user = User(
            username = 'mark',
            email = 'mark@example.com',
            password = 'scrypt:32768:8:1$7nzOB8PIG8dlIPYc$92d5d57a3074f9f4aadeff323761d84c28884ffb653c099c312a56551313a95f36f79c5d99e8bcb5cfa55876a37ebbce93b3dec6c6b74962cbd9ab46ab42f4c1',
            weight=90.2,
            height=188.1
        )

    def test_insert_successful(self):
        self.mock_cursor.fetchone.return_value = (1,)
        result = create_user(self.user, self.mock_cursor, self.mock_conn)

        self.mock_cursor.execute.assert_called_once()
        self.mock_conn.commit.assert_called_once()
        self.mock_conn.rollback.assert_not_called()
        self.assertEqual(result, 1)

    def test_insert_failure(self):
        self.mock_cursor.execute.side_effect = Exception("DB error")

        result = create_user(self.user, self.mock_cursor, self.mock_conn)

        self.mock_conn.rollback.assert_called_once()
        self.mock_conn.commit.assert_not_called()
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
