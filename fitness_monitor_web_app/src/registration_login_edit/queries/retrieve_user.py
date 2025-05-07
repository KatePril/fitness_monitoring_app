from fitness_monitor_web_app.src.registration_login_edit.password import check_password
from fitness_monitor_web_app.src.entities.user import User

SELECT_BY_EMAIL_QUERY = """
    SELECT user_id, password
    FROM app_user
    WHERE email = %s
"""

SELECT_USER_BY_ID = """
    SELECT *
    FROM app_user
    WHERE user_id = %s
"""

def check_login(email, password, cursor):
    cursor.execute(SELECT_BY_EMAIL_QUERY, (email,))
    fetched_data = cursor.fetchone()

    if fetched_data:
        if check_password(password, fetched_data[1]):
            return fetched_data[0]
    else:
        return None

def retrieve_user(user_id, cursor):
    cursor.execute(SELECT_USER_BY_ID, (user_id,))
    fetched_data = cursor.fetchone()
    if fetched_data:
        return  User.from_tuple(fetched_data)
    else:
        return None