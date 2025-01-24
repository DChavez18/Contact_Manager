import os
from dotenv import load_dotenv
from encryption import generate_key, encrypt_message, decrypt_message, load_key

load_dotenv()


key = load_key()
print(f"Loaded Key: {key.decode()}")

original_message = "Hello, World!"
encrypted = encrypt_message(original_message)
print(f"Encrypted: {encrypted}")

decrypted = decrypt_message(encrypted)
print(f"Decrypted: {decrypted}")  # Should print "Hello, World!"