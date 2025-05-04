from flask import Flask, render_template, request, session
from dotenv import load_dotenv
import os

from fitness_monitor_web_app.src.registration_login.landing import process_landing
app = Flask(__name__)

load_dotenv()
app.secret_key = os.getenv("APP_SECRET_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return process_landing(request.form)
    return render_template("landing_page.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)