import asyncio
import os
import unittest

import aiosqlite

from src.server.db.adapters import SQLiteAsyncAdapter
from src.server.db.formatters import SQLiteFormatter
from src.tests.server.db.mixins import SQLiteAsyncDBSetupMixin


class SQLiteAsyncAdapterTestCase(unittest.IsolatedAsyncioTestCase, SQLiteAsyncDBSetupMixin):
    adapter: SQLiteAsyncAdapter

    table_name = "users"
    data = {"id": 0,
            "name": "selim"}

    async def test_create(self):
        await self._reset_table()

        creation_data = {key: value for key, value in self.data.items() if key != "id"}

        await self.adapter.insert(self.table_name, creation_data)

        cursor = await self.connection.execute(f"SELECT * FROM {self.table_name} WHERE name='{self.data['name']}'")

        data_from_connector = await cursor.fetchone()

        self.assertEqual(data_from_connector[1], self.data["name"])

    async def test_select(self):
        await self._reset_table()

        await self.adapter.insert(self.table_name, self.data)

        adapter_data = await self.adapter.select(self.table_name, self.data["id"])

        cursor = await self.connection.execute(f"SELECT * FROM {self.table_name} WHERE id={self.data['id']};")
        data_from_connector = await cursor.fetchone()

        self.assertEqual(data_from_connector, adapter_data)

    async def test_update(self):
        await self._reset_table()

        await self.adapter.insert(self.table_name, self.data)

        new_name = "hello"

        await self.adapter.update(self.table_name, {"id": self.data["id"], "name": new_name})

        find_data = await self.adapter.select(self.table_name, self.data["id"])

        self.assertEqual(find_data, (self.data["id"], new_name))

    async def test_delete(self):
        await self._reset_table()

        await self.adapter.insert(self.table_name, self.data)

        await self.adapter.delete(self.table_name, self.data["id"])

        cursor = await self.connection.execute(f"SELECT * FROM {self.table_name} WHERE id={self.data['id']}")

        result = await cursor.fetchone()

        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()
