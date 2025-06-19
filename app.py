from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'mydb')
DB_USER = os.getenv('DB_USER', 'postgres')

# Support DB_PASS_FILE secret
if os.getenv('DB_PASS_FILE') and os.path.exists(os.getenv('DB_PASS_FILE')):
    with open(os.getenv('DB_PASS_FILE'), 'r') as f:
        DB_PASS = f.read().strip()
else:
    DB_PASS = os.getenv('DB_PASS', 'password')

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route('/')
def hello():
    return jsonify({"status": "OK", "message": "Flask Microservice Running"})

@app.route('/data')
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify({"database": db_version[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

