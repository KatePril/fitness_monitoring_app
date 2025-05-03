from flask import Flask, request
from dotenv import load_dotenv
from psycopg2 import connect
import os

from entities.health_data import HealthData

load_dotenv()
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")


conn =  connect(database=POSTGRES_DB,
                        user=POSTGRES_USER,
                        password=POSTGRES_PASSWORD,
                        host=POSTGRES_HOST,
                        port=POSTGRES_PORT)
cursor = conn.cursor()

app = Flask(__name__)

@app.route("/", methods=["POST"])
def ingest_data():
    health_data = HealthData(request.get_json())
    query = 'INSERT INTO health_data ("timestamp", heart_rate, saturation, steps, calories, user_id) VALUES (%s, %s, %s, %s, %s, %s)'
    cursor.execute(
        query,
        (
            health_data.timestamp,
            health_data.heart_rate,
            health_data.saturation,
            health_data.steps,
            health_data.calories,
            health_data.user_id
        )
    )
    conn.commit()
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)