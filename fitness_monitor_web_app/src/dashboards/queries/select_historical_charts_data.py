SELECT_LAST_WEEK_STATISTICS = """
    WITH days AS (
      SELECT DATE(
        generate_series(
          CURRENT_DATE - INTERVAL '6 days',
          CURRENT_DATE,
          INTERVAL '1 day'
        )
      ) AS day
    ),
    aggregated_data AS (
      SELECT
        timestamp::date AS day,
        SUM(steps) AS total_steps,
        SUM(calories) AS total_calories
      FROM health_data
      WHERE DATE("timestamp") >= CURRENT_DATE - INTERVAL '6 days'
        AND user_id = %s
      GROUP BY DATE("timestamp")
    )
    SELECT
      d.day,
      COALESCE(a.total_steps, 0) AS total_steps,
      COALESCE(a.total_calories, 0) AS total_calories
    FROM days d
    LEFT JOIN aggregated_data a ON d.day = a.day
    ORDER BY d.day;
"""

SELECT_LAST_MONTH_STATISTICS = """
    WITH days AS (
      SELECT DATE(generate_series(
        CURRENT_DATE - INTERVAL '1 month',
        CURRENT_DATE,
        INTERVAL '1 day'
      ))AS day
    ),
    aggregated_data AS (
      SELECT
        DATE(timestamp) AS day,
        SUM(steps) AS total_steps,
        SUM(calories) AS total_calories
      FROM health_data
      WHERE DATE(timestamp) >= CURRENT_DATE - INTERVAL '1 month'
      GROUP BY DATE(timestamp)
    )
    SELECT
      d.day,
      COALESCE(a.total_steps, 0) AS total_steps,
      COALESCE(a.total_calories, 0) AS total_calories
    FROM days d
    LEFT JOIN aggregated_data a ON d.day = a.day
    ORDER BY d.day;
"""

SELECT_LAST_YEAR_STATISTICS = """
    WITH months AS (
      SELECT DATE(
        generate_series(
          date_trunc('month', CURRENT_DATE) - INTERVAL '12 months',
          date_trunc('month', CURRENT_DATE),
          interval '1 month'
        )
      ) AS month_start
    ),
    aggregated_data AS (
      SELECT
        DATE(date_trunc('month', timestamp)) AS month_start,
        SUM(steps) AS total_steps,
        SUM(calories) AS total_calories
      FROM health_data
      WHERE timestamp >= date_trunc('month', CURRENT_DATE) - INTERVAL '12 months'
      GROUP BY date_trunc('month', timestamp)
    )
    SELECT
      TO_CHAR(m.month_start, 'MM-YYYY') AS month,
      COALESCE(a.total_steps, 0) AS total_steps,
      COALESCE(a.total_calories, 0) AS total_calories
    FROM months m
    LEFT JOIN aggregated_data a ON m.month_start = a.month_start
    ORDER BY m.month_start;
"""

def select_last_week_data(user_id, cursor):
    cursor.execute(SELECT_LAST_WEEK_STATISTICS, (user_id,))
    return cursor.fetchall()

def select_last_month_data(user_id, cursor):
    cursor.execute(SELECT_LAST_MONTH_STATISTICS, (user_id,))
    return cursor.fetchall()

def select_last_year_data(user_id, cursor):
    cursor.execute(SELECT_LAST_YEAR_STATISTICS, (user_id,))
    return cursor.fetchall()
