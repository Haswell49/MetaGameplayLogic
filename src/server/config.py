from db.adapters import SQLiteAsyncAdapter
from db.formatters import SQLiteFormatter
from db.mappers import SQLiteAsyncMapper

SECRET_KEY = b"ec5336a3f68b3518940bc211a7e5e45b5793f55632e20de92547d63ba4864014"

COOKIES_SECRET_KEY = b"SGVsbG8sIFdvcmxkITIxNXQzMmdhYXMy"

ENCRYPTION_ITER_COUNT = 20000

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8000

DB_CONFIG = {
    "database": "db.sqlite3"
}

SQL_ADAPTER_TYPE = SQLiteAsyncAdapter

SQL_MAPPER_TYPE = SQLiteAsyncMapper

SQL_FORMATTER_TYPE = SQLiteFormatter
