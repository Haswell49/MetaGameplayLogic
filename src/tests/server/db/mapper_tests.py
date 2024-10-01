import asyncio
import unittest

import aiosqlite

from src.server.db.adapters import SQLiteAsyncAdapter
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
        item_data = dict(id=0, name="Battleship", price=200)

        instance = await self.mapper.create(**item_data)

        adapter_row = await self.adapter.select(Item.get_table_name(), {"id": instance.id})

        adapter_data = {key: value for key, value in zip(Item.get_fields(), adapter_row)}

        adapter_instance = Item(**adapter_data)

        self.assertEqual(adapter_instance, instance)

    async def test_select(self):
        mapper_data = dict(id=0, name="Battleship", price=200)

        instance: Item = await self.mapper.create(**mapper_data)

        adapter_row = await self.adapter.select(Item.get_table_name(), {"id": instance.id})

        adapter_data = {key: value for key, value in zip(Item.get_fields(), adapter_row)}

        adapter_instance = Item(**adapter_data)

        self.assertEqual(adapter_instance, instance)

    async def test_update(self):
        initial_item_data = dict(id=0, name="Battleship", price=200)

        item = await self.mapper.create(**initial_item_data)

        item.name = "SpeedBoat"
        item.price = 1000

        await self.mapper.update(item)

        updated_item_row = await self.adapter.select(Item.get_table_name(), {"id": item.id})

        self.assertEqual(tuple(item.data.values()), updated_item_row)

    async def test_delete(self):
        item_data = dict(id=0, name="Battleship", price=200)

        item = await self.mapper.create(**item_data)

        item_id = item.id

        await self.mapper.delete(item)

        item = await self.adapter.select(Item.get_table_name(), {"id": item_id})

        if item:
            self.fail("Item was not deleted.")


if __name__ == '__main__':
    unittest.main()
