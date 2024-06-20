from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return "Welcome to the Flask web server with SQLite!"

@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'POST':
        new_user = request.get_json()
        name = new_user['name']
        age = new_user['age']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
        conn.commit()
        conn.close()
        return jsonify({'message': 'User added successfully!'}), 201

    if request.method == 'GET':
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        conn.close()
        return jsonify([dict(ix) for ix in users])

if __name__ == '__main__':
    app.run(debug=True)
