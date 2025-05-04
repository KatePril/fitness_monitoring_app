def insert_health_data(health_data, cursor, conn) -> str:
    try:
        query = '''
            INSERT INTO health_data ("timestamp", heart_rate, saturation, steps, calories, user_id)     
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(
            query,
            (
                health_data.timestamp,
                health_data.heart_rate,
                health_data.saturation,
                health_data.steps,
                health_data.calories,
                health_data.user_id
            )
        )
        conn.commit()
        return "OK"
    except Exception as e:
        conn.rollback()
        print("Error:", e)
        return "ERROR"