from flask import render_template
from fitness_monitor_web_app.src.dashboards.queries.select_data import select_username
from fitness_monitor_web_app.src.dashboards.queries.select_historical_charts_data import (
    select_last_week_data, 
    select_last_month_data, 
    select_last_year_data
)
from fitness_monitor_web_app.src.dashboards.charts.chart import Chart
from fitness_monitor_web_app.src.database_connection import cursor

def get_historical_dashboard(user_id):
    username = select_username(user_id, cursor)
    last_week_data = select_last_week_data(username, cursor)
    last_week_charts = create_historical_charts(
        last_week_data,
        "Last week's steps statistics",
        "Last week's calories statistics"
    )
    last_month_data = select_last_month_data(username, cursor)
    last_month_charts = create_historical_charts(
        last_month_data,
        "Last month's steps statistics",
        "Last month's calories statistics"
    )
    last_year_data = select_last_year_data(username, cursor)
    last_year_charts = create_historical_charts(
        last_year_data,
        "Last year's steps statistics",
        "Last year's calories statistics"
    )
    
    
def create_historical_charts(historical_data_list, steps_title, calories_title):
    dates = [historical_data[0] for historical_data in historical_data_list]
    steps = [historical_data[1] for historical_data in historical_data_list]
    calories = [historical_data[2] for historical_data in historical_data_list]
    steps_chart = Chart(steps, steps_title, categories=dates)
    calories_chart = Chart(calories, calories_title, categories=dates)
    return {
        "steps_chart": steps_chart.get_chart_image(), 
        "calories_chart": calories_chart.get_chart_image()
    }