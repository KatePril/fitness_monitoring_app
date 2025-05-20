class UserCreator:
    USER_INSERTION_QUERY = """
        INSERT INTO app_user(username, email, password, weight, height)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING user_id
    """

    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def create_user(self, user) -> int|None:
        try:
            self.cursor.execute(
                self.USER_INSERTION_QUERY,
                (
                    user.username,
                    user.email,
                    user.password,
                    user.weight,
                    user.height
                )
            )
            user_id = self.cursor.fetchone()[0]
            self.conn.commit()
            return user_id
        except Exception as e:
            self.conn.rollback()
            print("Error:", e)
            return None