import time
import psycopg2
from flask import Flask

app = Flask(__name__)

def connect_to_db():
    while True:
        try:
            conn = psycopg2.connect(
                host="db",
                database="mydatabase",
                user="postgres",
                password="postgres"
            )
            return conn
        except psycopg2.OperationalError:
            print("Database not ready, retrying in 5 seconds...")
            time.sleep(5)

@app.route('/')
def index():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello, World from PostgreSQL!'")
    result = cursor.fetchone()
    conn.close()
    return result[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
