import os
import logging
from cryptography.fernet import Fernet

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_key():
    return Fernet.generate_key()

def load_key():
    key = os.getenv("ENCRYPTION_KEY")
    if key is None:
        logger.error("ENCRYPTION_KEY not found in environment variables.")
        raise ValueError("ENCRYPTION_KEY is not set.")
    return key.encode()

def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    logger.info("Message encrypted successfully.")
    return encrypted_message

def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key)
    
    try:
        decrypted_message = fernet.decrypt(encrypted_message).decode()
        logger.info("Message decrypted successfully.")
        return decrypted_message
    except Exception as e:
        logger.error(f"Decryption failed: {e}")
        raise ValueError("Invalid token or decryption failed.")