from flask import render_template, session
from fitness_monitor_web_app.src.registration_login_edit.queries.retrieve_user import retrieve_user
from fitness_monitor_web_app.src.database_connection import cursor

def edit_account_get():
    user_id = session.get('user_id')
    user = retrieve_user(user_id, cursor)
    if user is not None:
        return render_template(
            "edit_account_page.html",
            user=user,
        )

def edit_account(form):
    user_id = session.get('user_id')