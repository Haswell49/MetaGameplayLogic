import asyncio
import unittest

import aiosqlite

from src.server.db.adapters import SQLiteAsyncAdapter, RowNotFoundException
from src.server.db.mappers import SQLiteAsyncMapper
from src.server.db.models import Item
from src.tests.server.db.mixins import SQLiteAsyncDBSetupMixin, SQLiteAsyncAdapterSetupMixin


class SQLiteAsyncMapperTestCase(unittest.IsolatedAsyncioTestCase, SQLiteAsyncAdapterSetupMixin):
    connection: aiosqlite.Connection

    adapter: SQLiteAsyncAdapter

    mapper: SQLiteAsyncMapper

    model_type: Item

    def setUp(self):
        SQLiteAsyncAdapterSetupMixin.setUp(self)

        self.mapper = SQLiteAsyncMapper(self.adapter, Item)

        asyncio.run(self._reset_tables())

    async def test_create(self):
        item = Item(id=0, name="Battleship", price=200)

        await self.mapper.create(item)

        test_item_values = await self.adapter.select(Item.get_table_name(), item.id)

        test_item_data = {key: value for key, value in zip(Item.get_fields(), test_item_values)}

        test_item = Item(**test_item_data)

        self.assertEqual(test_item, item)

    async def test_select(self):
        item = Item(id=0, name="Battleship", price=200)

        await self.mapper.create(item)

        item = await self.mapper.select(0)

        test_item_values = await self.adapter.select(Item.get_table_name(), item.id)

        test_item_data = {key: value for key, value in zip(Item.get_fields(), test_item_values)}

        test_item = Item(**test_item_data)

        self.assertEqual(test_item, item)

    async def test_update(self):
        item = Item(id=0, name="Battleship", price=200)

        await self.mapper.create(item)

        item = await self.mapper.select(0)

        item.name = "SpeedBoat"
        item.price = 1000

        await self.mapper.update(item)

        test_item_values = await self.adapter.select(Item.get_table_name(), item.id)

        test_item_data = {key: value for key, value in zip(Item.get_fields(), test_item_values)}

        test_item = Item(**test_item_data)

        self.assertEqual(test_item, item)

    async def test_delete(self):
        item = Item(id=0, name="Battleship", price=200)

        await self.mapper.create(item)

        await self.mapper.delete(0)

        try:
            await self.adapter.select(Item.get_table_name(), 0)
        except RowNotFoundException:
            return

        self.fail("Item was not deleted.")


if __name__ == '__main__':
    unittest.main()
