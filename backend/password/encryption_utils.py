from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

SECRET_KEY = "YourSecretKeyForEncryption"  # Replace with a secure key in production


def get_encryption_key(user_id: int, master_key: str = SECRET_KEY):
    """Generate a user-specific encryption key based on user ID and master key."""
    salt = str(user_id).encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_key.encode()))
    return key


def encrypt_password(password: str, user_id: int):
    """Encrypt a password using Fernet symmetric encryption."""
    # Get user-specific encryption key
    key = get_encryption_key(user_id)

    # Create a Fernet cipher
    cipher = Fernet(key)

    # Encrypt the password
    encrypted = cipher.encrypt(password.encode())

    # Return encrypted password as a string for storage
    return encrypted.decode()


def decrypt_password(encrypted_password: str, user_id: int):
    """Decrypt a password using Fernet symmetric encryption."""
    # Get user-specific encryption key
    key = get_encryption_key(user_id)

    # Create a Fernet cipher
    cipher = Fernet(key)

    # Decrypt the password
    decrypted = cipher.decrypt(encrypted_password.encode())

    # Return the decrypted password as a string
    return decrypted.decode()
