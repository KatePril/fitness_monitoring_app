import unittest

from data_sources.data_generation.data_generator import DataGenerator


class TestDataGeneration(unittest.TestCase):
    def test_data_generation(self):
        user_id = 1
        data = DataGenerator().generate_fitness_data(user_id)
        self.assertIsNotNone(data.get("timestamp"))
        self.assertIsNotNone(data.get("heart_rate"))
        self.assertIsNotNone(data.get("saturation"))
        self.assertIsNotNone(data.get("steps"))
        self.assertEqual(user_id, data.get("user_id"))
        self.assertEqual(5, len(data.keys()))


if __name__ == '__main__':
    unittest.main()
