import unittest
from ingestion_api.entities.health_data import HealthData

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.sample_input = {
            "timestamp": "2025-05-03 19:10:46.700203",
            "heart_rate": 75,
            "saturation": 98,
            "steps": 5,
            "calories": 0.2,
            "user_id": 1
        }
        self.health_data = HealthData(self.sample_input)

    def test_fields_parsing_calories_calculation(self):
        self.assertEqual(self.health_data.timestamp, self.sample_input["timestamp"])
        self.assertEqual(self.health_data.heart_rate, self.sample_input["heart_rate"])
        self.assertEqual(self.health_data.saturation, self.sample_input["saturation"])
        self.assertEqual(self.health_data.steps, self.sample_input["steps"])
        self.assertEqual(self.health_data.calories, self.sample_input["calories"])
        self.assertEqual(self.health_data.user_id, self.sample_input["user_id"])

if __name__ == '__main__':
    unittest.main()
