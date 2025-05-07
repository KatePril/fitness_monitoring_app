UPDATE_USER = """
    UPDATE app_user
    SET username=%s, email=%s, password=%s, weight=%s, height=%s
    WHERE user_id=%s;
"""


def update_user(user, cursor, conn):
    try:
        cursor.execute(
            UPDATE_USER,
            (
                user.username,
                user.email,
                user.password,
                user.weight,
                user.height,
                user.user_id
            )
        )
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print("Error:", e)
        return False