from fitness_monitor_web_app.src.entities.health_data import HealthData

SELECT_USERNAME_QUERY = """
    SELECT username
    FROM app_user
    WHERE user_id = %s
"""

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

def select_latest_record(user_id, cursor):
    cursor.execute(SELECT_LATEST_RECORD_QUERY, (user_id,))
    data = cursor.fetchone()
    return HealthData.from_tuple(data)

def select_username(user_id, cursor):
    cursor.execute(SELECT_USERNAME_QUERY, (user_id,))
    return cursor.fetchone()[0]

def select_today_total(user_id, cursor):
    cursor.execute(SELECT_TODAY_TOTAL_QUERY, (user_id,))
    return cursor.fetchone()