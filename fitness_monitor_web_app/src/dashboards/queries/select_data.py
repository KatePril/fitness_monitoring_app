from fitness_monitor_web_app.src.entities.health_data import HealthData

class TodayDataSelector:
    SELECT_LATEST_RECORD_QUERY = """
        SELECT *
        FROM health_data
        WHERE user_id = %s
        ORDER BY "timestamp" DESC
        LIMIT 1;
    """

    SELECT_TODAY_TOTAL_QUERY = """
        SELECT SUM(steps) AS total_steps, SUM(calories) AS total_calories
        FROM health_data
        WHERE DATE("timestamp") = CURRENT_DATE
          AND user_id = %s;
    """

    def __init__(self, cursor):
        self.cursor = cursor

    def select_latest_record(self, user_id):
        self.cursor.execute(self.SELECT_LATEST_RECORD_QUERY, (user_id,))
        data = self.cursor.fetchone()
        return HealthData.from_tuple(data)

    def select_today_total(self, user_id):
        self.cursor.execute(self.SELECT_TODAY_TOTAL_QUERY, (user_id,))
        return self.cursor.fetchone()
