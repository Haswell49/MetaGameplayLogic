from hashlib import pbkdf2_hmac

from config import SECRET_KEY, ENCRYPTION_ITER_COUNT


def encrypt(password: str):
    dk = pbkdf2_hmac("sha256", password.encode("utf-8"), SECRET_KEY, ENCRYPTION_ITER_COUNT)

    return dk.hex()
