from flask import render_template
from fitness_monitor_web_app.src.dashboards.queries.select_data import select_username, select_latest_record, select_today_total
from fitness_monitor_web_app.src.dashboards.queries.select_today_charts_data import select_today_charts_data
from fitness_monitor_web_app.src.dashboards.charts.chart import Chart
from fitness_monitor_web_app.src.database_connection import cursor

def get_main_dashboard(user_id):
    username = select_username(user_id, cursor)
    heath_data = select_latest_record(user_id, cursor)
    today_total = select_today_total(user_id, cursor)

    today_charts_data = select_today_charts_data(user_id, cursor)
    steps_chart = create_today_calories_chart(today_charts_data)
    calories_chart = create_today_calories_chart(today_charts_data)

    return render_template(
        "main_page.html",
        username=username,
        heart_rate=heath_data.heart_rate if heath_data.heart_rate else "--",
        saturation=heath_data.saturation if heath_data.saturation else "--",
        total_steps=today_total[0] if today_total[0] is not None else 0,
        total_calories=round(today_total[1], 3) if today_total[1] is not None else 0,
        steps_chart=steps_chart,
        calories_chart=calories_chart,
    )

def create_today_steps_chart(today_charts_data):
    steps = [hour_data[1] for hour_data in today_charts_data]
    chart = Chart(steps, "Today's steps statistics")
    return chart.get_chart_image()

def create_today_calories_chart(today_charts_data):
    steps = [hour_data[2] for hour_data in today_charts_data]
    chart = Chart(steps, "Today's calories statistics")
    return chart.get_chart_image()