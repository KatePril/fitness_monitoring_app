from flask import render_template, session, redirect
from fitness_monitor_web_app.src.registration_login_edit.queries.select_user import UserSelector
from fitness_monitor_web_app.src.database_connection import cursor, conn
from fitness_monitor_web_app.src.entities.user import User
from fitness_monitor_web_app.src.registration_login_edit.queries.create_user import UserCreator
from fitness_monitor_web_app.src.registration_login_edit.password import PasswordHasher


class LandingProvider:

    @staticmethod
    def process_landing(form):
        form_type = form.get("form_type")
        if form_type == "sign_in":
            user_selector = UserSelector(cursor)
            user_id = user_selector.check_login(
                email=form.get("login_email"),
                password=form.get("login_password"),
            )
            if user_id is None:
                message = "Email or password is incorrect"
                return render_template("landing_page.html", message=message)
            session["user_id"] = user_id
        elif form_type == "sign_up":
            user = User.from_dict(form)
            user.password = PasswordHasher.get_password_hash(user.password)
            user_creator = UserCreator(cursor, conn)
            user_id = user_creator.create_user(user)
            session["user_id"] = user_id
        return redirect("/dashboard")