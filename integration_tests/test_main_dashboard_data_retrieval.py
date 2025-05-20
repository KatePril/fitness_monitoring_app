import datetime
import unittest
from unittest.mock import Mock

from fitness_monitor_web_app.src.dashboards.queries.select_data import TodayDataSelector
from fitness_monitor_web_app.src.entities.health_data import HealthData


class TestMainDashboardDataRetrieval(unittest.TestCase):
    def setUp(self):
        self.mock_cursor = Mock()
        self.today_data_selector = TodayDataSelector(self.mock_cursor)

    def test_select_latest_record(self):
        fetched_data = (843, datetime.datetime(2025, 5, 7, 13, 14, 5, 473097), 106, 95, 1, 0.04, 1)
        self.mock_cursor.fetchone.return_value = fetched_data

        result = self.today_data_selector.select_latest_record(1)
        self.mock_cursor.execute.assert_called_once_with(
            self.today_data_selector.SELECT_LATEST_RECORD_QUERY,
            (1,)
        )
        self.assertEqual(result, HealthData.from_tuple(fetched_data))

    def test_select_today_total(self):
        fetched_data = (451, 18.04)
        self.mock_cursor.fetchone.return_value = fetched_data

        result = self.today_data_selector.select_today_total(1)
        self.mock_cursor.execute.assert_called_once_with(
            self.today_data_selector.SELECT_TODAY_TOTAL_QUERY,
            (1,)
        )
        self.assertEqual(result, fetched_data)



if __name__ == '__main__':
    unittest.main()
