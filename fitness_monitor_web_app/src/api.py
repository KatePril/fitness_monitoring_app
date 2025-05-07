from flask import Flask, render_template, request, session, redirect
from dotenv import load_dotenv
import os

from fitness_monitor_web_app.src.registration_login.landing import process_landing
from fitness_monitor_web_app.src.dashboards.main_dashboard import get_main_dashboard
app = Flask(__name__)

load_dotenv()
app.secret_key = os.getenv("APP_SECRET_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return process_landing(request.form)
    return render_template("landing_page.html")

@app.route("/dashboard", methods=["GET"])
def main_dashboard():
    user_id = session.get("user_id")
    if user_id is None:
        return redirect("/")
    return get_main_dashboard(user_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)