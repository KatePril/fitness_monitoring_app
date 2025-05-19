from fitness_monitor_web_app.src.registration_login_edit.password import PasswordHasher
from fitness_monitor_web_app.src.entities.user import User


class UserSelector:
    SELECT_BY_EMAIL_QUERY = """
        SELECT user_id, password
        FROM app_user
        WHERE email = %s
    """

    SELECT_USER_BY_ID_QUERY = """
        SELECT *
        FROM app_user
        WHERE user_id = %s
    """

    SELECT_USERNAME_QUERY = """
        SELECT username
        FROM app_user
        WHERE user_id = %s
    """

    def __init__(self, cursor):
        self.cursor = cursor

    def check_login(self, email, password):
        self.cursor.execute(self.SELECT_BY_EMAIL_QUERY, (email,))
        fetched_data = self.cursor.fetchone()

        if fetched_data:
            if PasswordHasher.check_password(password, fetched_data[1]):
                return fetched_data[0]
        else:
            return None

    def select_user(self, user_id):
        self.cursor.execute(self.SELECT_USER_BY_ID_QUERY, (user_id,))
        fetched_data = self.cursor.fetchone()
        if fetched_data:
            return  User.from_tuple(fetched_data)
        else:
            return None

    def select_username(self, user_id):
        self.cursor.execute(self.SELECT_USERNAME_QUERY, (user_id,))
        return self.cursor.fetchone()[0]