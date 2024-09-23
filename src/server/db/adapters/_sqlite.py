import typing

import aiosqlite

from src.server.db.formatters import SQLiteFormatter


# TODO: Add an base class for this class
class SQLiteAsyncAdapter:
    connection: aiosqlite.Connection

    formatter: SQLiteFormatter

    def __init__(self, connection: aiosqlite.Connection, formatter: SQLiteFormatter):
        self.connection = connection
        self.formatter = formatter

    async def insert(self, table_name: str, data: dict) -> None:
        query = self.formatter.insert(table_name, data)

        await self.connection.execute(query)

        await self.connection.commit()

    async def select(self, table_name: str, item_id: typing.Any) -> tuple:
        query = self.formatter.select(table_name, item_id)

        cursor = await self.connection.execute(query)

        return await cursor.fetchone()

    async def update(self, table_name: str, data: dict) -> None:
        query = self.formatter.update(table_name, data)

        cursor = await self.connection.execute(query)

        await self.connection.commit()

        return await cursor.fetchone()

    async def delete(self, table_name: str, item_id: typing.Any) -> None:
        query = self.formatter.delete(table_name, item_id)

        await self.connection.execute(query)

        await self.connection.commit()
