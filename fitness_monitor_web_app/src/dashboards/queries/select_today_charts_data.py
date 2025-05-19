class TodayChartsDataSelector:
    SELECT_TODAY_STATISTICS = """
        WITH hours AS (
          SELECT generate_series(0, 23) AS hour
        ),
        aggregated_data AS (
          SELECT
            EXTRACT(HOUR FROM timestamp) AS hour,
            SUM(steps) AS total_steps,
            SUM(calories) AS total_calories
          FROM health_data
          WHERE DATE("timestamp") = CURRENT_DATE
            AND user_id = %s
          GROUP BY hour
        )
        SELECT
          h.hour,
          COALESCE(a.total_steps, 0) AS total_steps,
          COALESCE(a.total_calories, 0) AS total_calories
        FROM hours h
        LEFT JOIN aggregated_data a ON h.hour = a.hour
        ORDER BY h.hour;
    """

    def __init__(self, cursor):
        self.cursor = cursor

    def select_today_charts_data(self, user_id):
        self.cursor.execute(self.SELECT_TODAY_STATISTICS, (user_id,))
        return self.cursor.fetchall()
