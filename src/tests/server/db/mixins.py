import asyncio
import os

import aiosqlite

from src.server.db.adapters import SQLiteAsyncAdapter
from src.server.db.formatters import SQLiteFormatter


class SQLiteAsyncDBSetupMixin:
    connection: aiosqlite.Connection

    def setUp(self):
        try:
            os.remove("test_db.sqlite3")
        except FileNotFoundError:
            pass

        async def wrapper():
            self.connection = await aiosqlite.connect("test_db.sqlite3")

        asyncio.run(wrapper())

    def tearDown(self):
        asyncio.run(self.connection.close())

    async def _reset_table(self):
        await self.connection.execute(f"DROP TABLE IF EXISTS {self.table_name};")

        await self.connection.execute(f"CREATE TABLE {self.table_name} ("
                                      "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                                      "name TEXT UNIQUE NOT NULL);")

        await self.connection.commit()


class SQLiteAsyncAdapterSetupMixin(SQLiteAsyncDBSetupMixin):
    adapter: SQLiteAsyncAdapter

    def setUp(self):
        super().setUp()

        formatter = SQLiteFormatter()

        self.adapter = SQLiteAsyncAdapter(self.connection, formatter)
