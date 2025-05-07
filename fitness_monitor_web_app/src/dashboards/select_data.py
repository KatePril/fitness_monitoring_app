from fitness_monitor_web_app.src.entities.health_data import HealthData

SELECT_USERNAME_QUERY = """
    SELECT username
    FROM app_user
    WHERE user_id = %s
"""

SELECT_LATEST_RECORD = """
    SELECT *
    FROM health_data
    WHERE user_id = %s
    ORDER BY "timestamp" DESC
    LIMIT 1;
"""

def select_latest_record(user_id, cursor):
    cursor.execute(SELECT_LATEST_RECORD, (user_id,))
    return HealthData.from_tuple(cursor.fetchone())

def select_username(user_id, cursor):
    cursor.execute(SELECT_USERNAME_QUERY, (user_id,))
    return cursor.fetchone()[0]