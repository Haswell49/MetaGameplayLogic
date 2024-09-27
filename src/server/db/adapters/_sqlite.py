import typing

import aiosqlite

from ._exceptions import RowNotFoundException
from ..formatters import SQLiteFormatter
from .. import abstract


class SQLiteAsyncAdapter(abstract.Adapter):
    connection: aiosqlite.Connection

    formatter: SQLiteFormatter

    @staticmethod
    async def create_connection(db_config: dict):
        return await aiosqlite.connect(**db_config)

    def __init__(self, connection: aiosqlite.Connection, formatter: SQLiteFormatter):
        self.connection = connection
        self.formatter = formatter

    async def insert(self, table_name: str, data: dict) -> None:
        query = self.formatter.insert(table_name, data)

        await self.connection.execute(query)

        await self.connection.commit()

    async def select(self, table_name: str, **filters) -> tuple:
        query = self.formatter.select(table_name, filters)

        cursor = await self.connection.execute(query)

        filters = await cursor.fetchone()

        if not filters:
            raise RowNotFoundException(f"Row with parameters: {filters} not found in table: {table_name}")

        return filters

    async def update(self, table_name: str, data: dict) -> None:
        query = self.formatter.update(table_name, data)

        cursor = await self.connection.execute(query)

        await self.connection.commit()

        return await cursor.fetchone()

    async def delete(self, table_name: str, item_id: typing.Any) -> None:
        query = self.formatter.delete(table_name, item_id)

        await self.connection.execute(query)

        await self.connection.commit()
