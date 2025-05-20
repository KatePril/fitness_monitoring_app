import unittest

from fitness_monitor_web_app.src.calculator.calculator_page import CalculatorPageProvider


class TestStepsCalculator(unittest.TestCase):
    def test_first_case(self):
        expected_result = 19250
        result = CalculatorPageProvider._calculate_steps(3, 30)
        self.assertEqual(expected_result, result)

    def test_second_case(self):
        expected_result = 12833
        result = CalculatorPageProvider._calculate_steps(4, 60)
        self.assertEqual(expected_result, result)



if __name__ == '__main__':
    unittest.main()
