from flask import render_template, session, redirect
from fitness_monitor_web_app.src.registration_login_edit.queries.retrieve_user import retrieve_user, check_login
from fitness_monitor_web_app.src.registration_login_edit.queries.update_user import update_user
from fitness_monitor_web_app.src.registration_login_edit.password import get_password_hash
from fitness_monitor_web_app.src.database_connection import cursor, conn

def edit_account_get():
    user_id = session.get('user_id')
    user = retrieve_user(user_id, cursor)
    if user is not None:
        return render_template(
            "edit_account_page.html",
            user=user,
        )

def edit_account_post(form):
    user_id = session.get('user_id')
    user = retrieve_user(user_id, cursor)
    if user is not None:
        form_type = form.get('form_type')
        if form_type == 'update_user':
            user.update(
                username=form.get('username'),
                email=form.get('email'),
                weight=form.get('weight'),
                height=form.get('height'),
            )
            if update_user(user, cursor, conn):
                return render_template(
                    "edit_account_page.html",
                    user=user,
                    message="Profile updated successfully"
                )
            return render_template(
                "edit_account_page.html",
                user=user,
                message="Failed to update profile"
            )
        elif form_type == 'update_password':
            if check_login(user.email, form.get("old_password"), cursor):
                user.password = get_password_hash(form.get("new_password"))
                return render_template(
                    "edit_account_page.html",
                    user=user,
                    password_message="Password updated successfully"
                )
            return render_template(
                "edit_account_page.html",
                user=user,
                password_message="The old password is incorrect"
            )
        return redirect("/edit-profile")