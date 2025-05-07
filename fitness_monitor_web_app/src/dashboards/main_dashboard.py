from flask import render_template
from fitness_monitor_web_app.src.dashboards.select_data import select_username, select_latest_record, select_today_total
from fitness_monitor_web_app.src.database_connection import cursor

def get_main_dashboard(user_id):
    print("get_main_dashboard")
    username = select_username(user_id, cursor)
    heath_data = select_latest_record(user_id, cursor)
    today_total = select_today_total(user_id, cursor)
    return render_template(
        "main_page.html",
        username=username,
        heart_rate=heath_data.heart_rate if heath_data.heart_rate else "--",
        saturation=heath_data.saturation if heath_data.saturation else "--",
        total_steps=today_total[0] if today_total[0] is not None else 0,
        total_calories=round(today_total[1], 3) if today_total[1] is not None else 0,
    )
