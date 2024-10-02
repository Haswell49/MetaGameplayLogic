import os

from dotenv import load_dotenv

from db.adapters import SQLiteAsyncAdapter
from db.formatters import SQLiteFormatter
from db.mappers import SQLiteAsyncMapper

load_dotenv(".env.shared")
load_dotenv(".env.sensitive")

SECRET_KEY = os.environ.get("SECRET_KEY").encode("utf-8")

COOKIES_SECRET_KEY = os.environ.get("COOKIES_SECRET_KEY").encode("utf-8")

ENCRYPTION_ITER_COUNT = int(os.environ.get("ENCRYPTION_ITER_COUNT"))

SERVER_HOST = os.environ.get("SERVER_HOST")
SERVER_PORT = int(os.environ.get("SERVER_PORT"))

DB_CONFIG = {
    "database": os.environ.get("DB_NAME")
}

SQL_ADAPTER_TYPE = SQLiteAsyncAdapter

SQL_MAPPER_TYPE = SQLiteAsyncMapper

SQL_FORMATTER_TYPE = SQLiteFormatter
