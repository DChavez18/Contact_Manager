import os
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def load_key():
    return os.getenv("ENCRYPTION_KEY").encode()

def encrypt_message(message):
    key = load_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    key = load_key()
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message