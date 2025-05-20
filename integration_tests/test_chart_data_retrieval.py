import unittest
from unittest.mock import Mock

from fitness_monitor_web_app.src.dashboards.queries.select_today_charts_data import TodayChartsDataSelector


class TestChartDataRetrieval(unittest.TestCase):
    def setUp(self):
        self.mock_cursor = Mock()
        self.today_charts_data_selector = TodayChartsDataSelector(self.mock_cursor)

    def test_select_today_charts_data(self):
        fetched_data = [
            (0, 0, 0.0), (1, 0, 0.0), (2, 0, 0.0), (3, 0, 0.0),
            (4, 0, 0.0), (5, 0, 0.0), (6, 0, 0.0), (7, 0, 0.0),
            (8, 0, 0.0), (9, 0, 0.0), (10, 0.0, 0.0), (11, 0.0, 0.0),
            (12, 0.0, 0.0), (13, 0.0, 0.0), (14, 0.0, 0.0), (15, 0.0, 0.0),
            (16, 0.0, 0.0), (17, 0.0, 0.0), (18, 0.0, 0.0), (19, 0.0, 0.0),
            (20, 0.0, 0.0), (21, 0.0, 0.0), (22, 0.0, 0.0), (23, 0.0, 0.0),
        ]
        self.mock_cursor.fetchall.return_value = fetched_data

        result = self.today_charts_data_selector.select_today_charts_data(1)
        self.mock_cursor.execute.assert_called_once_with(
            self.today_charts_data_selector.SELECT_TODAY_STATISTICS_QUERY,
            (1,)
        )
        self.assertEqual(result, fetched_data)


if __name__ == '__main__':
    unittest.main()
