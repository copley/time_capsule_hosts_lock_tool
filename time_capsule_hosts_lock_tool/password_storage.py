import os
import hashlib

# Parameters for PBKDF2
ITERATIONS = 100000
ALGORITHM = 'sha256'
SALT_SIZE = 16  # bytes

def hash_password(password: str):
    salt = os.urandom(SALT_SIZE)
    pwd_hash = hashlib.pbkdf2_hmac(ALGORITHM, password.encode(), salt, ITERATIONS)
    return salt, pwd_hash

def verify_password(password: str, salt: bytes, stored_hash: bytes):
    pwd_hash = hashlib.pbkdf2_hmac(ALGORITHM, password.encode(), salt, ITERATIONS)
    return pwd_hash == stored_hash
