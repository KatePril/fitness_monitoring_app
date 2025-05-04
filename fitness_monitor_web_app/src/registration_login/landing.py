from flask import render_template, session
from fitness_monitor_web_app.src.registration_login.check_login import check_login
from fitness_monitor_web_app.src.database_connection import cursor, conn
from fitness_monitor_web_app.src.entities.user import User
from fitness_monitor_web_app.src.registration_login.create_user import create_user
from fitness_monitor_web_app.src.registration_login.password import get_password_hash

def process_landing(form):
    form_type = form.get("form_type")
    if form_type == "sign_in":
        user_id = check_login(
            email=form.get("login_email"),
            password=form.get("login_password"),
            cursor=cursor,
        )
        if user_id is None:
            message = "Email or password is incorrect"
            return render_template("landing_page.html", message=message)
    elif form_type == "sign_up":
        user = User.from_dict(form)
        user.password = get_password_hash(user.password)
        user_id = create_user(user, cursor, conn)
        session["user_id"] = user_id
    return render_template("landing_page.html", message="Success")