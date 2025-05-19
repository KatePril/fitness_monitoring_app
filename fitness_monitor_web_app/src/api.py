from flask import Flask, render_template, request, session, redirect
from dotenv import load_dotenv
import os

from fitness_monitor_web_app.src.registration_login_edit.landing import LandingProvider
from fitness_monitor_web_app.src.registration_login_edit.edit_account import EditAccountPageProvider
from fitness_monitor_web_app.src.dashboards.main_dashboard import MainDashboardProvider
from fitness_monitor_web_app.src.dashboards.historical_dashboard import HistoricalDashboardProvider
from fitness_monitor_web_app.src.calculator.calculator_page import CalculatorPageProvider


app = Flask(__name__)

load_dotenv()
app.secret_key = os.getenv("APP_SECRET_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return LandingProvider.process_landing(request.form)
    return render_template("landing_page.html")

@app.route("/dashboard", methods=["GET"])
def main_dashboard():
    user_id = session.get("user_id")
    if user_id is None:
        return redirect("/")
    return MainDashboardProvider.get_main_dashboard(user_id)

@app.route("/historical_dashboards", methods=["GET"])
def historical_dashboards():
    user_id = session.get("user_id")
    if user_id is None:
        return redirect("/")
    return HistoricalDashboardProvider.get_historical_dashboard(user_id)

@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    user_id = session.get("user_id")
    if request.method == "POST":
        return CalculatorPageProvider.calculator_page_post(request.form, user_id)
    else:
        return CalculatorPageProvider.calculator_page_get(user_id)

@app.route('/edit_profile', methods=["GET", "POST"])
def edit_profile():
    if request.method == "POST":
        return EditAccountPageProvider.edit_account_post(request.form)
    else:
        return EditAccountPageProvider.edit_account_get()

@app.route('/sign_out')
def sign_out():
    session.pop("user_id")
    return redirect("/")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)