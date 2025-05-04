import unittest
from unittest.mock import Mock, call
from types import SimpleNamespace

from ingestion_api.insert_health_data import insert_health_data
from ingestion_api.entities.health_data import HealthData

class TestInsertHealthData(unittest.TestCase):
    def setUp(self):
        self.mock_cursor = Mock()
        self.mock_conn = Mock()

        self.health_data = HealthData({
            "timestamp": "2025-05-04 12:00:00",
            "heart_rate": 72,
            "saturation": 98,
            "steps": 5,
            "calories": 0.2,
            "user_id": 1
        })

    def test_insert_successful(self):
        result = insert_health_data(self.health_data, self.mock_cursor, self.mock_conn)

        self.mock_cursor.execute.assert_called_once()
        self.mock_conn.commit.assert_called_once()
        self.mock_conn.rollback.assert_not_called()
        self.assertEqual(result, "OK")

    def test_insert_failure(self):
        self.mock_cursor.execute.side_effect = Exception("DB error")

        result = insert_health_data(self.health_data, self.mock_cursor, self.mock_conn)

        self.mock_conn.rollback.assert_called_once()
        self.mock_conn.commit.assert_not_called()
        self.assertEqual(result, "ERROR")

if __name__ == '__main__':
    unittest.main()
