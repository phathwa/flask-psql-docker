from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            host="db",
            database="mydatabase",
            user="postgres",
            password="postgres"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hello, World from PostgreSQL!'")
        result = cursor.fetchone()
        conn.close()
        return result[0]
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
