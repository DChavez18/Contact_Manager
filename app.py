from flask import Flask, request, jsonify, render_template
import psycopg2
from psycopg2 import OperationalError
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Connect to PostgreSQL
def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME", "contact_manager"),  # Default to contact_manager
            user=os.getenv("DB_USER", "your_username"),      # Replace with your PostgreSQL username
            password=os.getenv("DB_PASSWORD", "your_password"),  # Replace with your PostgreSQL password
            host=os.getenv("DB_HOST", "localhost")            # Default to localhost
        )
        return conn
    except OperationalError as e:
        print(f"Error connecting to the database: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts', methods=['GET'])
def get_contacts():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    cur = conn.cursor()
    cur.execute('SELECT * FROM contacts;')
    contacts = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(contacts)

@app.route('/contacts', methods=['POST'])
def add_contact():
    new_contact = request.json
    name = new_contact['name']
    phone = new_contact['phone']
    
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    cur = conn.cursor()
    cur.execute('INSERT INTO contacts (name, phone) VALUES (%s, %s)', (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify(new_contact), 201

if __name__ == '__main__':
    app.run(debug=True)