from hashlib import pbkdf2_hmac

from src.server.config import SECRET_KEY, ENCRYPTION_ITER_COUNT

def encrypt(password: bytes):
    dk = pbkdf2_hmac("sha256", password, SECRET_KEY, ENCRYPTION_ITER_COUNT)