from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Connect to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        dbname="contact_manager",
        user="your_username",  # replace with your PostgreSQL username
        password="your_password",  # replace with your PostgreSQL password
        host="localhost"
    )
    return conn

@app.route('/contacts', methods=['GET'])
def get_contacts():
    conn = get_db_connection()
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
    cur = conn.cursor()
    cur.execute('INSERT INTO contacts (name, phone) VALUES (%s, %s)', (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify(new_contact), 201

if __name__ == '__main__':
    app.run(debug=True)