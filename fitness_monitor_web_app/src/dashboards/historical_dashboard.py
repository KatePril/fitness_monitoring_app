from flask import render_template
from fitness_monitor_web_app.src.dashboards.queries.select_data import select_username
from fitness_monitor_web_app.src.dashboards.queries.select_historical_charts_data import (
    select_last_week_data, 
    select_last_month_data, 
    select_last_year_data
)
from fitness_monitor_web_app.src.dashboards.charts.chart import Chart
from fitness_monitor_web_app.src.database_connection import cursor


class HistoricalDashboardProvider:
    
    @staticmethod
    def get_historical_dashboard(user_id):
        username = select_username(user_id, cursor)
        last_week_data = select_last_week_data(user_id, cursor)
        last_week_charts = HistoricalDashboardProvider.__create_historical_charts(last_week_data)
        last_month_data = select_last_month_data(user_id, cursor)
        last_month_charts = HistoricalDashboardProvider.__create_historical_charts(last_month_data)
        last_year_data = select_last_year_data(user_id, cursor)
        last_year_charts = HistoricalDashboardProvider.__create_historical_charts(last_year_data)
    
        return render_template(
            'historical_charts.html',
            username=username,
            steps_week=last_week_charts.get("steps_chart"),
            calories_week=last_week_charts.get("calories_chart"),
            steps_month=last_month_charts.get("steps_chart"),
            calories_month=last_month_charts.get("calories_chart"),
            steps_year=last_year_charts.get("steps_chart"),
            calories_year=last_year_charts.get("calories_chart"),
        )
        
    @staticmethod    
    def __create_historical_charts(historical_data_list):
        dates = [historical_data[0] for historical_data in historical_data_list]
        steps = [historical_data[1] for historical_data in historical_data_list]
        calories = [historical_data[2] for historical_data in historical_data_list]
        steps_chart = Chart(steps,rotation=25, categories=dates)
        calories_chart = Chart(calories, rotation=25, categories=dates)
        return {
            "steps_chart": steps_chart.get_chart_image(), 
            "calories_chart": calories_chart.get_chart_image()
        }