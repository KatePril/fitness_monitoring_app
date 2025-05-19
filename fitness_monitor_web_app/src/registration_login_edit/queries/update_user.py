class UserUpdater:
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

    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def update_user(self, user):
        try:
            self.cursor.execute(
                self.UPDATE_USER_QUERY,
                (
                    user.username,
                    user.email,
                    user.weight,
                    user.height,
                    user.user_id
                )
            )
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print("Error:", e)
            return False

    def update_password(self, user):
        try:
            self.cursor.execute(
                self.UPDATE_PASSWORD_QUERY,
                (
                    user.password,
                    user.user_id
                )
            )
            self.conn.commit()
            return True
        except Exception as e:
            self.conn.rollback()
            print("Error:", e)
            return False