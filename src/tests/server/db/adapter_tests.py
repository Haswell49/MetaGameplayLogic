import asyncio
import os
import unittest

import aiosqlite

from src.server.db.adapters import SQLiteAsyncAdapter
from src.server.db.formatters import SQLiteFormatter
from src.tests.server.db.mixins import SQLiteAsyncDBSetupMixin, SQLiteAsyncAdapterSetupMixin


class SQLiteAsyncAdapterTestCase(unittest.IsolatedAsyncioTestCase, SQLiteAsyncAdapterSetupMixin):
    adapter: SQLiteAsyncAdapter

    table_name = "users"
    data = {"id": 1,
            "email": "test@gmail.com",
            "password": "<PASSWORD>"}

    def setUp(self):
        SQLiteAsyncAdapterSetupMixin.setUp(self)

        asyncio.run(self._reset_tables())

    async def test_create(self):
        creation_data = {key: value for key, value in self.data.items() if key != "id"}

        await self.adapter.insert(self.table_name, creation_data)

        cursor = await self.connection.execute(f"SELECT * FROM {self.table_name} WHERE email='{self.data['email']}'")

        data_from_connector = await cursor.fetchone()

        self.assertEqual(data_from_connector, tuple(self.data.values()))

    async def test_select(self):
        await self.adapter.insert(self.table_name, self.data)

        adapter_data = await self.adapter.select(self.table_name, self.data["id"])

        cursor = await self.connection.execute(f"SELECT * FROM {self.table_name} WHERE id={self.data['id']};")
        data_from_connector = await cursor.fetchone()

        self.assertEqual(data_from_connector, adapter_data)

    async def test_update(self):
        await self.adapter.insert(self.table_name, self.data)

        new_email = "hello@gmail.com"

        await self.adapter.update(self.table_name, {"id": self.data["id"], "email": new_email})

        find_data = await self.adapter.select(self.table_name, self.data["id"])

        new_data = tuple(value if key != "email" else new_email for key, value in self.data.items())

        self.assertEqual(find_data, new_data)

    async def test_delete(self):
        await self.adapter.insert(self.table_name, self.data)

        await self.adapter.delete(self.table_name, self.data["id"])

        cursor = await self.connection.execute(f"SELECT * FROM {self.table_name} WHERE id={self.data['id']}")

        result = await cursor.fetchone()

        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()
