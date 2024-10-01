import typing

import aiosqlite

from .. import abstract
from ..formatters import SQLiteFormatter


class SQLiteAsyncAdapter(abstract.AsyncAdapter):
    connection: aiosqlite.Connection

    formatter: SQLiteFormatter

    @staticmethod
    async def create_connection(db_config: dict) -> aiosqlite.Connection:
        return await aiosqlite.connect(**db_config)

    def __init__(self, connection: aiosqlite.Connection, formatter: SQLiteFormatter):
        self.connection = connection
        self.formatter = formatter

    async def insert(self, table_name: str, data: dict) -> str | int:
        query = self.formatter.insert(table_name, data)

        cursor = await self.connection.execute(query)

        await self.connection.commit()

        return cursor.lastrowid

    async def select(self, table_name: str, data: dict) -> tuple:
        query = self.formatter.select(table_name, data)

        cursor = await self.connection.execute(query)

        data = await cursor.fetchone()

        return data

    async def update(self, table_name: str, data: dict) -> None:
        query = self.formatter.update(table_name, data)

        cursor = await self.connection.execute(query)

        await self.connection.commit()

        return await cursor.fetchone()

    async def delete(self, table_name: str, pk: typing.Any) -> None:
        query = self.formatter.delete(table_name, pk)

        await self.connection.execute(query)

        await self.connection.commit()
