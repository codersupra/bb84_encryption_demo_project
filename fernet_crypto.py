from cryptography.fernet import Fernet
import hashlib
import base64

def bb84_key_to_fernet_key(bb84_key):
    """Converts BB84 key (list of bits) to Fernet-compatible key."""
    bb84_key_str = ''.join(map(str, bb84_key))  # e.g., "01001100..."
    key_hash = hashlib.sha256(bb84_key_str.encode()).digest()
    fernet_key = base64.urlsafe_b64encode(key_hash[:32])
    return fernet_key


def encrypt_message(message: str, fernet_key):
    """Encrypts a plaintext message using Fernet."""
    cipher = Fernet(fernet_key)
    token = cipher.encrypt(message.encode())
    return token


def decrypt_message(token, fernet_key):
    """Decrypts a Fernet token using the Fernet key."""
    cipher = Fernet(fernet_key)
    message = cipher.decrypt(token).decode()
    return message
