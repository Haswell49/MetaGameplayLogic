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
        except PermissionError:
            pass

        async def wrapper():
            self.connection = await aiosqlite.connect("test_db.sqlite3")

        asyncio.run(wrapper())

    def tearDown(self):
        asyncio.run(self.connection.close())

        try:
            os.remove("test_db.sqlite3")
        except FileNotFoundError:
            pass
        except PermissionError:
            pass

    async def _reset_tables(self):
        drop_file = open("./src/server/db/sql/drop_tables.sql")
        await self.connection.executescript(drop_file.read())

        create_file = open("./src/server/db/sql/create_tables.sql")
        await  self.connection.executescript(create_file.read())

        drop_file.close()
        create_file.close()

        await self.connection.commit()


class SQLiteAsyncAdapterSetupMixin(SQLiteAsyncDBSetupMixin):
    adapter: SQLiteAsyncAdapter

    def setUp(self):
        super().setUp()

        formatter = SQLiteFormatter()

        self.adapter = SQLiteAsyncAdapter(self.connection, formatter)
