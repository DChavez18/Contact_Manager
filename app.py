from flask import Flask, request, jsonify, render_template
import psycopg2
from psycopg2 import OperationalError
import os
from dotenv import load_dotenv
from logger_config import setup_logger
import pyshark
from encryption import encrypt_message, decrypt_message  # Import encryption functions

load_dotenv()

app = Flask(__name__)

logger = setup_logger()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME", "contact_manager"),
            user=os.getenv("DB_USER", "your_username"),
            password=os.getenv("DB_PASSWORD", "your_password"),
            host=os.getenv("DB_HOST", "localhost")
        )
        return conn
    except OperationalError as e:
        logger.error(f"Error connecting to the database: {e}")  
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts', methods=['GET'])
def get_contacts():
    conn = get_db_connection()
    if conn is None:
        logger.error("Database connection failed in GET /contacts")  
        return jsonify({"error": "Database connection failed"}), 500

    cur = conn.cursor()
    cur.execute('SELECT * FROM contacts;')
    contacts = cur.fetchall()
    cur.close()
    conn.close()

    # Decrypt phone numbers
    decrypted_contacts = []
    for contact in contacts:
        name = contact[0]
        encrypted_phone = contact[1]
        phone = decrypt_message(encrypted_phone)  # Decrypt the phone number
        decrypted_contacts.append((name, phone))
        
    logger.info("Fetched contacts successfully")  
    return jsonify(decrypted_contacts)  # Return decrypted contacts

@app.route('/contacts', methods=['POST'])
def add_contact():
    new_contact = request.json
    name = new_contact['name']
    phone = new_contact['phone']
    
    # Encrypt the phone number
    encrypted_phone = encrypt_message(phone)

    conn = get_db_connection()
    if conn is None:
        logger.error("Database connection failed in POST /contacts")
        return jsonify({"error": "Database connection failed"}), 500

    cur = conn.cursor()
    cur.execute('INSERT INTO contacts (name, phone) VALUES (%s, %s)', (name, encrypted_phone))
    conn.commit()
    cur.close()
    conn.close()
    
    logger.info(f"Added new contact: {name}, {phone}")  
    return jsonify(new_contact), 201

@app.route('/capture', methods=['GET'])
def capture_packets():
    capture = pyshark.LiveCapture(interface='en0')
    packets = []

    try:
        for packet in capture.sniff_continuously(packet_count=10):
            packets.append(str(packet))
        logger.info("Captured packets successfully")
    except Exception as e:
        logger.error(f"Error capturing packets: {e}")
        return jsonify({"error": "Packet capture failed"}), 500

    return jsonify(packets), 200

if __name__ == '__main__':
    app.run(debug=True, port=5001)