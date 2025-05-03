from flask import Flask
from dotenv import load_dotenv
from psycopg2 import connect
import os

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
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)