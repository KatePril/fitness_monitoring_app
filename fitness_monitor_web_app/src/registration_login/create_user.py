from fitness_monitor_web_app.src.entities.user import User

INSERTION_QUERY = """
    INSERT INTO app_user(username, email, password, weight, height)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING user_id
"""

def create_user(user: User, cursor, conn) -> int|None:
    print(user.username)
    try:
        cursor.execute(
            INSERTION_QUERY,
            (
                user.username,
                user.email,
                user.password,
                user.weight,
                user.height
            )
        )
        user_id = cursor.fetchone()[0]
        conn.commit()
        return user_id
    except Exception as e:
        conn.rollback()
        print("Error:", e)
        return None