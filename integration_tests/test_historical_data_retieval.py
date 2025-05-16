import datetime
import unittest
from unittest.mock import Mock

from fitness_monitor_web_app.src.dashboards.queries.select_historical_charts_data import *


class TestHistoricalDataRetrieval(unittest.TestCase):
    def setUp(self):
        self.mock_cursor = Mock()

    def test_week_data_retrieval(self):
        fetched_data = [
            (datetime.date(2025, 5, 10), 0, 0.0), (datetime.date(2025, 5, 11), 0, 0.0),
            (datetime.date(2025, 5, 12), 0, 0.0), (datetime.date(2025, 5, 13), 0, 0.0),
            (datetime.date(2025, 5, 14), 0, 0.0), (datetime.date(2025, 5, 15), 7216, 288.64),
            (datetime.date(2025, 5, 16), 8687, 347.48)
        ]
        self.mock_cursor.fetchall.return_value = fetched_data

        result = select_last_week_data(1, self.mock_cursor)
        self.mock_cursor.execute.assert_called_once_with(
            SELECT_LAST_WEEK_STATISTICS,
            (1,)
        )
        self.assertEqual(result, fetched_data)

    def test_month_data_retrieval(self):
        fetched_data = [
            (datetime.date(2025, 4, 16), 0, 0.0), (datetime.date(2025, 4, 17), 0, 0.0), (datetime.date(2025, 4, 18), 0, 0.0),
            (datetime.date(2025, 4, 19), 0, 0.0), (datetime.date(2025, 4, 20), 0, 0.0), (datetime.date(2025, 4, 21), 0, 0.0),
            (datetime.date(2025, 4, 22), 0, 0.0), (datetime.date(2025, 4, 23), 0, 0.0), (datetime.date(2025, 4, 24), 0, 0.0),
            (datetime.date(2025, 4, 25), 0, 0.0), (datetime.date(2025, 4, 26), 0, 0.0), (datetime.date(2025, 4, 27), 0, 0.0),
            (datetime.date(2025, 4, 28), 0, 0.0), (datetime.date(2025, 4, 29), 0, 0.0), (datetime.date(2025, 4, 30), 0, 0.0),
            (datetime.date(2025, 5, 1), 0, 0.0), (datetime.date(2025, 5, 2), 0, 0.0), (datetime.date(2025, 5, 3), 0, 0.0),
            (datetime.date(2025, 5, 4), 1866, 74.63), (datetime.date(2025, 5, 5), 0, 0.0), (datetime.date(2025, 5, 6), 0, 0.0),
            (datetime.date(2025, 5, 7), 59039, 2361.57), (datetime.date(2025, 5, 8), 0, 0.0), (datetime.date(2025, 5, 9), 0, 0.0),
            (datetime.date(2025, 5, 10), 0, 0.0), (datetime.date(2025, 5, 11), 0, 0.0), (datetime.date(2025, 5, 12), 0, 0.0),
            (datetime.date(2025, 5, 13), 0, 0.0), (datetime.date(2025, 5, 14), 0, 0.0), (datetime.date(2025, 5, 15), 21639, 865.56),
            (datetime.date(2025, 5, 16), 26108, 1044.32)
        ]
        self.mock_cursor.fetchall.return_value = fetched_data

        result = select_last_month_data(1, self.mock_cursor)
        self.mock_cursor.execute.assert_called_once_with(
            SELECT_LAST_MONTH_STATISTICS,
            (1,)
        )
        self.assertEqual(result, fetched_data)

    def test_year_data_retrieval(self):
        fetched_data = [
            ('05-2024', 0, 0.0), ('06-2024', 0, 0.0), ('07-2024', 0, 0.0), ('08-2024', 0, 0.0), ('09-2024', 0, 0.0),
            ('10-2024', 0, 0.0), ('11-2024', 0, 0.0), ('12-2024', 0, 0.0), ('01-2025', 0, 0.0), ('02-2025', 0, 0.0),
            ('03-2025', 0, 0.0), ('04-2025', 0, 0.0), ('05-2025', 108652, 4346.079)
        ]
        self.mock_cursor.fetchall.return_value = fetched_data

        result = select_last_year_data(1, self.mock_cursor)
        self.mock_cursor.execute.assert_called_once_with(
            SELECT_LAST_YEAR_STATISTICS,
            (1,)
        )
        self.assertEqual(result, fetched_data)