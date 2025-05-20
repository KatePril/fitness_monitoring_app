from flask import render_template, session, redirect
from fitness_monitor_web_app.src.registration_login_edit.queries.select_user import UserSelector
from fitness_monitor_web_app.src.registration_login_edit.queries.update_user import UserUpdater
from fitness_monitor_web_app.src.registration_login_edit.password import PasswordHasher
from fitness_monitor_web_app.src.database_connection import cursor, conn


class EditAccountPageProvider:

    @staticmethod
    def edit_account_get():
        user_id = session.get('user_id')
        user = UserSelector(cursor).select_user(user_id)
        if user is not None:
            return render_template(
                "edit_account_page.html",
                user=user,
            )

    @staticmethod
    def edit_account_post(form):
        user_id = session.get('user_id')
        user_selector = UserSelector(cursor)
        user = user_selector.select_user(user_id)
        if user is not None:
            form_type = form.get('form_type')
            if form_type == 'update_user':
                user.update(
                    username=form.get('username'),
                    email=form.get('email'),
                    weight=form.get('weight'),
                    height=form.get('height'),
                )
                user_updater = UserUpdater(cursor, conn)
                if user_updater.update_user(user):
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
                if user_selector.check_login(user.email, form.get("old_password")):
                    user.password = PasswordHasher.get_password_hash(form.get("new_password"))
                    user_updater = UserUpdater(cursor, conn)
                    if user_updater.update_password(user):
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