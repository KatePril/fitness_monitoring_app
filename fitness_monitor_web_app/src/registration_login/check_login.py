from fitness_monitor_web_app.src.registration_login.password import check_password

SELECT_BY_EMAIL_QUERY = """
    SELECT user_id, password
    FROM app_user
    WHERE email = %s
"""

def check_login(email, password, cursor):
    cursor.execute(SELECT_BY_EMAIL_QUERY, (email,))
    fetched_data = cursor.fetchone()

    if fetched_data:
        if check_password(password, fetched_data[1]):
            return fetched_data[0]
    else:
        return None