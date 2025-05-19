from flask import render_template
from fitness_monitor_web_app.src.dashboards.queries.select_data import TodayDataSelector
from fitness_monitor_web_app.src.registration_login_edit.queries.select_user import UserSelector
from fitness_monitor_web_app.src.dashboards.queries.select_today_charts_data import TodayChartsDataSelector
from fitness_monitor_web_app.src.dashboards.chart import Chart
from fitness_monitor_web_app.src.database_connection import cursor

class MainDashboardProvider:
    
    @staticmethod
    def get_main_dashboard(user_id):
        user_selector = UserSelector(cursor)
        username = user_selector.select_username(user_id)

        today_data_selector = TodayDataSelector(cursor)
        heath_data = today_data_selector.select_latest_record(user_id)
        today_total = today_data_selector.select_today_total(user_id)

        today_charts_data_selector = TodayChartsDataSelector(cursor)
        today_charts_data = today_charts_data_selector.select_today_charts_data(user_id)
        steps_chart = MainDashboardProvider.__create_today_steps_chart(today_charts_data)
        calories_chart = MainDashboardProvider.__create_today_calories_chart(today_charts_data)
    
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
    
    @staticmethod
    def __create_today_steps_chart(today_charts_data):
        steps = [hour_data[1] for hour_data in today_charts_data]
        chart = Chart(steps)
        return chart.get_chart_image()
    
    @staticmethod
    def __create_today_calories_chart(today_charts_data):
        steps = [hour_data[2] for hour_data in today_charts_data]
        chart = Chart(steps)
        return chart.get_chart_image()