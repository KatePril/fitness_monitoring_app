UPDATE_USER_QUERY = """
    UPDATE app_user
    SET username=%s, email=%s, weight=%s, height=%s
    WHERE user_id=%s
"""

UPDATE_PASSWORD_QUERY = """
    UPDATE app_user
    SET password=%s
    WHERE user_id=%s
"""

def update_user(user, cursor, conn):
    try:
        cursor.execute(
            UPDATE_USER_QUERY,
            (
                user.username,
                user.email,
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

def update_password(user, cursor, conn):
    try:
        cursor.execute(
            UPDATE_PASSWORD_QUERY,
            (
                user.password,
                user.user_id
            )
        )
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print("Error:", e)
        return False